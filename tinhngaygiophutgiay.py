while True:
  ss = int(input('Nhập số giây: '))
  while int(ss) < 0:
      print('Vui lòng nhập lại!')
      ss = int(input('Nhập số giây: '))
  ngay = ss // (24 * 60 * 60)
  gio = ss % (24 * 60 * 60) // 3600
  phut = ss % (24 * 60 * 60) % 3600 // 60
  giay = ss % (24 * 60 * 60) % 3600 % 60
  print(f'Ngày: {ngay} Giờ: {gio} Phút: {phut} Giây: {giay}')
