from flask import Flask,render_template,request,redirect,url_for
import base 
import rsaAlgo as rsa

app=Flask(__name__)

@app.route('/')
def index():
   db=base.connecter()
   curseur=db.cursor()
   curseur.execute("SELECT * FROM etudiant")
   tableEtudiant = curseur.fetchall()
   db.commit()

   return render_template('index.html',t=tableEtudiant)


# @app.route('/save_etudiant',methods=['POST'])
# def save_etudiant():
#    if request.method=='POST':
#       mat=request.form['Matricule']
#       nom=request.form['Nom']
#       postNom=request.form['PostNom']
      
      
#       db=base.connecter()
#       curseur=db.cursor()
    
#       sql=" INSERT INTO Etudiant(Matricule,Nom,PostNom) VALUES(%s,%s,%s)"

#       valeurs=(mat,nom,postNom)
#       curseur.execute(sql,valeurs)
#       tableEtudiant=curseur.fetchall()
#       db.commit()
#       return redirect(url_for('index'))

@app.route('/save_etudiant', methods=['POST', 'GET'])
def save_etudiant():
   if request.method == 'POST':
      mat = request.form['Matricule']
      nom = request.form['Nom']
      
      rsaNom = rsa.rsa(nom, 33,3)
      postNom = request.form['PostNom']
      rsaPostNom = rsa.rsa(postNom, 33, 3)
      date = request.form['date']

      db = base.connecter()
      curseur = db.cursor()

      # sql = "INSERT INTO Etudiant(Matricule, Nom, PostNom) VALUES (%s, %s, %s)"
      sql ="INSERT INTO etudiant(matricule, nom, postnom, dateNaissance) VALUES (%s,%s,%s,%s)"

      valeurs = (mat, str(rsaNom), str(rsaPostNom), date,)
      curseur.execute(sql, valeurs)
      db.commit()

      curseur.close()
      db.close()

      return redirect(url_for('index'))
   return render_template('formulaire.html')


@app.route('/fomulaire')
def std():
   return render_template('formulaire.html')


@app.route('/Delete/<Matricule>')
def delete_etudiant(Matricule):
   db=base.connecter()
   curseur=db.cursor()
   sql="DELETE FROM Etudiant WHERE MATRICULE=%s"
   val=(Matricule,)
   curseur.execute(sql,val)
   db.commit()
   #flash('Etudiant est suprime')
   return redirect(url_for('index'))
   
@app.route('/ouvrir_update/<Matricule>/')
def lancer(Matricule):
   sql="SELECT* FROM etudiant WHERE Matricule=%s"
   db=base.connecter()
   curseur=db.cursor()
 
   curseur.execute(sql, (Matricule,))
   data=curseur.fetchall()
   return render_template('modifier.html',data=data)

@app.route('/update/<Matricule>/', methods=['POST'])
def update(Matricule): 
   if request.method=='POST':
      nom=request.form['Nom']
      postnom=request.form['PostNom']

    
      sql="UPDATE etudiant SET nom=%s,postnom=%s WHERE Matricule=%s"
     
      val=(nom,postnom,Matricule,)
      # print("hello")
      db=base.connecter()
      curseur=db.cursor()
      curseur.execute(sql,val)
      db.commit()
      db.close()
      return redirect(url_for('index'))
     
      
   
  

# @app.route('/')
# def index():
#    return render_template('index.html')



# @app.route('/etudiant')
# def etudiants():
#    listeEtudiant=['Mado','Cedrick', 'David','Laety']
#    return render_template('etudiant.html',donnee =listeEtudiant )


if __name__=='__main__':
   app.run(port=4000)
   app.run(debug = True)