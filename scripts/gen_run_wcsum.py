import os

langs = ['da', 'sv', 'bg', 'ru', 'es', 'pt']

with open("run_gpu.sh") as f:
  data = f.readlines()

pyscript = "python tagger.py --gpu --langs language --sum_word_char --test"

for lang in langs:
  wdata = data + [pyscript.replace("language", lang)]
  script_name = "scripts/run_tagger_" + lang + "_wcsum-all.sh"
  with open(script_name, 'w') as f:
    f.writelines(wdata)
  os.system("sbatch -J " + lang + "_wcsum-all " + script_name)
