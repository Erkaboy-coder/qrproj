import qrcode
from django.shortcuts import render
from django.http import HttpResponse
from io import BytesIO

def index(request):
    if request.method == "POST":
        url = request.POST.get("url")
        if url:
            # QR kod yaratish
            qr = qrcode.QRCode(
                version=1,
                box_size=10,
                border=5
            )
            qr.add_data(url)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")

            # Rasmni BytesIO ga yozish
            buffer = BytesIO()
            img.save(buffer, format="PNG")
            buffer.seek(0)

            # Download response
            response = HttpResponse(buffer, content_type="image/png")
            response['Content-Disposition'] = 'attachment; filename=qr_code.png'
            return response

    # GET so‘rov bo‘lsa, oddiy landing page ko‘rsatish
    return render(request, "index.html")
