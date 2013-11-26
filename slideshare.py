import MySQLdb as mdb
import xlrd
import datetime
import pandas as pd

f_sh=pd.open_workbook('slideshare1.xlsx')

row1=f_sh.row(1)
row2=f_sh.row(2)
row3=f_sh.row(3)
row4=f_sh.row(4)
row5=f_sh.row(5)
row6=f_sh.row(6)
row7=f_sh.row(7)
row8=f_sh.row(8)
row9=f_sh.row(9)
row10=f_sh.row(10)
row11=f_sh.row(11)
row12=f_sh.row(12)
row13=f_sh.row(13)
row14=f_sh.row(14)
row15=f_sh.row(15)
row16=f_sh.row(16)
row17=f_sh.row(17)
row18=f_sh.row(18)
row19=f_sh.row(19)

con = mdb.connect('intuittest.cq2mgcdwryfy.us-west-1.rds.amazonaws.com', 'root', 'password', 'jenndb');
for i in range(0,8):
	with con:
 		cur = con.cursor()
 		cur.execute("UPDATE Slideshare SET Presentation=%s, Views=%s, Downloads=%s, Favorites=%s, Comments=%s, Email_Shares=%s, FB_Shares=%s, Tweets=%s, Linkedin_Shares=%s WHERE id=%s",  (str(row1[i].value),
																																															str(row2[i].value),
																																															str(row3[i].value),	
																																															str(row4[i].value),		
																																															str(row5[i].value),
																																															str(row6[i].value),
																																															str(row7[i].value),
																																															str(row8[i].value),
																																															str(row9[i].value),
																																															str(row10[i].value),
																																															str(row11[i].value),
																																															str(row12[i].value),
																																															str(row13[i].value),
																																															str(row14[i].value),
																																															str(row15[i].value),
																																															str(row16[i].value),
																																															str(row17[i].value),
																																															str(row18[i].value),
																																															str(row19[i].value)

																																															
																																															))		
																																															



																																															

																																																																																																							    