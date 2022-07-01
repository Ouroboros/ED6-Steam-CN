import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import E0312_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('E0312_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Event'
    header.mapModel       = 'E0312.x'
    header.mapIndex       = 1
    header.bgm            = 116
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT21/E0312._SN', 'ED6_DT21/E0312_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x4F28
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000000,
            dword_08        = 0x00001770,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 45,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 0,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10001 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
    ]

# id: 0x10002 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0xA8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0xA8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0xA8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xA8
@scena.Code('PreInit')
def PreInit():
    EventBegin(0x00)
    FadeOut(300, 0, 100)
    OP_22(0x009D, 0x00, 0x64)
    SetChrName('CAPEL')
    SetMessageWindowPos(250, 78, 36, 12)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1SThe Orbal Calculator\n',
            'CAPEL SYSTEM Ver.7.0\n',
            'Copyright(C) Z.C.F. 1197-1202\n',
            'MODE:Information Retrieval\n',
            '#200W　#20W\n',
            'MEMORY_CHECK#100W..........#20WＯＫ!\n',
            '#200W　#20W\n',
            '#1S已连接到数据库。\n',
            '请选择要搜索的内容。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1A4(): pass

    label('loc_1A4')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4F0C',
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_CC(0x00, 0x00, 0x0037, 0x0050, 0x01)
    OP_CC(0x01, 0x00, '【中央工房关联】')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 3, 0x1E0B)),
            Expr.Return,
        ),
        'loc_1ED',
    )

    OP_CC(0x01, 0x00, '【数据水晶】')

    def _loc_1ED(): pass

    label('loc_1ED')

    OP_CC(0x02, 0x00)
    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_204'),
        (0x00000001, 'loc_15A7'),
        (-1, 'loc_4EFC'),
    )

    def _loc_204(): pass

    label('loc_204')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_15A7',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        1,
        55,
        153,
        1,
        (
            TXT(0x00, '【设立·沿革】\n'),
            TXT(0x01, '【技术一览】\n'),
            TXT(0x02, '【关连信息搜索】　　\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_26D'),
        (0x00000001, 'loc_8B8'),
        (0x00000002, 'loc_12C6'),
        (-1, 'loc_1597'),
    )

    def _loc_26D(): pass

    label('loc_26D')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S【Ｓ１１５４】（Ｓ…七耀历）\n',
            'Ｃ·爱普斯泰恩博士于列曼自治州去世。\n',
            '【Ｓ１１５５】\n',
            'Ａ·拉赛尔博士回到利贝尔王国。\n',
            '回国后提倡普及导力器技术，\n',
            '但没有得到世人的认可和支持。\n',
            '【Ｓ１１５７】\n',
            '拉赛尔博士带领蔡斯的钟表工匠普及导力器。\n',
            '同年，『蔡斯技术工房』（即之后的中央工房）设立。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S【Ｓ１１６０】\n',
            '埃德佳Ⅲ世在视察蔡斯技术工房后提供巨额资金建设工\n',
            '房。拉赛尔博士出任首任工房长。【Ｓ１１６２】\n',
            '埃德佳Ⅲ世去世。艾莉茜雅Ⅱ世即位。\n',
            '【Ｓ１１６４】\n',
            '『伦格兰德大桥』落成。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S【Ｓ１１６８】\n',
            '首部导力飞船『加拉托拉巴号』诞生。\n',
            '（经过３９次飞行实验失败后的产物）\n',
            '【Ｓ１１７３】\n',
            '蔡斯技术工房开始对共和国乌尔努社和帝国莱恩福尔特\n',
            '社输出导力器技术。工房改名为『中央工房』。\n',
            '【Ｓ１１７５】\n',
            '飞船公社设立。定期船『林德号』开始服役。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S【Ｓ１１７７】\n',
            '定期船『赛希莉亚号』开始服役。\n',
            '【Ｓ１１７８】\n',
            '移动工房船『莱普尼兹号』竣工。\n',
            '【Ｓ１１８０】\n',
            '中央工房搬迁（即现在的建筑物）。\n',
            '开掘卡鲁迪亚平原丘陵的一角，地下工房建成。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S【Ｓ１１８２】\n',
            '拉赛尔工房长退休。\n',
            '玛多克技术主任出任第二任工房长。\n',
            '【Ｓ１１８５】\n',
            '自然科学和医学研究部门设立。\n',
            '【Ｓ１１８７】\n',
            '客船『埃迪鲁那号』在卡尔瓦德领海沉没。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S【Ｓ１１９０】\n',
            '与爱普斯泰恩财团合作，\n',
            '发表了『导力网络』的构想。\n',
            '【Ｓ１１９２】\n',
            '『百日战役』爆发。\n',
            '中央工房被埃雷波尼亚帝国接管。\n',
            '拉赛尔博士在雷斯顿要塞开发出警备飞艇，\n',
            '并将其用于反攻作战中，取得了显赫的战功，\n',
            '从此警备飞艇作为王国军的主力兵器被广泛使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S【Ｓ１１９３】\n',
            '利贝尔王国和埃雷波尼亚帝国缔结和平条约。\n',
            '战后，王国再次向帝国输出导力器。\n',
            '【Ｓ１１９７】\n',
            '导力演算器『卡佩尔』Ver.1完成。\n',
            '【Ｓ１１９９】\n',
            '高速巡洋舰『埃尔赛尤』开发工程开始。\n',
            '【Ｓ１２０２】\n',
            '高速巡洋舰『埃尔赛尤』竣工，进入试飞阶段。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15A4')

    def _loc_8B8(): pass

    label('loc_8B8')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_12B6',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0001)

    Menu(
        2,
        55,
        259,
        1,
        (
            TXT(0x00, '【导力器】\n'),
            TXT(0x01, '【结晶回路】\n'),
            TXT(0x02, '【七耀石】\n'),
            TXT(0x03, '【导力飞船】\n'),
            TXT(0x04, '【导力兵器】\n'),
            TXT(0x05, '【战术导力器】\n'),
            TXT(0x06, '【新型战术导力器】\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_962'),
        (0x00000001, 'loc_AE5'),
        (0x00000002, 'loc_BAF'),
        (0x00000003, 'loc_CC7'),
        (0x00000004, 'loc_DFC'),
        (0x00000005, 'loc_F6E'),
        (0x00000006, 'loc_10FD'),
        (-1, 'loc_12A6'),
    )

    def _loc_962(): pass

    label('loc_962')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S项目：导力器（Orbment）\n',
            '在半世纪前由Ｃ·爱普斯泰恩博士所发明，是能从七耀\n',
            '石中提取导力，从而引发各种各样现象的机械装置的总\n',
            '称。导力器内部的构造和齿轮的运动，使加工七耀石而\n',
            '成的结晶回路相互干涉，可以引发丰富多彩的现象。导\n',
            '力器的实用性，除了能产生丰富现象以外，还在于拥有\n',
            '『经过一段时间内部的导力可以自然恢复』这种特异的\n',
            '便利性。另外，经济效率也要远远地领先于各种外燃、\n',
            '内燃机。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12B3')

    def _loc_AE5(): pass

    label('loc_AE5')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S项目：结晶回路（Quartz）\n',
            '将七耀石的碎片（耀晶片，Sepith）精制、加工而成的\n',
            '具有结晶构造的回路。作为能量源的同时，本身还是引\n',
            '起各种各样现象的装置。但结晶回路必须安装在导力器\n',
            '内才可以发挥作用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12B3')

    def _loc_BAF(): pass

    label('loc_BAF')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S项目：七耀石（Septium）\n',
            '是在大陆全土分布的７种贵重矿石的总称。因被人们称\n',
            '为『古代的宝石』、『神秘的象征』而变得珍重。近代\n',
            '一种将体积过小不能成为宝石的碎片（耀晶片）精制加\n',
            '工制作出结晶回路的技术被发明出来，因此导致七耀石\n',
            '资源的重要性在大陆诸国之间一夜之间变得十分重要。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12B3')

    def _loc_CC7(): pass

    label('loc_CC7')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S项目：导力飞船\n',
            '导力飞船可以称得上是导力技术精华凝聚而成的结晶。\n',
            '集合了用于重力制御的大型飞翔引擎和供给大量能量的\n',
            '导力引擎两大技术，使得如此大的飞船在空中飞行成为\n',
            '可能。\n',
            '为了实现高效率的导力传送和十分复杂的船体控制，最\n',
            '新的飞船大多搭载了高性能的导力演算器。２０亚矩以\n',
            '下的小型飞船又被称为『飞艇』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12B3')

    def _loc_DFC(): pass

    label('loc_DFC')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S项目：导力兵器\n',
            '即以导力枪、导力炮作为代表，使用导力技术的兵器体\n',
            '系。现在已成为大多数国家军队的主力装备。\n',
            '导力枪枪管内具有能将能量按照螺旋线聚集并高速射出\n',
            '豆粒大小的金属子弹的构造，与发射火药的枪相比，填\n',
            '弹量大幅增加，而且还能够调节枪的威力。\n',
            '导力炮则可以发射封装了能量的炮弹（导力弹）并产生\n',
            '爆炸，与发射火药的炮相比，其后坐力小，而且也可以\n',
            '自由调节威力大小。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12B3')

    def _loc_F6E(): pass

    label('loc_F6E')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S项目：战术导力器\n',
            '可以发动导力魔法的导力器。大小和怀表差不多，内部\n',
            '构造则相当精致优雅。\n',
            '战术导力器具有安装结晶回路后能够提高持有者能力的\n',
            '设计，使内部结晶回路与持有者达到同步，引发出『共\n',
            '鸣现象』，以代替传统释放魔法所需的复杂的齿轮和驱\n',
            '动装置，使持有者能够发动各种导力魔法。\n',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S　\n',
            '而且，根据复数结晶回路属性和势能的组合不同，持有\n',
            '者能够使用的导力魔法也会发生变化，具有相当的灵活\n',
            '性。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12B3')

    def _loc_10FD(): pass

    label('loc_10FD')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S项目：新型战术导力器\n',
            '作为战术导力器的开发者，爱普斯泰恩财团对过去的型号进\n',
            '行大幅改良，并且成功投入实用的新规格战术导力器。和过\n',
            '去只有六个结晶回路插槽的旧型号相比，这种新型号则具备\n',
            '了七个结晶回路插槽，可以实现更为灵活的结晶回路组合。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S　\n',
            '新型号不仅使可以使用的魔法变得多元化，而且使其威力也\n',
            '得到了飞跃性的提升。但是，由于新型号和过去型号的基本\n',
            '构造有很大的不同，新型战术导力器也有着无法互换结晶回\n',
            '路的缺陷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12B3')

    def _loc_12A6(): pass

    label('loc_12A6')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_12B3')

    def _loc_12B3(): pass

    label('loc_12B3')

    Jump('loc_8B8')

    def _loc_12B6(): pass

    label('loc_12B6')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0002)

    Jump('loc_15A4')

    def _loc_12C6(): pass

    label('loc_12C6')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1587',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        2,
        55,
        255,
        1,
        (
            TXT(0x00, '【内燃机】\n'),
            TXT(0x01, '【汽油】\n'),
            TXT(0x02, '【运输车】\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_131D'),
        (0x00000001, 'loc_13EE'),
        (0x00000002, 'loc_149A'),
        (-1, 'loc_1577'),
    )

    def _loc_131D(): pass

    label('loc_131D')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S项目：内燃机\n',
            '在机关装置内燃烧燃料以获得能量的动力源。与导力机\n',
            '关相比经济效率低下，而且还会产生噪音、废气等各种\n',
            '问题，因此已经停止开发和生产。\n',
            '\n',
            '『内燃机部件』\n',
            '库存量：１台\n',
            '管理责任人：格斯塔夫维修长',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1584')

    def _loc_13EE(): pass

    label('loc_13EE')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S项目：汽油\n',
            '将天然产生的液态碳氢化合物（石油）分馏、精制而成\n',
            '的液体。常作为内燃引擎设备的燃料以及工业生产的溶\n',
            '剂使用。\n',
            '\n',
            '共和国产汽油\n',
            '储备量：无（已向共和国订购）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1584')

    def _loc_149A(): pass

    label('loc_149A')

    OP_28(0x0029, 0x01, 0x8000)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S项目：运输车\n',
            '使用导力引擎驱动的各种车辆的总称。因为乘坐的舒适\n',
            '度较差，速度也很慢，所以基本不用于客运方面，而主\n',
            '要用来进行中短距离的货物运输。\n',
            '\n',
            '『运输车用驱动导力器』\n',
            '库存量：不明\n',
            '保管地点：地下工场搬入口',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1584')

    def _loc_1577(): pass

    label('loc_1577')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1584')

    def _loc_1584(): pass

    label('loc_1584')

    Jump('loc_12C6')

    def _loc_1587(): pass

    label('loc_1587')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0002)

    Jump('loc_15A4')

    def _loc_1597(): pass

    label('loc_1597')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_15A4')

    def _loc_15A4(): pass

    label('loc_15A4')

    Jump('loc_204')

    def _loc_15A7(): pass

    label('loc_15A7')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4EEC',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_CC(0x00, 0x01, 0x0037, 0x0099, 0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0450, 0, 0x2280)),
            Expr.Return,
        ),
        'loc_15EE',
    )

    OP_CC(0x01, 0x01, '＃０　　阅览完毕')

    Jump('loc_1620')

    def _loc_15EE(): pass

    label('loc_15EE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_160E',
    )

    OP_CC(0x01, 0x01, '＃０　　分析完成！')

    Jump('loc_1620')

    def _loc_160E(): pass

    label('loc_160E')

    OP_CC(0x01, 0x01, '＃０　　分析中')

    def _loc_1620(): pass

    label('loc_1620')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 7, 0x1E07)),
            (Expr.Eval, "OP_40(0x03FE, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_168D',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Or2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0450, 1, 0x2281)),
            Expr.Return,
        ),
        'loc_165B',
    )

    OP_CC(0x01, 0x01, '＃１　　阅览完毕')

    Jump('loc_168D')

    def _loc_165B(): pass

    label('loc_165B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_167B',
    )

    OP_CC(0x01, 0x01, '＃１　　分析完成！')

    Jump('loc_168D')

    def _loc_167B(): pass

    label('loc_167B')

    OP_CC(0x01, 0x01, '＃１　　分析中')

    def _loc_168D(): pass

    label('loc_168D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 0, 0x1E08)),
            (Expr.Eval, "OP_40(0x03FF, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_16FA',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x2),
            Expr.Or2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0450, 2, 0x2282)),
            Expr.Return,
        ),
        'loc_16C8',
    )

    OP_CC(0x01, 0x01, '＃２　　阅览完毕')

    Jump('loc_16FA')

    def _loc_16C8(): pass

    label('loc_16C8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_16E8',
    )

    OP_CC(0x01, 0x01, '＃２　　分析完成！')

    Jump('loc_16FA')

    def _loc_16E8(): pass

    label('loc_16E8')

    OP_CC(0x01, 0x01, '＃２　　分析中')

    def _loc_16FA(): pass

    label('loc_16FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 1, 0x1E09)),
            (Expr.Eval, "OP_40(0x0400, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1767',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x4),
            Expr.Or2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0450, 3, 0x2283)),
            Expr.Return,
        ),
        'loc_1735',
    )

    OP_CC(0x01, 0x01, '＃３　　阅览完毕')

    Jump('loc_1767')

    def _loc_1735(): pass

    label('loc_1735')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_1755',
    )

    OP_CC(0x01, 0x01, '＃３　　分析完成！')

    Jump('loc_1767')

    def _loc_1755(): pass

    label('loc_1755')

    OP_CC(0x01, 0x01, '＃３　　分析中')

    def _loc_1767(): pass

    label('loc_1767')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 6, 0x1E0E)),
            (Expr.Eval, "OP_40(0x0401, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_17D4',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x8),
            Expr.Or2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0450, 4, 0x2284)),
            Expr.Return,
        ),
        'loc_17A2',
    )

    OP_CC(0x01, 0x01, '＃４　　阅览完毕')

    Jump('loc_17D4')

    def _loc_17A2(): pass

    label('loc_17A2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 0, 0x2218)),
            Expr.Return,
        ),
        'loc_17C2',
    )

    OP_CC(0x01, 0x01, '＃４　　分析完成！')

    Jump('loc_17D4')

    def _loc_17C2(): pass

    label('loc_17C2')

    OP_CC(0x01, 0x01, '＃４　　分析中')

    def _loc_17D4(): pass

    label('loc_17D4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 7, 0x1E0F)),
            (Expr.Eval, "OP_40(0x0402, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1841',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x10),
            Expr.Or2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0450, 5, 0x2285)),
            Expr.Return,
        ),
        'loc_180F',
    )

    OP_CC(0x01, 0x01, '＃５　　阅览完毕')

    Jump('loc_1841')

    def _loc_180F(): pass

    label('loc_180F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 0, 0x2218)),
            Expr.Return,
        ),
        'loc_182F',
    )

    OP_CC(0x01, 0x01, '＃５　　分析完成！')

    Jump('loc_1841')

    def _loc_182F(): pass

    label('loc_182F')

    OP_CC(0x01, 0x01, '＃５　　分析中')

    def _loc_1841(): pass

    label('loc_1841')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 0, 0x1E10)),
            (Expr.Eval, "OP_40(0x0403, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_18AE',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x20),
            Expr.Or2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0450, 6, 0x2286)),
            Expr.Return,
        ),
        'loc_187C',
    )

    OP_CC(0x01, 0x01, '＃６　　阅览完毕')

    Jump('loc_18AE')

    def _loc_187C(): pass

    label('loc_187C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 0, 0x2218)),
            Expr.Return,
        ),
        'loc_189C',
    )

    OP_CC(0x01, 0x01, '＃６　　分析完成！')

    Jump('loc_18AE')

    def _loc_189C(): pass

    label('loc_189C')

    OP_CC(0x01, 0x01, '＃６　　分析中')

    def _loc_18AE(): pass

    label('loc_18AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 2, 0x1E1A)),
            (Expr.Eval, "OP_40(0x0404, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_191B',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x40),
            Expr.Or2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0450, 7, 0x2287)),
            Expr.Return,
        ),
        'loc_18E9',
    )

    OP_CC(0x01, 0x01, '＃７　　阅览完毕')

    Jump('loc_191B')

    def _loc_18E9(): pass

    label('loc_18E9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 0, 0x2218)),
            Expr.Return,
        ),
        'loc_1909',
    )

    OP_CC(0x01, 0x01, '＃７　　分析完成！')

    Jump('loc_191B')

    def _loc_1909(): pass

    label('loc_1909')

    OP_CC(0x01, 0x01, '＃７　　分析中')

    def _loc_191B(): pass

    label('loc_191B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 3, 0x1E1B)),
            (Expr.Eval, "OP_40(0x0405, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1988',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x80),
            Expr.Or2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0451, 0, 0x2288)),
            Expr.Return,
        ),
        'loc_1956',
    )

    OP_CC(0x01, 0x01, '＃８　　阅览完毕')

    Jump('loc_1988')

    def _loc_1956(): pass

    label('loc_1956')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 6, 0x221E)),
            Expr.Return,
        ),
        'loc_1976',
    )

    OP_CC(0x01, 0x01, '＃８　　分析完成！')

    Jump('loc_1988')

    def _loc_1976(): pass

    label('loc_1976')

    OP_CC(0x01, 0x01, '＃８　　分析中')

    def _loc_1988(): pass

    label('loc_1988')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 4, 0x1E1C)),
            (Expr.Eval, "OP_40(0x0406, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_19F5',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x100),
            Expr.Or2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0451, 1, 0x2289)),
            Expr.Return,
        ),
        'loc_19C3',
    )

    OP_CC(0x01, 0x01, '＃９　　阅览完毕')

    Jump('loc_19F5')

    def _loc_19C3(): pass

    label('loc_19C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 6, 0x221E)),
            Expr.Return,
        ),
        'loc_19E3',
    )

    OP_CC(0x01, 0x01, '＃９　　分析完成！')

    Jump('loc_19F5')

    def _loc_19E3(): pass

    label('loc_19E3')

    OP_CC(0x01, 0x01, '＃９　　分析中')

    def _loc_19F5(): pass

    label('loc_19F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C4, 1, 0x1E21)),
            (Expr.Eval, "OP_40(0x0407, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1A62',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x200),
            Expr.Or2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0451, 2, 0x228A)),
            Expr.Return,
        ),
        'loc_1A30',
    )

    OP_CC(0x01, 0x01, '＃１０　阅览完毕')

    Jump('loc_1A62')

    def _loc_1A30(): pass

    label('loc_1A30')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 6, 0x221E)),
            Expr.Return,
        ),
        'loc_1A50',
    )

    OP_CC(0x01, 0x01, '＃１０　分析完成！')

    Jump('loc_1A62')

    def _loc_1A50(): pass

    label('loc_1A50')

    OP_CC(0x01, 0x01, '＃１０　分析中')

    def _loc_1A62(): pass

    label('loc_1A62')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C4, 2, 0x1E22)),
            (Expr.Eval, "OP_40(0x0408, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1ACF',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x400),
            Expr.Or2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0451, 3, 0x228B)),
            Expr.Return,
        ),
        'loc_1A9D',
    )

    OP_CC(0x01, 0x01, '＃１１　阅览完毕')

    Jump('loc_1ACF')

    def _loc_1A9D(): pass

    label('loc_1A9D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 6, 0x221E)),
            Expr.Return,
        ),
        'loc_1ABD',
    )

    OP_CC(0x01, 0x01, '＃１１　分析完成！')

    Jump('loc_1ACF')

    def _loc_1ABD(): pass

    label('loc_1ABD')

    OP_CC(0x01, 0x01, '＃１１　分析中')

    def _loc_1ACF(): pass

    label('loc_1ACF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C4, 3, 0x1E23)),
            (Expr.Eval, "OP_40(0x0409, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1B3C',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x800),
            Expr.Or2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x044E, 6, 0x2276)),
            Expr.Return,
        ),
        'loc_1B0A',
    )

    OP_CC(0x01, 0x01, '＃１２　阅览完毕')

    Jump('loc_1B3C')

    def _loc_1B0A(): pass

    label('loc_1B0A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Return,
        ),
        'loc_1B2A',
    )

    OP_CC(0x01, 0x01, '＃１２　分析完成！')

    Jump('loc_1B3C')

    def _loc_1B2A(): pass

    label('loc_1B2A')

    OP_CC(0x01, 0x01, '＃１２　分析中')

    def _loc_1B3C(): pass

    label('loc_1B3C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C6, 2, 0x1E32)),
            (Expr.Eval, "OP_40(0x0412, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1BA9',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1000),
            Expr.Or2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x044E, 7, 0x2277)),
            Expr.Return,
        ),
        'loc_1B77',
    )

    OP_CC(0x01, 0x01, '＃１３　阅览完毕')

    Jump('loc_1BA9')

    def _loc_1B77(): pass

    label('loc_1B77')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Return,
        ),
        'loc_1B97',
    )

    OP_CC(0x01, 0x01, '＃１３　分析完成！')

    Jump('loc_1BA9')

    def _loc_1B97(): pass

    label('loc_1B97')

    OP_CC(0x01, 0x01, '＃１３　分析中')

    def _loc_1BA9(): pass

    label('loc_1BA9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C6, 3, 0x1E33)),
            (Expr.Eval, "OP_40(0x0413, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1C16',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x2000),
            Expr.Or2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x044F, 0, 0x2278)),
            Expr.Return,
        ),
        'loc_1BE4',
    )

    OP_CC(0x01, 0x01, '＃１４　阅览完毕')

    Jump('loc_1C16')

    def _loc_1BE4(): pass

    label('loc_1BE4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Return,
        ),
        'loc_1C04',
    )

    OP_CC(0x01, 0x01, '＃１４　分析完成！')

    Jump('loc_1C16')

    def _loc_1C04(): pass

    label('loc_1C04')

    OP_CC(0x01, 0x01, '＃１４　分析中')

    def _loc_1C16(): pass

    label('loc_1C16')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C6, 4, 0x1E34)),
            (Expr.Eval, "OP_40(0x0414, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1C83',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x4000),
            Expr.Or2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x044F, 1, 0x2279)),
            Expr.Return,
        ),
        'loc_1C51',
    )

    OP_CC(0x01, 0x01, '＃１５　阅览完毕')

    Jump('loc_1C83')

    def _loc_1C51(): pass

    label('loc_1C51')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Return,
        ),
        'loc_1C71',
    )

    OP_CC(0x01, 0x01, '＃１５　分析完成！')

    Jump('loc_1C83')

    def _loc_1C71(): pass

    label('loc_1C71')

    OP_CC(0x01, 0x01, '＃１５　分析中')

    def _loc_1C83(): pass

    label('loc_1C83')

    OP_CC(0x02, 0x01)
    MenuEnd(0x0000)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1CA3',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1D0D')

    def _loc_1CA3(): pass

    label('loc_1CA3')

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1CAD(): pass

    label('loc_1CAD')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1D0D',
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1CC6',
    )

    Jump('loc_1D0D')

    def _loc_1CC6(): pass

    label('loc_1CC6')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1D00',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_1CF3',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x2),
            Expr.Div2,
            Expr.Return,
        ),
    )

    Jump('loc_1D00')

    def _loc_1CF3(): pass

    label('loc_1CF3')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x2),
            Expr.Div2,
            Expr.Return,
        ),
    )

    Jump('loc_1CC6')

    def _loc_1D00(): pass

    label('loc_1D00')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_1CAD')

    def _loc_1D0D(): pass

    label('loc_1D0D')

    Switch(
        (
            (Expr.PushReg, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_1D56'),
        (0x00000001, 'loc_2139'),
        (0x00000002, 'loc_23E8'),
        (0x00000003, 'loc_269B'),
        (0x00000004, 'loc_2A30'),
        (0x00000005, 'loc_2D93'),
        (0x00000006, 'loc_30B3'),
        (0x00000007, 'loc_3358'),
        (0x00000008, 'loc_364B'),
        (0x00000009, 'loc_393E'),
        (0x0000000A, 'loc_3C9C'),
        (0x0000000B, 'loc_408E'),
        (0x0000000C, 'loc_4499'),
        (0x0000000D, 'loc_46C0'),
        (0x0000000E, 'loc_491A'),
        (0x0000000F, 'loc_4B93'),
        (-1, 'loc_4EDC'),
    )

    def _loc_1D56(): pass

    label('loc_1D56')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_1F4A',
    )

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S『关于封印机构（１／４）』\n',
            '　\n',
            '──我的名字是\n',
            '赛雷斯托·Ｄ·奥赛雷丝。\n',
            '是『封印机构』的设立者，\n',
            '『封印计划』的实行负责人。\n',
            '　\n',
            '因塔的『第二结界』发动\n',
            '而被封印在异次元之中的『环』\n',
            '在后世将会苏醒，\n',
            '为此我们决定留下一部分信息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S读到这些信息的人，\n',
            '如果打算阻止『环』的复活的话，\n',
            '请以此作参考，那将是一大幸事。\n',
            '但如果你是期盼『环』复活的人，\n',
            '我请求你重新考虑一下。\n',
            '　\n',
            '『环』的力量过于强大，\n',
            '并非人类所能操控的存在。\n',
            '当人们接纳了『环』之时，\n',
            '也许就是我们造访炼狱之日。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x2280)

    Jump('loc_2135')

    def _loc_1F4A(): pass

    label('loc_1F4A')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S『关于封印机构（１／４）』\n',
            '　\n',
            '──我的名字是\n',
            '赛雷斯托·Ｄ·奥赛雷丝。\n',
            '是『封■■■』■设立■■\n',
            '■封■计■■■■■负责人。\n',
            '丂\n',
            '■塔■■■二结■■发■\n',
            '而■封■■异次■■■■■环』\n',
            '■■世■会苏■■\n',
            '■■■■■定留■■部分信■■',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S读■这■■息的■，\n',
            '■■■■■■『环■■复活的■■\n',
            '■以此作■■，那将是■大幸■。\n',
            '■■■你是期■■环』■■的■，\n',
            '我请求■■新考虑■■■■■。\n',
            '　\n',
            '『■』■力量■■强大■\n',
            '■■人类■能■■的■在。\n',
            '当人■接■了『环■之■■\n',
            '也■是■们造■■狱■日。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2135(): pass

    label('loc_2135')

    CloseMessageWindow()

    Jump('loc_4EE9')

    def _loc_2139(): pass

    label('loc_2139')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_2295',
    )

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S『关于封印机构（２／４）』\n',
            '　\n',
            '本机构，是为了通过消除『环』\n',
            '的干涉，从而保护人类的存在\n',
            '而设立的。\n',
            '　\n',
            '在此想事先提醒大家的是，\n',
            '『环』本身并不具备\n',
            '支配人类的意志。\n',
            '一切都起因于我们对\n',
            '『环』的过分依赖以及自身的软弱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S这伟大的至宝对于不成熟的灵魂\n',
            '而言，力量实在过于强大了。\n',
            '因此，女神的慈悲和全能\n',
            '丝毫也不会动摇。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x2281)

    Jump('loc_23E4')

    def _loc_2295(): pass

    label('loc_2295')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S『关于封印机构（２／４）』\n',
            '　\n',
            '本■■，是■了■■■除『■』\n',
            '的干■，■而■■人■的存■\n',
            '■■立的。\n',
            '　\n',
            '在此想■■■■大■的是，\n',
            '『环』■身■■具■\n',
            '■配■■的■志。\n',
            '一■■起■■■们对\n',
            '『■■的过■■赖■及自■■■弱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S■■大的至宝■■■■■■■■\n',
            '而■■■量实■■■■大了。\n',
            '因此■■神的慈■■全能\n',
            '丝■■■■■■。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_23E4(): pass

    label('loc_23E4')

    CloseMessageWindow()

    Jump('loc_4EE9')

    def _loc_23E8(): pass

    label('loc_23E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_2547',
    )

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S『关于封印机构（３／４）』\n',
            '　\n',
            '封印机构的目的，\n',
            '完全脱离了所谓\n',
            '民主主义的理念。\n',
            '　\n',
            '即使在我们之中，也存在着不少\n',
            '认为应当有效地利用拥有\n',
            '无限力量的『环』的意见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S但是，当『环』拥有自主性后，\n',
            '它将会凭借着其势不可挡的力量\n',
            '给社会和市民生活带来惊人的变化。\n',
            '不仅不可思议地带来物质上的充足，\n',
            '甚至还囊括了精神层面的丰富。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x2282)

    Jump('loc_2697')

    def _loc_2547(): pass

    label('loc_2547')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S『关于封印机构（３／４）』\n',
            '　\n',
            '■印■■■■的，\n',
            '完■■离了■谓\n',
            '民■■义的■■。\n',
            '丂\n',
            '■使在我■■中，■存在着■■\n',
            '认为■当有效■■■■有\n',
            '无■■量■■』■意见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S■是，■■■』拥■■■■后，\n',
            '■■会凭■■■势不■■■■量\n',
            '给社会■■■生活带■■■■■■■\n',
            '■■不可思议■■来物质■■■■，\n',
            '■■■■括■精■■面的■■。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2697(): pass

    label('loc_2697')

    CloseMessageWindow()

    Jump('loc_4EE9')

    def _loc_269B(): pass

    label('loc_269B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_286A',
    )

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S『关于封印机构（４／４）』\n',
            '　\n',
            '例如『环』通过『福音』向市民\n',
            '展示了带来幸福感的虚拟现实，\n',
            '有时甚至完全控制了脑内物质。\n',
            '　\n',
            '这就跟随时随地在吸食强力无比的\n',
            '毒品或迷幻药别无二致。\n',
            '更糟糕的是，这种药品在\n',
            '生理方面完全没有副作用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S这样的恩惠将给人类的存在\n',
            '带来多么深刻的影响啊……\n',
            '　\n',
            '这种影响已经在很多市民的身上体现出来，\n',
            '留给我们的时间太少了。\n',
            '因此，我们在克服了意见的对立，\n',
            '并对将来的各种困难抱持觉悟后，\n',
            '着手实施了『封印计划』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x2283)

    Jump('loc_2A2C')

    def _loc_286A(): pass

    label('loc_286A')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S『关于封印机构（４／４）』\n',
            '　\n',
            '■■『环』■■■■音』向市■\n',
            '展■■带来■■感■虚■■实，\n',
            '■■■至■■控制■■内■质。\n',
            '　\n',
            '这就■■■随地■■■■力无■■\n',
            '毒■■迷■■■■■致■\n',
            '■■■的■■这■■品■\n',
            '■理■面■■■有■■用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S这样的■■将给人■■■在\n',
            '带来■么■■的■■■……\n',
            '　\n',
            '这种■■已经在■多市民■■■■现出■，\n',
            '■■■■的时间太■■。\n',
            '因此，我■■■服了意见■■■■\n',
            '并■将来的各■■■抱■■悟■，\n',
            '■手■■了■■■■■』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A2C(): pass

    label('loc_2A2C')

    CloseMessageWindow()

    Jump('loc_4EE9')

    def _loc_2A30(): pass

    label('loc_2A30')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 0, 0x2218)),
            Expr.Return,
        ),
        'loc_2BE5',
    )

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S『关于湖岸的地下设施（１／４）』\n',
            '　\n',
            '要使『封印机构』建立成形，\n',
            '庞大的能量以及\n',
            '大规模的设施都是不可或缺的。\n',
            '作为能量的来源，我们首先\n',
            '研究尝试了对『环』本身的利用。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S『环』会对人的愿望产生反应，\n',
            '进而给予恩惠－－也就是说，\n',
            '我们当时猜想可否藉由此方式\n',
            '从『环』之中提取必须的能量。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S……但是这种想法没能行得通。\n',
            '『环』在拥有了自主性之后不久，\n',
            '那种恩惠就与人的愿望脱离关系，\n',
            '成为了单方面的给予。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x2284)

    Jump('loc_2D8F')

    def _loc_2BE5(): pass

    label('loc_2BE5')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S『关于湖岸的地下设施（１／４）』\n',
            '　\n',
            '要使『■印■■』建■■形，\n',
            '■大的■■■■\n',
            '■规模■■施都■不可■■■。\n',
            '作为■■的■■，我■■先\n',
            '研究■■■对『■■■■的利用。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S■■』会对人的愿望■■■■■\n',
            '■■■予■■－－也就是■■\n',
            '我■当时■■■否■■■■方式\n',
            '从『环』■中■■■须■■量。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S……■■■种■■没能■得■。\n',
            '■■』在拥有了■主性■■■久，\n',
            '那种■■就与人的■■■■关系，\n',
            '■为了■方■的■予■',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2D8F(): pass

    label('loc_2D8F')

    CloseMessageWindow()

    Jump('loc_4EE9')

    def _loc_2D93(): pass

    label('loc_2D93')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 0, 0x2218)),
            Expr.Return,
        ),
        'loc_2F27',
    )

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S『关于湖岸地下设施（２／４）』\n',
            '　\n',
            '－－利用『环』的力量的构想无法实现。\n',
            '我们便将目光转向都市之外，\n',
            '找到了深深沉眠在大地中的七耀脉能源之后，\n',
            '我们试图在那里建造设施。\n',
            '　\n',
            '但是，我们当时已经完全\n',
            '置身于『环』的监视之下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S『环』的思考模式\n',
            '似乎是把城市的存续放在第一位\n',
            '而排除所有可能对此造成威胁的因素。\n',
            '　\n',
            '因此为了欺骗『环』，我们就在\n',
            '观测七耀脉的名义下进行设施的建造。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x2285)

    Jump('loc_30AF')

    def _loc_2F27(): pass

    label('loc_2F27')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S『关于湖岸的地下设施（２／４）』\n',
            '　\n',
            '■■■■环■的力量■■■■法实现。\n',
            '#1S■们■■■光转■■市■■■\n',
            '找到■■深沉眠■■■中的七耀脉■■■■■\n',
            '■们■■在■里■造■■。\n',
            '　\n',
            '■是，我们当■■经完■\n',
            '置■于『■』的监■■下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S■环』的■■■■\n',
            '似乎是■■■的存续放■第■位\n',
            '而排■■■■能对此■成■胁的■■■\n',
            '　\n',
            '■■为了■■『■』，我们就■\n',
            '观测七■■的名义下■■施的■造。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_30AF(): pass

    label('loc_30AF')

    CloseMessageWindow()

    Jump('loc_4EE9')

    def _loc_30B3(): pass

    label('loc_30B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 0, 0x2218)),
            Expr.Return,
        ),
        'loc_3208',
    )

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S『关于湖岸的地下设施（３／４）』\n',
            '　\n',
            '设施被建在瓦雷利亚湖东岸\n',
            '地下５００亚矩的位置。\n',
            '根据调查显示，\n',
            '那里是七耀脉高密度集中的地方。\n',
            '　\n',
            '都市底下的辽阔大地，\n',
            '被郁郁葱葱的原生林笼罩着。\n',
            '其间完全无人涉足，\n',
            '没有任何事物对工程造成阻碍。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S我们一边逃避『环』的监视，\n',
            '一边集结所有技术力量\n',
            '火速进行地下设施的建设。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x2286)

    Jump('loc_3354')

    def _loc_3208(): pass

    label('loc_3208')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S『关于湖岸的地下设施（３／４）』\n',
            '　\n',
            '设施■■■■雷利亚■东■\n',
            '地下５■０■■的位■■\n',
            '#1S■调查■■■\n',
            '那里是七■脉■■■■中■地方。\n',
            '　\n',
            '都市■■的■■■地，\n',
            '被郁郁■葱■原生■■■着。\n',
            '#1S■完全■■■足，\n',
            '没有任■事物对工程■■■■。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S■■一边逃避『■』■监视，\n',
            '一■■结所有■■■量，\n',
            '火■■行地■■施的■■。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3354(): pass

    label('loc_3354')

    CloseMessageWindow()

    Jump('loc_4EE9')

    def _loc_3358(): pass

    label('loc_3358')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 0, 0x2218)),
            Expr.Return,
        ),
        'loc_34D6',
    )

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S『关于湖岸的地下设施（４／４）』\n',
            '　\n',
            '在进行地下设施建造的期间，\n',
            '我们在『环』未察觉的情况下，\n',
            '于地面的周边部分\n',
            '建起了两种巨大的建筑物。\n',
            '　\n',
            '一种是内壁一致朝向\n',
            '『环』的方向的长城『亚宁堡』。\n',
            '而另一种则是包围着『环』，\n',
            '矗立于地面的四座『设备塔』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S这两种建筑物在计划中\n',
            '分别有着各自重要的任务，\n',
            '它们和地下设施一样，\n',
            '都是『封印机构』不可或缺的存在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x2287)

    Jump('loc_3647')

    def _loc_34D6(): pass

    label('loc_34D6')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S『关于湖岸的地下设施（４／４）』\n',
            '　\n',
            '在进行■■■■建■■期间，\n',
            '■们在『环■■■■的情况■，\n',
            '于■■的周■■分\n',
            '建起了■■巨大■■■物。\n',
            '　\n',
            '■■■■壁■■朝向\n',
            '『■』的方■■■城■■■堡』。\n',
            '而另■■则■■围■■环』，\n',
            '■立于■■的四■■■■塔』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S这两■建■■在计■■\n',
            '分■有着■■■要■任务，\n',
            '它们和■下■■一■■\n',
            '都■『封印■■』■■■缺的■■。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3647(): pass

    label('loc_3647')

    CloseMessageWindow()

    Jump('loc_4EE9')

    def _loc_364B(): pass

    label('loc_364B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 6, 0x221E)),
            Expr.Return,
        ),
        'loc_37C9',
    )

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S关于『环』的封印（１／４）\n',
            '　\n',
            '当地下设施的建造即将完成的时候，\n',
            '在不知不觉中，我们被\n',
            '『环』得知了『封印计划』的存在。\n',
            '　\n',
            '原因是我们其中一名同胞禁不住\n',
            '『环』的诱惑而被其介入精神之中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S不过，那名同胞没有处于\n',
            '能够得知计划全貌的立场上，\n',
            '这实在是不幸中的万幸。\n',
            '　\n',
            '『环』并没有将目光放在\n',
            '长城『亚宁堡』和『设备塔』上，\n',
            '而是只掌握到了湖畔的地下设施。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x2288)

    Jump('loc_393A')

    def _loc_37C9(): pass

    label('loc_37C9')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S关于『环』的封印（１／４）\n',
            '　\n',
            '当地■■■■建■■将■■■■候，\n',
            '在■知不■中■■们被\n',
            '『■■■知了『■■■■』■存在。\n',
            '丂\n',
            '■因是■们其■■名同■■■住\n',
            '『■』的诱■而被■■■精■■中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S不过■■■■胞没有■于\n',
            '能■■■计划全■■■场■■\n',
            '■■■是不幸■■■■。\n',
            '丂\n',
            '『■』并■■■■■放在\n',
            '长城■■■■■和『设■■■上，\n',
            '■是只■■■了湖■的■■■■。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_393A(): pass

    label('loc_393A')

    CloseMessageWindow()

    Jump('loc_4EE9')

    def _loc_393E(): pass

    label('loc_393E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 6, 0x221E)),
            Expr.Return,
        ),
        'loc_3AF3',
    )

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S『关于‘环’的封印（２／４）』\n',
            '　\n',
            '得知我们计划的『环』\n',
            '所采取的手段是强制性的。\n',
            '　\n',
            '『环』诞生出了几台\n',
            '被称为『幻想乐曲』\n',
            '的自身守护者，\n',
            '并向来到设施中的我们袭来\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S不过，幸运的是\n',
            '我们的设施建造于地下。\n',
            '地上与设施之间\n',
            '相连的路径只有一条。\n',
            '『幻想乐曲』的攻击\n',
            '无法直接到达\n',
            '地下５００亚矩的深处。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S但是，『幻想乐曲』的攻击\n',
            '却日夜不停地持续进行着。\n',
            '过了不久之后，\n',
            '我们坚固的防线也逼近了极限。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x2289)

    Jump('loc_3C98')

    def _loc_3AF3(): pass

    label('loc_3AF3')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S『关于‘环’的封印（２／４）』\n',
            '　\n',
            '得知■■■划的■环■\n',
            '■采■■手段■强制■■■\n',
            '丂\n',
            '『■』诞生出■■■\n',
            '被称为『■想■■』\n',
            '的自■■护者，\n',
            '并■来到■■中的我们■■\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S不■，■■的■\n',
            '■■的设■建造■■下。\n',
            '地■■■施之■\n',
            '相连■■■只■一■。\n',
            '■■想乐■』的攻■\n',
            '无法■■■■\n',
            '■■５００■■■■■。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S■■，■■■乐■』的攻■\n',
            '却日■不■■持续■■■。\n',
            '过■■久之■，\n',
            '■们坚固■■■■逼近■■■。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3C98(): pass

    label('loc_3C98')

    CloseMessageWindow()

    Jump('loc_4EE9')

    def _loc_3C9C(): pass

    label('loc_3C9C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 6, 0x221E)),
            Expr.Return,
        ),
        'loc_3E98',
    )

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S『关于‘环’的封印（３／４）』\n',
            '　\n',
            '在承受『幻想乐曲』的攻击期间，\n',
            '设施的建造终于完成了，\n',
            '然而我们还需要一些时间\n',
            '确保从七耀脉中得到计划所需的能量。\n',
            '　\n',
            '但是，或许是设施的完工\n',
            '让我们松懈下来了──\n',
            '我们不小心让一架『幻想乐曲』\n',
            '进入了设施的内部。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S一旦让它进入内部之后，\n',
            '要阻止它的攻击就十分困难了。\n',
            '『幻想乐曲』一转眼\n',
            '便抵达了设施的最深处。\n',
            '　\n',
            '──真是千钧一发啊。\n',
            '来到最深处的『幻想乐曲』\n',
            '正要展开破坏活动时，\n',
            '计划所需的能量终于收集完毕了，\n',
            '于是我们马上启动了『第一结界』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x228A)

    Jump('loc_408A')

    def _loc_3E98(): pass

    label('loc_3E98')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S『关于‘环’的封印（３／４）』\n',
            '　\n',
            '在■■■幻想乐■■的攻■■间，\n',
            '设■的■■■于■成了，\n',
            '然■我们■■■一■时■\n',
            '■■从■■脉中■■计■■■的能■■\n',
            '　\n',
            '但是，■■■设施的■■\n',
            '让我■松■■来■──\n',
            '■■不小■■■架■幻■■曲』\n',
            '■入了■■的内部。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S■旦让■进入■■■■，\n',
            '要阻止■■■■就十分■■■■\n',
            '■■想■■■■■眼\n',
            '■■■了■■■■■处。\n',
            '　\n',
            '■─真是■■一■啊。\n',
            '#1S来到■■■■『■■■曲』\n',
            '正要展■■坏■■时，\n',
            '■■所需的■■终于■■■■■，\n',
            '于是我们■上启■■■第■结■■。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_408A(): pass

    label('loc_408A')

    CloseMessageWindow()

    Jump('loc_4EE9')

    def _loc_408E(): pass

    label('loc_408E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 6, 0x221E)),
            Expr.Return,
        ),
        'loc_4298',
    )

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S『关于‘环’的封印（４／４）』\n',
            '　\n',
            '设施所释放出的光芒，\n',
            '经过长城『亚宁堡』的内壁增幅后，\n',
            '顺利地捕捉到了漂浮在空中的『环』。\n',
            '　\n',
            '于是，『环』\n',
            '便从我们眼前消失了，\n',
            '『幻想乐曲』也停止了运转。\n',
            '就这样，我们确认\n',
            '『第一结界』顺利地发动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S『环』是『七至宝』中\n',
            '掌管空间的至宝。\n',
            '为了让拥有对空间的绝对支配力量的『环』\n',
            '失去效力，所必须做的事情就是──\n',
            '断绝掉『环』对空间\n',
            '乃至对时间的一切干涉。\n',
            '　\n',
            '我们费尽心血所建立起的『封印机构』\n',
            '将『环』连同都市一起送进了异次元，\n',
            '成功地实现了『时间冻结』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x228B)

    Jump('loc_4495')

    def _loc_4298(): pass

    label('loc_4298')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S『关于‘环’的封印（４／４）』\n',
            '　\n',
            '设施■■■■的光■■\n',
            '■过长城『■■■』■■■■■后，\n',
            '■■■■■到了■■在空中■■■』。\n',
            '　\n',
            '■是，■环■\n',
            '■从我们■■消■■，\n',
            '『■■■曲』■■■了运■。\n',
            '■这样■■■确认\n',
            '『■■■■』顺利■■■了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S■环■是■■至宝■中\n',
            '■■空间的■■。\n',
            '■了让拥■■空■■■■■■力量的■■』\n',
            '失去■■■所■■■的事情■■──\n',
            '■绝掉■■■对空间\n',
            '■至对时间的■■■■。\n',
            '　\n',
            '我们费■■血■■■起的■■印■■』\n',
            '将■■■连同都■■■■进了■■元，\n',
            '成功地■■■■时■■结■。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4495(): pass

    label('loc_4495')

    CloseMessageWindow()

    Jump('loc_4EE9')

    def _loc_4499(): pass

    label('loc_4499')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Return,
        ),
        'loc_45B1',
    )

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S『关于设备塔（１／４）』\n',
            '　\n',
            '『第一结界』顺利发动，\n',
            '我们将『环』封进异次元，\n',
            '成功地实现了『时间冻结』。\n',
            '　\n',
            '但是，正如名称所示\n',
            '『封印计划』中的结界\n',
            '并非只有这一道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S『封印计划』最后的防线是『第二结界』。\n',
            '　\n',
            '──其关键是由\n',
            '四座设备塔所掌握的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x2276)

    Jump('loc_46BC')

    def _loc_45B1(): pass

    label('loc_45B1')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S『关于设备塔（１／４）』\n',
            '　\n',
            '■第一■界』■利■■，\n',
            '我们■『环■■进■■元，\n',
            '成■■实现■■时间■■■。\n',
            '　\n',
            '但■，正如■■■示\n',
            '『■■计划』■■■■\n',
            '■非■■■一■。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S■封印计■』最后的■■■『■二■界■。\n',
            '　\n',
            '──■■■■■\n',
            '■■■■塔■■握的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_46BC(): pass

    label('loc_46BC')

    CloseMessageWindow()

    Jump('loc_4EE9')

    def _loc_46C0(): pass

    label('loc_46C0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Return,
        ),
        'loc_47F1',
    )

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S『关于设备塔（２／４）』\n',
            '这个机构在『第一结界』被解除\n',
            '『环』的时间再次开始流动之时，\n',
            '便会自行发动。\n',
            '　\n',
            '『第二结界』\n',
            '又名『重力结界』，\n',
            '拥有在异次元中\n',
            '产生重力的机能。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S其目的是当『环』开始活动的时候，\n',
            '利用重力之楔将它维系在异次元之中，\n',
            '藉此防止『环』重新出现于世上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x2277)

    Jump('loc_4916')

    def _loc_47F1(): pass

    label('loc_47F1')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S『关于设备塔（２／４）』\n',
            '　\n',
            '■■机■在『■■■■』被解除\n',
            '■环■的时间■■开始■■之时\n',
            '■会■■■动。\n',
            '　\n',
            '『■二■界』\n',
            '■■『重力结■』，\n',
            '拥有在■次■中\n',
            '■■■■的机能。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S其■■是当『环』■■活动■■■■\n',
            '利用■■■楔将■维系■■■元■■，\n',
            '■此■■『■』重新■■于■上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4916(): pass

    label('loc_4916')

    CloseMessageWindow()

    Jump('loc_4EE9')

    def _loc_491A(): pass

    label('loc_491A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Return,
        ),
        'loc_4A5D',
    )

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S『关于设备塔（３／４）』\n',
            '　\n',
            '当『第二结界』发动时，\n',
            '『环』已经开始了运转。\n',
            '　\n',
            '如果使用那个名为『福音』的终端，\n',
            '便可以随心所欲地提取它的力量。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S残留在『利贝尔·方舟』中的\n',
            '『福音』\n',
            '与『环』一样是被封印起来的。\n',
            '　\n',
            '但是，如果后世出现了\n',
            '可以代替『福音』的东西，\n',
            '『环』的力量便会波及到世间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x2278)

    Jump('loc_4B8F')

    def _loc_4A5D(): pass

    label('loc_4A5D')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S『关于数据塔（３／４）』\n',
            '　\n',
            '当『第二结界■发■■，\n',
            '『■』已经■■■■转。\n',
            '　\n',
            '如果使用那个■为■■■■的■■，\n',
            '■■■随■所欲地■■■的■量。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S■留在■贝■·■舟■■\n',
            '■■音』\n',
            '■■■』一样是■■■■来■■\n',
            '　\n',
            '但是，如果■■■现了\n',
            '■■代■■■■』的东西，\n',
            '■环■的力量便会■■到■■。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4B8F(): pass

    label('loc_4B8F')

    CloseMessageWindow()

    Jump('loc_4EE9')

    def _loc_4B93(): pass

    label('loc_4B93')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Return,
        ),
        'loc_4D3B',
    )

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S『关于设备塔（４／４）』\n',
            '　\n',
            '虽然我们成功地封印了『环』，\n',
            '但并没能使它的力量消失。\n',
            '　\n',
            '我们打算扎根于此地，\n',
            '世世代代一直看守着『环』。\n',
            '并且祈祷这些记录\n',
            '不被任何人看到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S然而与此同时\n',
            '我们也预见，这是不可能的事。\n',
            '　\n',
            '『环』再次出现在世间的时候，\n',
            '生活于后世里的人们\n',
            '将做出怎样的选择呢──\n',
            '　\n',
            '我们相信人类将不会再次犯错，\n',
            '相信终有从『环』中解放出来的一天\n',
            '因此，我们决定将这些记录托付给后世。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x2279)

    Jump('loc_4ED8')

    def _loc_4D3B(): pass

    label('loc_4D3B')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S『关于设备塔（４／４）』\n',
            '　\n',
            '■■■■成功地封■了『■』，\n',
            '但■没■■■的力■■失。\n',
            '　\n',
            '我■打算■■■此地，\n',
            '■■■代一直■■着『■』。\n',
            '并且祈祷■■■■\n',
            '不被■■人看到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S■■■此同时\n',
            '我们也■见，这是■■能的事。\n',
            '　\n',
            '『环■再次出■在世间■■■，\n',
            '生活于■世里的■■\n',
            '将做出■■■选择■－－\n',
            '　\n',
            '我们相信人类■不会■次■错，\n',
            '■■终有从■环■中■■■■的一天。\n',
            '■■，我们决定■这些■■■■给■■。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4ED8(): pass

    label('loc_4ED8')

    CloseMessageWindow()

    Jump('loc_4EE9')

    def _loc_4EDC(): pass

    label('loc_4EDC')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_4EE9')

    def _loc_4EE9(): pass

    label('loc_4EE9')

    Jump('loc_15A7')

    def _loc_4EEC(): pass

    label('loc_4EEC')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Xor2,
            Expr.Return,
        ),
    )

    OP_5F(0x0001)

    Jump('loc_4F09')

    def _loc_4EFC(): pass

    label('loc_4EFC')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_4F09')

    def _loc_4F09(): pass

    label('loc_4F09')

    Jump('loc_1A4')

    def _loc_4F0C(): pass

    label('loc_4F0C')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    FadeIn(300, 0)
    EventEnd(0x01)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
