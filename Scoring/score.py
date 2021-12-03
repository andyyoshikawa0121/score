import glob
import subprocess
import os
import pathlib
import shutil
import openpyxl

if __name__ == '__main__':
  # ファイルのrename
  # files = glob.glob("./prog2/*.c")

  # student_num_list = list(map(lambda file: file.split()[0].replace("./prog2/", ""), files))
  # for index, file in enumerate(files):
  #   os.rename(file, f"./prog2/{student_num_list[index]}.c")

  # ファイルの採点

  files = glob.glob("./prog2/*.c")
  input_files = glob.glob("./src/*.txt")
  wb = openpyxl.load_workbook("saiten.xlsx")
  ws = wb["4回プログラミング演習"]

  for student_index, file in enumerate(files):
    # 学籍番号をシートに書き込み
    cell = ws.cell(row=student_index + 1, column=1)
    cell.value = file.replace('./prog2/', '').replace('.c', '')

    for input_index, input in enumerate(input_files):
      shutil.copy(input, './input.txt')
      os.system("gcc %s" % file)
      # 正しくコンパイルされ a.outがあるか
      if os.path.exists('./a.out'):
        result = subprocess.Popen('./a.out', stdout=subprocess.PIPE).communicate()[0].decode('utf-8')

        # 出力をシートに書き込み
        output_cell = ws.cell(row=student_index + 1, column=input_index + 2)
        output_cell.value = result
        # a.outを削除
        os.remove('./a.out')
      else:
        # 出力をシートに書き込み
        output_cell = ws.cell(row=student_index + 1, column=input_index + 2)
        output_cell.value = "compile was failed"
  
  wb.save("saiten.xlsx")
  wb.close()