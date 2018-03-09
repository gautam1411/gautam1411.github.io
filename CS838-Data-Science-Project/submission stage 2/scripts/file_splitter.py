#!/usr/bin/python
#Splits the data in development set and test set

if __name__ == "__main__":
    
    pfile = open("food_feature_vector_data_.txt", "r")
    nfile = open("non_food_feature_vector_data_.txt","r")
    dset_tr_data = open("t_data/devset_training_data.txt","w")
    dset_test_data = open("t_data/devset_test_data.txt","w")
    tset_data = open("t_data/tset_data.txt","w")
    
    p_count = 0
    n_count = 0
    
    #pushing postive labelled data
    
    for line in pfile:
        if p_count < 300:
            dset_tr_data.write(line)
        elif p_count < 400:
            dset_test_data.write(line)
        elif p_count < 500:
            tset_data.write(line)
        else:
            break
        p_count += 1
    
    #pushing negative labelled data
    
    for line in nfile:
        if n_count < 200:
            dset_tr_data.write(line)
        elif n_count < 266:
            dset_test_data.write(line)
        elif n_count < 332:
            tset_data.write(line)
        else:
            break
        n_count += 1
    
    pfile.close()
    nfile.close()
    dset_tr_data.close()
    dset_test_data.close()
    tset_data.close()
    
                