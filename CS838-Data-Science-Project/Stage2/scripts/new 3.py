for i,l in enumerate(open('test_set_tagged_data.csv')):
  f = open('new_file_%i.txt' % i, 'w')
  f.write(l)
  f.close()
