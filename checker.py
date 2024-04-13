import json

pict = """
MY FIRST SKRIPT

    /------/
   /      /|
  /      / |
 /------/  |
 |      |  /
 |      | /
 |______|/

I LOVE PYTHON
"""
print(pict)


statistics_dict = {'avg_diag': 19.4,
                    'avg_volume': 1083.1,
                    'avg_surface_area': 627.7,
                    'avg_alpha': 56.7,
                    'avg_beta': 57.8,
                    'avg_gamma': 55.5,
                    'avg_radius_described_sphere': 9.7,
                    'avg_volume_described_sphere': 4652.9}

with open('statistics.json', 'r' ) as f:
  statistics_to_check = json.load(f)

total = '--------ALL IS GOOD !!!--------'
for fun in statistics_dict:
  if round(float(statistics_to_check[fun]), 1) != statistics_dict[fun]:
    print(f'!!! {fun} NOT CORRECT !!!')
    total = '--------NOT GOOD !!!--------'
  else:
    print('CORRECT')
    
print(total)