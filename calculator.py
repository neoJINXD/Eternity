from flask import Flask, render_template, request
import re
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def frontPage():

  if request.method == 'GET':
    # Show the basic HTML page
    return render_template('index.html')
    
  elif request.method == 'POST':
    if 'io' in request.form:
      # Update HTML page
      expression = request.form.get('calc') + request.form['io']
      return render_template('index.html', test=expression)

    else:
      # Calculate request
      expression = request.form.get('calc')
      result = str(calcEval(expression))
      return render_template('index.html', result=result, expression=expression)
    

def calcEval(equation):
  '''

  calcEval() uses eval(), which is normally a dangerous thing to do.
  To combat this, a list of allowed inputs are made so eval() only gets called if the 
  "equation" given contains only allowed inputs.
  
  '''

  characters = list(equation)

  allowedInputs = ['0','1','2','3','4','5','6','7','8','9',
  '+','-','*','/','^', ' ', '(', ')','.','cos','sin']

  checkSet = set(characters + allowedInputs)

  if len(checkSet) != len(allowedInputs):
    return "Error: Unknown input character."

  else:
    try:
      equation = re.sub('(?<=\d|\))(\()', '*(', equation)
      equation = equation.replace('^','**')
      return (eval(equation))
    except:
      return 'Unknown error occured.'  










class Cal:
    def __init__(self, L):
        self.values = L       

    def dump(self):
        print(self.values)

    def mad(self):
        sum = 0        
        for e in self.values:
            sum += e
        size = len(self.values)
        mean = sum/size
        distance = 0
        for e in self.values:
            distance += (mean-e, e-mean)[e-mean>0]
        result = distance/size
        #print(result)
        return result

    def sd(self):
        sum = 0        
        for e in self.values:
            sum += e
        size = len(self.values)
        mean = sum/size
        distance_square = 0
        for e in self.values:
            distance_square += (e-mean)*(e-mean)
        result = (distance_square/size)**(.5)
        #print(result)
        return result

#t = Cal([1, 4, 7, 2, 6])
#t.sd()