from django import forms

class CommentForm(forms.Form):
    """
    评论表单
    """
    name = forms.CharField(label='昵称', max_length=16, error_messages={
        'required': '请填写您的称呼',
        'max_length': '称呼太长'
    },widget=forms.TextInput(attrs={'class': 'form-control','id': 'exampleInputName','placeholder':'Name'}))

    email = forms.EmailField(label='邮箱', error_messages={
        'required': '请填写您的邮箱',
        'invalid': '邮箱格式不正确'
    },widget=forms.TextInput(attrs={'class': 'form-control','id': 'exampleInputEmail1','type':'email','placeholder':'Email'}))

    content = forms.CharField(label='评论内容', error_messages={
        'required': '请填写您的评论内容',
        'max_length': '评论内容太长'
    },widget=forms.Textarea(attrs={'class': 'form-control','id': 'exampleInputContent','placeholder':'content','rows':'3'}))

class fanyiForm(forms.Form):
    '''
    翻译功能表单
    '''
    fanyi_content = forms.CharField(label='翻译', error_messages={
        'required': '请填写需要翻译的内容',
        'max_length': '填写的内容太长'
    }, widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'exampleInputContent', 'placeholder': '请输入要翻译的文字', 'rows': '1'}))
