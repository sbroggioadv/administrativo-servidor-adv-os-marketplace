"""H07: natalina federal sob base e meses confirmados pelo advogado."""
import argparse
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
import json
import sys

VERSAO = '0.1.0'
FONTE = 'Lei 8.112 art. 63 (context/A-lei8112.md:1707-1712); art. 65 só se a hipótese confirmada for exoneração'
REGRA_AVOS = ('meses de exercício no ano; fração igual ou superior a 15 dias conta como mês integral',
              'Lei 8.112, art. 63, parágrafo único (context/A-lei8112.md:1711-1712)')
REGRA_VALOR = ('1/12 da remuneração da hipótese confirmada por mês de exercício: base / 12 x avos; '
               'Decimal com arredondamento final ROUND_HALF_UP em centavos',
               'Lei 8.112, art. 63, caput (context/A-lei8112.md:1707-1709)')

class Parser(argparse.ArgumentParser):
    def error(self, message):
        raise ValueError(message)

def build_parser():
    p = Parser(description=__doc__)
    p.add_argument('--remuneracao')
    p.add_argument('--meses', type=int)
    p.add_argument('--fracao-dias', type=int)
    p.add_argument('--base-confirmada', action='store_true')
    p.add_argument('--json', action='store_true')
    p.add_argument('--versao', action='store_true', help='imprime a versão do script e sai')
    return p

def calcular(a):
    used = vars(a).copy()
    value = Decimal(a.remuneracao) if a.remuneracao is not None else None
    if value is not None and (not value.is_finite() or value < 0 or value > Decimal('1000000000000')):
        raise ValueError('remuneração deve ser finita, não negativa e dentro do recorte')
    if a.meses is not None and not 0 <= a.meses <= 12:
        raise ValueError('meses deve estar entre 0 e 12')
    if a.fracao_dias is not None and not 0 <= a.fracao_dias <= 31:
        raise ValueError('fração de mês deve estar entre 0 e 31 dias')
    if value is None or a.meses is None or a.fracao_dias is None or not a.base_confirmada:
        return 3, {'versao': VERSAO, 'parametros_usados': used, 'resultado': None,
                   'formula_aberta': 'remuneração da hipótese legal / 12 × (meses integrais + fração adicional >=15 dias, sem duplicar mês)',
                   'fonte': FONTE, 'memoria': ['Base/períodos pendentes; não preencher com estimativa.'], 'pendencia': 'PENDENTE DE PROVA'}
    avos = a.meses + int(a.fracao_dias >= 15)
    if avos > 12:
        raise ValueError('fração duplica mês ou excede doze avos')
    total = (value * avos / Decimal(12)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    return 0, {'versao': VERSAO, 'parametros_usados': used, 'resultado': {'natalina_bruta': str(total), 'avos': avos},
               'memoria': [f'Base da hipótese confirmada: {value}', f'Meses integrais: {a.meses}; fração adicional: {a.fracao_dias}; avos: {avos}',
                           f'{value} × {avos} / 12 = {total}; arredondamento final ROUND_HALF_UP'],
               'numeros': {'avos': {'valor': avos, 'regra': REGRA_AVOS[0], 'fonte': REGRA_AVOS[1]},
                           'natalina_bruta': {'valor': str(total), 'regra': REGRA_VALOR[0], 'fonte': REGRA_VALOR[1]}},
               'fonte': FONTE, 'formula_aberta': None, 'limites': 'Não decide rubricas, afastamentos, direito à verba ou descontos/pagamentos não fornecidos.'}

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
