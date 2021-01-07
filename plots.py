import os
from asreviewcontrib.visualization import Plot


dic = { "simoutput/nb" : "naive Bayes",
       "simoutput/logistic" : "logistic regression"
      }

with Plot.from_paths(dic) as plot:
    all_files = all(plot.is_file.values())
    inc_plot = plot.new("inclusion")
    inc_plot.set_grid()
    for key in list(plot.analyses):
        if all_files or not plot.is_file[key]:
            inc_plot.add_WSS(key, 95, add_text = False)
            inc_plot.add_RRF(key, 10, add_text = False)
    #inc_plot.set_xlim(0, 50)
    #inc_plot.set_ylim(0, 101)
    inc_plot.add_random(add_text = False)
    inc_plot.set_legend()
    inc_plot.save("nb_lr2.pdf")
