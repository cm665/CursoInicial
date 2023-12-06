capitals = {'USA':'washington DC',
            'India':'new dehli',
            'china':'beijing',
            'russia':'moscow'}

capitals.update({'germany':'berlin'})
capitals.update({'USA':'Las vegas'})
capitals.pop('china')
#capitals.clear()

print(capitals.get('germany'))

print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key,value in capitals.items():
    print(key,value)

