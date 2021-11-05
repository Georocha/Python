medida = float(input('Digite uma distância em Metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print(' A distância de {} metros equivalente a {} decímetro,  {} centímetros e a {} milímetros'.format(medida, dm, cm, mm))
print('Em Quilômetro {}, Hectômetro {} , Decâmetro {} '.format(km, hm, dam))


