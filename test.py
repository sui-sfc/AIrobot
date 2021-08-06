from opentrons import protocol_api

metadata = {
	'protocolName': 'My Protocol',
	'author': 'Rei Oya <rei_sfc20@keio.jp>',
	'apiLevel': '2.0'
}


def run(protocol: protocol_api.ProtocolContext):

    # Labware
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    container = protocol.load_labware('corning_6_wellplate_16.8ml_flat', '2')
    plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '3')
    tiprack_2 = protocol.load_labware('opentrons_96_tiprack_20ul', '4')
    
    pipetto_300 = protocol.load_instrument(
        'p300_single_gen2', 'left', tip_racks=[tiprack])
    pipetto_20 = protocol.load_instrument(
        'p20_single_gen2', 'right', tip_racks=[tiprack_2])
    
    color = {"red": "A1", "green": "A2", "blue": "A3"}
    grad = []
    grad2 = []
    tmp = ['A{}'.format(i) for i in range(1, 13)]
    grad += tmp
    tmp = ['B{}'.format(i) for i in range(1, 13)]
    grad += tmp
    tmp = ['C{}'.format(i) for i in range(1, 13)]
    grad += tmp
    tmp = ['D{}'.format(i) for i in range(1, 13)]
    grad += tmp
    
    tmp = ['E{}'.format(i) for i in range(1, 13)]
    grad2 += tmp
    tmp = ['F{}'.format(i) for i in range(1, 13)]
    grad2 += tmp
    tmp = ['G{}'.format(i) for i in range(1, 13)]
    grad2 += tmp
    tmp = ['H{}'.format(i) for i in range(1, 13)]
    grad2 += tmp
    
    
    
    wells = dict(
        grad_1 = grad,
        re_grad = reversed(grad),
        grad_2 = grad2,
        re_grad_2 = reversed(grad2),
    )

    #Red
    rest = 0
    n = 1
    pipetto_300.pick_up_tip()
    for well in wells['grad_1']:
        if rest < (96-(n)):
            pipetto_300.aspirate(200, container[color["red"]])
            rest = 200+rest
            pipetto_300.dispense((96-n), plate[well])
            rest -= (96-n)
            n+=1
        elif (48-n) == 0:
            pipetto_300.drop_tip()
            n+=1
            break;
        else:
            pipetto_300.dispense((96-n), plate[well])
            rest -= (96-n)
            n+=1

    #Blue
    pipetto_300.drop_tip()
    pipetto_300.pick_up_tip()
    rest = 0
    t=1
    for well in wells['re_grad_2']:
        if rest < (96-(t)):
            pipetto_300.aspirate(200, container[color["blue"]])
            rest = 200+rest
            pipetto_300.dispense((96-t), plate[well])
            rest -= (96-t)
            t+=1
        elif (48-t) == 0:
            pipetto_300.drop_tip()
            t+=1
            break;
        else:
            pipetto_300.dispense((96-t), plate[well])
            rest -= (96-t)
            t+=1
  
    #Red
    rest = 0
    pipetto_300.drop_tip()
    pipetto_300.pick_up_tip()
    for well in wells['grad_2']:
        if rest < (96-(n)):
            if n != 48:
               pipetto_300.drop_tip()
               pipetto_300.pick_up_tip()
            pipetto_300.aspirate(200, container[color["red"]])
            rest = 200
            pipetto_300.dispense((96-n), plate[well])
            rest -= (96-n)
            n+=1
        elif (96-n) == 0:
            pipetto_300.drop_tip()
            break;
        else:
            pipetto_300.dispense((96-n), plate[well])
            rest -= (96-n)
            n+=1

    #Blue
    rest = 0
    pipetto_300.pick_up_tip()
    for well in wells['re_grad']:
        if rest < (96-(t)):
            if t != 48:
               pipetto_300.drop_tip()
               pipetto_300.pick_up_tip()
            pipetto_300.aspirate(200,container[color["blue"]])
            rest = 200
            pipetto_300.dispense((96-t), plate[well])
            rest -= (96-t)
            t+=1
        elif (96-t) == 0:
            pipetto_300.drop_tip()
            break;
        else:
            pipetto_300.dispense((96-t), plate[well])
            rest -= (96-t)
            t+=1
