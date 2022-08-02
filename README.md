# datascience-test

### Getting started

Begin by creating a development branch, off of the master branch,
which will contain your work.

Basic packages can be installed using the `requirements.txt` file by 
running

```pip install -r requirements```

However, you are welcome to install whatever packages. Please add
any new packages you may use to the `requirements.txt` file so that
we can reproduce your results.

### Generator class

Answers to your questions should be added to the `Generator` class.
For example, if you're creating an answer to **question 1**, you
can add a function to `Generator` called `question_1`.

The data you need can be found in the `data` subclass, within 
`Generator`.

### Results

After creating the functions to a question in `Generator`, add some
code executing that function to the `results.py`.

E.g. `results.py` would contain a function called

```
# Here are my results for question 1
q1_results = generator.question_1()
```

### Submitting

To submit your completed work, make a pull request to the 
datascience-test repository