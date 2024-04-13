import json
import parallelepipeds_hepler as hepler


pict = """
MY FIRST SCRIPT

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

parallelepipeds = {}
with open('parallelepipeds.json', 'r') as f:
    parallelepipeds = json.load(f)


def get_characteristics(parallels:dict) -> dict:
    temp = {}
    for k, v in parallels.items():
        diag_ = hepler.diag(int(v.get('a')), int(v.get('b')), int(v.get('c')))
        radius_d_s_ = hepler.radius_desc_sph(diag_)
        temp[k] = {
            "diag": str(round(diag_, 2)),
            "volume": str(round(hepler.volume(int(v.get('a')), int(v.get('b')), int(v.get('c'))), 2)),
            "surface_area": str(round(hepler.surface_area(int(v.get('a')), int(v.get('b')), int(v.get('c'))), 2)),
            "alpha": str(round(hepler.alpha(int(v.get('a')), diag_), 2)),
            "beta": str(round(hepler.beta(int(v.get('b')), diag_), 2)),
            "gamma": str(round(hepler.gamma(int(v.get('c')), diag_), 2)),
            "radius_described_sphere": str(round(radius_d_s_, 2)),
            "volume_described_sphere": str(round(hepler.volume_desc_sph(radius_d_s_), 2))
        }
    return temp

characteristics = get_characteristics(parallelepipeds)
    
with open('characteristics.json', 'w') as f:
    json.dump(characteristics, f, indent=4)

print(f'Total number of figures: {len(parallelepipeds)}')

def get_statistics(characters:dict) ->dict:
    temp = {}
    diag_lst = []
    volume_lst = []
    surface_area_lst = []
    alpha_lst = []
    beta_lst = []
    gamma_lst = []
    rds_lst = []
    vds_lst = []
    
    for figure in characters.values():
        diag_lst.append(float(figure.get('diag')))
        volume_lst.append(float(figure.get('volume')))
        surface_area_lst.append(float(figure.get('surface_area')))
        alpha_lst.append(float(figure.get('alpha')))
        beta_lst.append(float(figure.get('beta')))
        gamma_lst.append(float(figure.get('gamma')))
        rds_lst.append(float(figure.get('radius_described_sphere')))
        vds_lst.append(float(figure.get('volume_described_sphere')))

    temp['avg_diag'] = str(round(hepler.average(diag_lst), 2))
    temp['avg_volume'] = str(round(hepler.average(volume_lst), 2))
    temp['avg_surface_area'] = str(round(hepler.average(surface_area_lst), 2))
    temp['avg_alpha'] = str(round(hepler.average(alpha_lst), 2))
    temp['avg_beta'] = str(round(hepler.average(beta_lst), 2))
    temp['avg_gamma'] = str(round(hepler.average(gamma_lst), 2))
    temp['avg_radius_described_sphere'] = str(round(hepler.average(rds_lst), 2))
    temp['avg_volume_described_sphere'] = str(round(hepler.average(vds_lst), 2))
    
    return temp

statistics = get_statistics(characteristics)

with open('statistics.json', 'w') as f:
    json.dump(statistics, f, indent=4)

print(f"""
Среднее всех главных диагоналей:              {statistics['avg_diag']}
Средний объем параллелограммов:               {statistics['avg_volume']}
Средняя площадь поверхностей параллелограмов: {statistics['avg_surface_area']}
Средний угол между диагональю и стороной a:   {statistics['avg_alpha']}
Средний угол между диагональю и стороной b:   {statistics['avg_beta']}
Средний угол между диагональю и стороной c:   {statistics['avg_gamma']}
Средний радиус описаной сферы:                {statistics['avg_radius_described_sphere']}
Средний объем описаной сферы:                 {statistics['avg_volume_described_sphere']}
      """)
