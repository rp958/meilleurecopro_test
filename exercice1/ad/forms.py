from django import forms


class UrlForm(forms.Form):
    url = forms.URLField(label="URL", required=True)


class QuantilesForm(forms.Form):
    dept_code = forms.CharField(label="Departement", required=False)
    city = forms.CharField(label="Ville", required=False)
    zip_code = forms.IntegerField(label="Code postal", required=False)
