{"filter":false,"title":"admin.py","tooltip":"/checkout/admin.py","undoManager":{"mark":1,"position":1,"stack":[[{"start":{"row":2,"column":0},"end":{"row":2,"column":28},"action":"remove","lines":["# Register your models here."],"id":2}],[{"start":{"row":2,"column":0},"end":{"row":13,"column":38},"action":"insert","lines":["from .models import Order, OrderLineItem","","","class OrderLineAdminInline(admin.TabularInline):","    model = OrderLineItem","","","class OrderAdmin(admin.ModelAdmin):","    inlines = (OrderLineAdminInline, )","","","admin.site.register(Order, OrderAdmin)"],"id":3}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":14,"column":0},"end":{"row":14,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1567814323847,"hash":"0162eb6de6d13224e978a3003d51c65bf9f2f33a"}