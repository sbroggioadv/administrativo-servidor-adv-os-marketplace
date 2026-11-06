"""H01/H02/H04: aritmética condicionada, sem decidir enquadramento jurídico."""
import argparse
import calendar
from datetime import date, timedelta
import json
import sys

VERSAO = '0.1.0'
FONTE = {'geral': 'Lei 9.784 arts. 59/66/67/69; context/A-lei9784.md',
         'estatutario': 'Lei 8.112 art. 238 e dispositivo da quantidade/marco; context/A-lei8112.md',
         'judicial': 'CPC arts. 219/220/224/231; context/A-cpc.md'}

REGRA = {
    ('geral', 'dias'): ('exclui o dia do começo e inclui o do vencimento; dias contínuos; vencimento em dia sem expediente prorroga ao primeiro dia seguinte com expediente',
                        'Lei 9.784, art. 66, caput e §§1º-2º (context/A-lei9784.md:950-960)'),
    ('geral', 'meses'): ('data a data; sem dia equivalente no mês do vencimento, último dia do mês; vencimento sem expediente prorroga',
                         'Lei 9.784, art. 66, §§1º e 3º (context/A-lei9784.md:954-965)'),
    ('estatutario', 'dias'): ('dias corridos; exclui o dia do começo e inclui o do vencimento; vencido em dia sem expediente, prorroga ao primeiro dia útil seguinte',
                              'Lei 8.112, art. 238 (context/A-lei8112.md:6013-6016)'),
    ('judicial', 'dias'): ('somente dias úteis; exclui o dia do começo e inclui o do vencimento; suspensão de 20/12 a 20/01; dias sem expediente informados excluídos',
                           'CPC, arts. 219, 220 e 224 (context/A-cpc.md:2041, 2045, 2077-2079)'),
}
REGRA[('geral', 'anos')] = REGRA[('geral', 'meses')]

class Parser(argparse.ArgumentParser):
    def error(self, message):
        raise ValueError(message)

def build_parser():
    p = Parser(description=__doc__)
    p.add_argument('--regime', choices=['geral', 'estatutario', 'judicial'])
    p.add_argument('--marco')
    p.add_argument('--quantidade', type=int)
    p.add_argument('--unidade', choices=['dias', 'meses', 'anos'])
    p.add_argument('--calendario-json')
    p.add_argument('--calendario-confirmado', action='store_true')
    p.add_argument('--json', action='store_true')
    p.add_argument('--versao', action='store_true', help='imprime a versão do script e sai')
    return p

def calcular(a):
    used = vars(a).copy()
    if a.quantidade is not None and not 1 <= a.quantidade <= 3660:
        raise ValueError('quantidade deve estar entre 1 e 3660')
    if a.unidade and a.regime in ('judicial', 'estatutario') and a.unidade != 'dias':
        raise ValueError('este recorte judicial/estatutário aceita somente dias')
    start = date.fromisoformat(a.marco) if a.marco else None
    closed = None
    if a.calendario_json is not None:
        values = json.loads(a.calendario_json)
        if not isinstance(values, list) or any(not isinstance(x, str) for x in values):
            raise ValueError('calendario-json deve ser lista de datas ISO sem expediente')
        closed = {date.fromisoformat(x) for x in values}
    if not all((a.regime, start, a.quantidade, a.unidade, a.calendario_confirmado)) or closed is None:
        return 3, {'versao': VERSAO, 'parametros_usados': used, 'resultado': None,
                   'formula_aberta': 'Selecionar regime, marco jurídico excluído, quantidade/unidade e calendário completo confirmado; contar e conferir expediente final.',
                   'pendencia': 'PENDENTE DE PROVA', 'fonte': FONTE.get(a.regime),
                   'memoria': ['Não presumir marco nem calendário; nenhuma data final calculada.']}
    def eligible(d):
        if d in closed:
            return False
        if a.regime == 'judicial':
            if d.weekday() >= 5:
                return False
            if (d.month == 12 and d.day >= 20) or (d.month == 1 and d.day <= 20):
                return False
        return True
    steps = ['Marco excluído: ' + start.isoformat(), 'Calendário e regime são premissas confirmadas externamente, não certificados pelo script.']
    if a.unidade == 'dias':
        end = start
        counter = 0
        while counter < a.quantidade:
            end += timedelta(days=1)
            if a.regime != 'judicial' or eligible(end):
                counter += 1
                steps.append(f'{end.isoformat()}: dia {counter}')
            else:
                steps.append(f'{end.isoformat()}: excluído (expediente/fim de semana/suspensão processual)')
    else:
        months = a.quantidade * (12 if a.unidade == 'anos' else 1)
        absolute = start.year * 12 + start.month - 1 + months
        year, month = divmod(absolute, 12)
        month += 1
        end = date(year, month, min(start.day, calendar.monthrange(year, month)[1]))
        steps.append('Data a data, último dia do mês se não houver equivalente: ' + end.isoformat())
    limit = 0
    while not eligible(end):
        steps.append(end.isoformat() + ': sem expediente final; prorrogar')
        end += timedelta(days=1)
        limit += 1
        if limit > 3660:
            raise ValueError('calendário sem dia final elegível no limite do recorte')
    if a.regime in ('geral', 'estatutario') and (end.weekday() >= 5 or not closed):
        steps.append('ALERTA: termo em sábado/domingo ou possível feriado não informado no calendário vazio; o termo pode prorrogar para o próximo dia útil; conferir o calendário. Data 🟡 condicional, sem inferir feriado ou expediente.')
    return 0, {'versao': VERSAO, 'parametros_usados': used,
               'resultado': {'data_limite': end.isoformat()}, 'memoria': steps,
               'numeros': {'data_limite': {'valor': end.isoformat(), 'regra': REGRA[(a.regime, a.unidade)][0], 'fonte': REGRA[(a.regime, a.unidade)][1]}},
               'fonte': FONTE[a.regime], 'formula_aberta': None,
               'limites': 'Não decide direito, termo inicial, quantidade legal, dobro, prorrogação especial ou efeitos do polo. MS e prescrição excluídos.'}

def main(argv=None):
    try:
        args = build_parser().parse_args(argv)
        if args.versao:
            print(json.dumps({'versao': VERSAO, 'script': __file__.rsplit('/', 1)[-1]}, ensure_ascii=False))
            return 0
        status, result = calcular(args)
    except Exception as exc:
        status, result = 2, {'versao': VERSAO, 'erro': str(exc), 'resultado': None}
    print(json.dumps(result, ensure_ascii=False))
    return status

if __name__ == '__main__':
    sys.exit(main())
