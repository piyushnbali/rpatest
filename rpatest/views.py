from django.shortcuts import render, redirect
import rsa
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def test(request):
    if request.method == 'GET':
        publicKey = rsa.PublicKey(60092367176717177236697572105348316055238458425410182886498711079787218116951,65537)
        text = request.GET['text'].encode('utf8')
        crypto = rsa.encrypt(text,publicKey)
        context ={"text":crypto}
        return render(request,'test/test.html',context)

@csrf_exempt
def testde(request):
    if request.method == 'POST':
        print(request.POST)
        publicKey = rsa.PrivateKey(60092367176717177236697572105348316055238458425410182886498711079787218116951, 65537, 50680155005439855657517863274284940123977021759276884790621110551029383500097, 74178846850887288189740490132250073456309, 810101123538810903977891689469410139)
        text = request.POST['text']
        print(type(text))
        crypto = rsa.decrypt(text,publicKey)
        context ={"text":crypto}
        return render(request,'test/test.html',context)