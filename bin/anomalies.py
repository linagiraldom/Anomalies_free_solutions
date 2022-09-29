#!/usr/bin/env python3

from anomalies_sol import Anomalies_free_solutions
import argparse

parser = argparse.ArgumentParser()parser = argparse.ArgumentParser()
parser.add_argument("n", help="Valor de n para el cual se van a calcular las soluciones",
                    type=int)
parser.add_argument("--zmax", help="Valor absoluto del entero más grande que puede contener las soluciones",
                    type=int)
parser.add_argument("--m", help="Entero máximo que contendrán l y k",
                    type=int)
parser.add_argument("--output_name", "-on", help="Guardar soluciones en un archivo json con nombre el nombre dado por el usuario")                    

parser.add_argument("--cores", "-c", help="Cuántos núcleos desea usar para el multiprocessing",
                    type=int)
args = parser.parse_args()


if args.cores and args.zmax and args.m:
    results = Anomalies_free_solutions.run(args.n, use=args.cores, zmax=args.zmax, dmax=args.m)
elif args.cores and args.m:
    results = Aresults = Anomalies_free_solutions.run(args.n, use=args.cores, dmax=args.m)
elif args.m and args.zmax:
    results = Anomalies_free_solutions.run(args.n, use=args.cores, dmax=args.m)
elif args.cores and args.zmax:
    results = Anomalies_free_solutions.run(args.n, use=args.cores, zmax=args.zmax)
elif args.zmax:
    results = Anomalies_free_solutions.run(args.n, zmax=args.zmax)
elif args.cores:
    results = Anomalies_free_solutions.run(args.n, use=args.cores)
elif args.m:
    results = Anomalies_free_solutions.run(args.n, dmax=args.m)
else:
    results = Anomalies_free_solutions.run(args.n)

if args.output_name:
    results.to_json(f'{args.output_name}.json',orient='records')
else:
    print(results)
