from flask import*
from flask import request
import datetime as dt
from flask import request
import os
import shutil as sl
class arw:
		def add_issue(a):
			open("ISSUES/"+str(dt.datetime.now()).replace(":","").replace(".","")+".txt","a").write(a)
		def add_post(a,b):
				name="static/"+str(dt.datetime.now()).replace(":","").replace(".","")+" "+a
				open(name,"a").write(b)
		def get_content():
				l = os.listdir("static")
				l.reverse()
				n=0
				k=""
				if (l==None):
					return ""
				else:
					while(len(l)>n):
						k=k+open("static/"+l[n],"r+").read()+"\n<br><br>"
						n=n+1
					return k
		def change_password(a,b):
				os.rename("ACC/"+b+"/"+os.listdir("ACC/"+b)[1],"ACC/"+b+"/Password-"+a)
		def create(a,b,c):
				if (a in os.listdir("ACC")):
					return "X"
				else:
					os.mkdir("ACC/"+a)
					os.mkdir("ACC/"+a+"/"+"Name-"+c)
					os.mkdir("ACC/"+a+"/"+"Password-"+b)
					return "Y"
		def delete_comment(a):
				bc = os.listdir("static")
				n=0
				while(len(bc)>n):
					if(a == bc[n].split(" ")[2]):
						os.remove("static/"+bc[n])
					else:
						tg=""
					n=n+1
		def delete(a):
			arw.delete_comment(a)
			sl.rmtree("ACC/"+a)
		def verify(a,b):
				if (a in os.listdir("ACC")):
						f = os.listdir("ACC/"+a)
						n=0
						k=[]
						while(len(f) > n):
								if ("Password-"in f[n]):
										if(b == f[n].replace("Password-","")):
												k.append("d")
										else:
												jk=""
								else:
										jk=""
								n=n+1
						if (len(k)>0):
								return "Y"
						else:
								return "Xpassword"
				else:
						return "X"
app = Flask(__name__,static_folder=os.getcwd().replace("\\","/")+"/files")
@app.route("/")
def main():
		return open("main.html","r+").read()
@app.route("/create",methods=["GET","POST"])
def a():
		if (request.method == "POST"):
				c = request.form["name"]
				a = request.form["username"]
				b = request.form["password"]
				if (len(b)>10):
						if (len(a)<4):
								"<script>\nalert('Please enter the valid username');\n</script>\n" + open("create.html","r+").read()
						else:
								r = arw.create(a,b,c)
								if (r == "X"):
										return "<script>\nalert('Account with this username already exist');\n</script>\n" + open("create.html","r+").read()
								else:
										return "<script>\nalert('You are account has been made. Now you can login');\n</script>\n"+open("login.html","r+").read()
				else:
						return "<script>\nalert('Enter the password of more than 10 digits');\n</script>" + open("create.html","r+").read()
		else:
			return open("create.html","r+").read()
@app.route("/login",methods=["GET","POST"])
def b():
		if (request.method == "POST"):
				g = arw.verify(request.form["username"],request.form["password"])
				if (g == "X"):
						return "<script>alert('There is no such account')</script>" + open("login.html","r+").read()
				elif (g=="Xpassword"):
						return "<script>alert('Your password is wrong');</script>" + open("login.html","r+").read()
				else:
						return "<script>localStorage.setItem('username',"+"'"+request.form["username"]+"'"+")</script>"+(open("post.html","r+").read()).replace('cttntbntt',arw.get_content())
		else:
			 return open("login.html","r+").read()
@app.route("/post",methods=["GET","POST"])
def c():
		if (request.method == "POST"):
				if (len(request.form["text"])>5000):
						return "<script>\nalert('Don't exceed the limit of 3000 letters');\n</script>\n"+open("post.html","r+").read()
				elif (len(request.form["text"])<5):
						return "<script>alert('Enter the valid information');</script>"+open("post.html","r+").read()
				else:
						arw.add_post(request.form["username"],request.form["text"])
						return (open("post.html","r+").read()).replace('cttntbntt',arw.get_content())
		else:
				return (open("post.html","r+").read()).replace('cttntbntt',arw.get_content())
@app.route("/refresh",methods=["GET"])
def e():
	return (open("post.html","r+").read()).replace('cttntbntt',arw.get_content())
@app.route("/delete",methods=["GET","POST"])
def d():
		if (request.method== "POST"):
				if(arw.verify(request.form["username"],request.form["password"])=="Y"):
						arw.delete(request.form["username"])
						arw.delete_comment(request.form["username"])
						return open("delete_arg.html","r+").read()
				else:
						return "<script>setTimeout(m,1);\n\nfunction m(){alert('Your password or username is wrong');}</script>" + open("delete.html","r+").read()
		else:
				return open("delete.html","r+").read()
@app.route("/delete_comment",methods=["GET","POST"])
def g():
	if (request.method == "POST"):
		if (request.form["text"] in os.listdir("ACC")):
			arw.delete_comment(request.form["text"])
			return "<script>alert('Your all comments are deleted.');</script>"+ (open("post.html","r+").read()).replace('cttntbntt',arw.get_content())
		else:
			return "ERROR 501"
	else:
		return (open("post.html","r+").read()).replace('cttntbntt',arw.get_content())
@app.route("/help",methods=["GET","POST"])
def f():
	if (request.method == "POST"):
		arw.add_issue(request.form["text"])
		return "<script>alert('Your report has been submitted');</script>"+(open("post.html","r+").read()).replace('cttntbntt',arw.get_content())
	else:
		return open("help.html","r").read()
@app.route("/change_password",methods=["GET","POST"])
def kp():
	if (request.method == "POST"):
		arw.change_password(request.form["new_pss"],request.form["text"])
		return "<script>alert('Your password has been changed');</script>"+(open("post.html","r+").read()).replace('cttntbntt',arw.get_content())
	else:
		return open("post.html","r").read()
if __name__ == '__main__':
	app.run()
