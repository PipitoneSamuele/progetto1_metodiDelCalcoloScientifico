from scipy.io import mmread

a = mmread("libreria_s_pipitone_830595_py//resources//data//spa1.mtx")

print(a.A)