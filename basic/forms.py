from django import forms

class TestForm(forms.Form):
    CHOICES=[('0','Strongly Disagree'),
         ('1','Disagree'),
         ('2','Slightly Disagree'),
         ('3','Neither Agree nor Disagree'),
         ('4','Slightly Agree'),
          ('5','Agree'),
         ('6','Strongly Agree'),]

    ques=[
    'I put effort into work because it has personal significance to me.',
    'I care about having a great reputation at work.',
    'I care about having challenges that help me to develop new skills.',
    'I like to complete tasks way in advance to feel comfortable.',
    'I am motivated by recognition at work.',
    'Its important to me to work in an environment where no one day is the same.',
    'Its important to me to keep up to date with the newest research of my field.',
    'It is important that I am able to take on different kinds of tasks at work.',
    'I want to support others in their learning.',
    'Being publicly praised for my work would feel uncomfortable for me.']
    Q1 = forms.ChoiceField(label=ques[0],choices=CHOICES, widget=forms.RadioSelect)
    Q2 = forms.ChoiceField(label=ques[1],choices=CHOICES, widget=forms.RadioSelect)
    Q3 = forms.ChoiceField(label=ques[2],choices=CHOICES, widget=forms.RadioSelect)
    Q4 = forms.ChoiceField(label=ques[3],choices=CHOICES, widget=forms.RadioSelect)
    Q5 = forms.ChoiceField(label=ques[4],choices=CHOICES, widget=forms.RadioSelect)
    Q6 = forms.ChoiceField(label=ques[5],choices=CHOICES, widget=forms.RadioSelect)
    Q7 = forms.ChoiceField(label=ques[6],choices=CHOICES, widget=forms.RadioSelect)
    Q8 = forms.ChoiceField(label=ques[7],choices=CHOICES, widget=forms.RadioSelect)
    Q9 = forms.ChoiceField(label=ques[8],choices=CHOICES, widget=forms.RadioSelect)
    Q10 = forms.ChoiceField(label=ques[9],choices=CHOICES, widget=forms.RadioSelect)

