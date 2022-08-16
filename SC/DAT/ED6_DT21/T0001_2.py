import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0001_2_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0001_2 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'map'
    header.mapModel       = 'T0001.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
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
            preInitFunction = 0x0001,
            initScena       = 0x0000,
            initFunction    = 0x0002,
        ),
    )

# id: 0x10000 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
    ]

# id: 0x10001 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10002 offset: 0xA8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xA8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0xA8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xA8
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1CF',
    )

    Menu(
        1,
        10,
        100,
        1,
        (
            TXT(0x00, '测试\n'),
            TXT(0x01, '跳跳猫\n'),
            TXT(0x02, '盔甲巨蟹\n'),
            TXT(0x03, '跳跳猫3\n'),
            TXT(0x04, '人型Boss\n'),
            TXT(0x05, '大型Boss\n'),
            TXT(0x06, '其他Boss\n'),
            TXT(0x07, '自动战斗\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_12B'),
        (0x00000001, 'loc_13B'),
        (0x00000002, 'loc_14B'),
        (0x00000003, 'loc_15B'),
        (0x00000004, 'loc_16B'),
        (0x00000005, 'loc_172'),
        (0x00000006, 'loc_179'),
        (0x00000007, 'loc_180'),
        (-1, 'loc_187'),
    )

    def _loc_12B(): pass

    label('loc_12B')

    Battle(0x00000466, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_18A')

    def _loc_13B(): pass

    label('loc_13B')

    Battle(0x000007D4, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_18A')

    def _loc_14B(): pass

    label('loc_14B')

    Battle(0x000007D5, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_18A')

    def _loc_15B(): pass

    label('loc_15B')

    Battle(0x000007D7, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_18A')

    def _loc_16B(): pass

    label('loc_16B')

    Call(2, 0x0035)

    Jump('loc_18A')

    def _loc_172(): pass

    label('loc_172')

    Call(2, 0x0036)

    Jump('loc_18A')

    def _loc_179(): pass

    label('loc_179')

    Call(2, 0x0037)

    Jump('loc_18A')

    def _loc_180(): pass

    label('loc_180')

    Call(2, 0x0038)

    Jump('loc_18A')

    def _loc_187(): pass

    label('loc_187')

    Jump('loc_18A')

    def _loc_18A(): pass

    label('loc_18A')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_0D()

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_1A1'),
        (-1, 'loc_1CC'),
    )

    def _loc_1A1(): pass

    label('loc_1A1')

    ChrSetStatus(ChrTable['艾丝蒂尔'], 0xFE, 0)
    ChrSetStatus(ChrTable['约修亚'], 0xFE, 0)
    ChrSetStatus(ChrTable['雪拉扎德'], 0xFE, 0)
    ChrSetStatus(ChrTable['奥利维尔'], 0xFE, 0)
    ChrSetStatus(ChrTable['科洛丝'], 0xFE, 0)
    ChrSetStatus(ChrTable['阿加特'], 0xFE, 0)
    ChrSetStatus(ChrTable['提妲'], 0xFE, 0)
    ChrSetStatus(ChrTable['金'], 0xFE, 0)

    Jump('loc_1CC')

    def _loc_1CC(): pass

    label('loc_1CC')

    Jump('Init')

    def _loc_1CF(): pass

    label('loc_1CF')

    OP_5F(0x0001)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0001 offset: 0x1DD
@scena.Code('func_01_1DD')
def func_01_1DD():
    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    def _loc_1E7(): pass

    label('loc_1E7')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_291',
    )

    Menu(
        1,
        10,
        100,
        1,
        (
            TXT(0x00, '测试\n'),
            TXT(0x01, '洛连特\n'),
            TXT(0x02, '柏斯\n'),
            TXT(0x03, '卢安\n'),
            TXT(0x04, '蔡斯\n'),
            TXT(0x05, '格兰赛尔\n'),
            TXT(0x06, '其他\n'),
            TXT(0x07, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_253'),
        (0x00000001, 'loc_25A'),
        (0x00000002, 'loc_261'),
        (0x00000003, 'loc_268'),
        (0x00000004, 'loc_26F'),
        (0x00000005, 'loc_276'),
        (0x00000006, 'loc_27D'),
        (-1, 'loc_284'),
    )

    def _loc_253(): pass

    label('loc_253')

    Call(2, 0x0002)

    Jump('loc_28E')

    def _loc_25A(): pass

    label('loc_25A')

    Call(2, 0x0003)

    Jump('loc_28E')

    def _loc_261(): pass

    label('loc_261')

    Call(2, 0x0004)

    Jump('loc_28E')

    def _loc_268(): pass

    label('loc_268')

    Call(2, 0x0005)

    Jump('loc_28E')

    def _loc_26F(): pass

    label('loc_26F')

    Call(2, 0x0006)

    Jump('loc_28E')

    def _loc_276(): pass

    label('loc_276')

    Call(2, 0x0007)

    Jump('loc_28E')

    def _loc_27D(): pass

    label('loc_27D')

    Call(2, 0x0008)

    Jump('loc_28E')

    def _loc_284(): pass

    label('loc_284')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_28E(): pass

    label('loc_28E')

    Jump('loc_1E7')

    def _loc_291(): pass

    label('loc_291')

    OP_5F(0x0001)
    OP_56(0x00)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0002 offset: 0x2A1
@scena.Code('func_02_2A1')
def func_02_2A1():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_389',
    )

    Menu(
        2,
        10,
        100,
        1,
        (
            TXT(0x00, '地图１ BTTEST01\n'),
            TXT(0x01, '地图２ BTTEST02\n'),
            TXT(0x02, '地图３ BTTEST03\n'),
            TXT(0x03, '地图４ BTTEST04\n'),
            TXT(0x04, '地图５ BTTEST05\n'),
            TXT(0x05, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_32C'),
        (0x00000001, 'loc_33C'),
        (0x00000002, 'loc_34C'),
        (0x00000003, 'loc_35C'),
        (0x00000004, 'loc_36C'),
        (-1, 'loc_37C'),
    )

    def _loc_32C(): pass

    label('loc_32C')

    Battle(0x000007DA, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_386')

    def _loc_33C(): pass

    label('loc_33C')

    Battle(0x000007DB, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_386')

    def _loc_34C(): pass

    label('loc_34C')

    Battle(0x000007DC, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_386')

    def _loc_35C(): pass

    label('loc_35C')

    Battle(0x000007DD, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_386')

    def _loc_36C(): pass

    label('loc_36C')

    Battle(0x000007DE, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_386')

    def _loc_37C(): pass

    label('loc_37C')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_386(): pass

    label('loc_386')

    Jump('func_02_2A1')

    def _loc_389(): pass

    label('loc_389')

    OP_5F(0x0002)
    OP_56(0x00)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0003 offset: 0x399
@scena.Code('func_03_399')
def func_03_399():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4AB',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        2,
        10,
        80,
        1,
        (
            TXT(0x00, 'BC0700（里）翡翠之塔战斗地图\n'),
            TXT(0x01, 'BC0701（里）翡翠之塔战斗地图（塔顶Boss战）\n'),
            TXT(0x02, 'BT0400 帕赛尔农场（雾）\n'),
            TXT(0x03, 'BC0403 翡翠之塔战斗地图\n'),
            TXT(0x04, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_452'),
        (0x00000001, 'loc_462'),
        (0x00000002, 'loc_472'),
        (0x00000003, 'loc_48E'),
        (-1, 'loc_49E'),
    )

    def _loc_452(): pass

    label('loc_452')

    Battle(0x000003EE, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_4A8')

    def _loc_462(): pass

    label('loc_462')

    Battle(0x00000456, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_4A8')

    def _loc_472(): pass

    label('loc_472')

    OP_C4(0x00, 0x00000004)
    Battle(0x00000799, 0x00000000, 0x00, 0x0000, 0xFF)
    OP_C4(0x01, 0x00000004)

    Jump('loc_4A8')

    def _loc_48E(): pass

    label('loc_48E')

    Battle(0x00000031, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_4A8')

    def _loc_49E(): pass

    label('loc_49E')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_4A8(): pass

    label('loc_4A8')

    Jump('func_03_399')

    def _loc_4AB(): pass

    label('loc_4AB')

    OP_5F(0x0002)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0004 offset: 0x4B9
@scena.Code('func_04_4B9')
def func_04_4B9():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_612',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        2,
        10,
        80,
        1,
        (
            TXT(0x00, 'BC1601　古龙的住处战斗地图\n'),
            TXT(0x01, 'BC1603　古龙的住处战斗地图（Boss战\n'),
            TXT(0x02, 'BC1700　（里）琥珀之塔战斗地图\n'),
            TXT(0x03, 'BC1701　（里）琥珀之塔战斗地图（塔顶boss战）\n'),
            TXT(0x04, 'BC1203　（表）琥珀之塔战斗地图（塔顶boss战）\n'),
            TXT(0x05, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_5B5'),
        (0x00000001, 'loc_5C5'),
        (0x00000002, 'loc_5D5'),
        (0x00000003, 'loc_5E5'),
        (0x00000004, 'loc_5F5'),
        (-1, 'loc_605'),
    )

    def _loc_5B5(): pass

    label('loc_5B5')

    Battle(0x000003C7, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_60F')

    def _loc_5C5(): pass

    label('loc_5C5')

    Battle(0x0000044F, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_60F')

    def _loc_5D5(): pass

    label('loc_5D5')

    Battle(0x000003F4, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_60F')

    def _loc_5E5(): pass

    label('loc_5E5')

    Battle(0x00000457, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_60F')

    def _loc_5F5(): pass

    label('loc_5F5')

    Battle(0x00000093, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_60F')

    def _loc_605(): pass

    label('loc_605')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_60F(): pass

    label('loc_60F')

    Jump('func_04_4B9')

    def _loc_612(): pass

    label('loc_612')

    OP_5F(0x0002)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0005 offset: 0x620
@scena.Code('func_05_620')
def func_05_620():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_844',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        2,
        10,
        80,
        1,
        (
            TXT(0x00, 'BC2300　（里）绀碧之塔战斗地图\n'),
            TXT(0x01, 'BC2301　（里）绀碧之塔战斗地图（塔顶boss战）\n'),
            TXT(0x02, 'BC2400　王立学院旧校舍地下\n'),
            TXT(0x03, 'BC2401　王立学院旧校舍地下Boss\n'),
            TXT(0x04, 'BC2500　王立学院校园\n'),
            TXT(0x05, 'BC2510　王立学院走廊\n'),
            TXT(0x06, 'BC2511　王立学院男子宿舍\n'),
            TXT(0x07, 'BC2512　王立学院女子宿舍\n'),
            TXT(0x08, 'BT2611　王立学院旧校舍内部（白天）\n'),
            TXT(0x09, 'BC2102　绀碧之塔战斗地图\n'),
            TXT(0x0A, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_797'),
        (0x00000001, 'loc_7A7'),
        (0x00000002, 'loc_7B7'),
        (0x00000003, 'loc_7C7'),
        (0x00000004, 'loc_7D7'),
        (0x00000005, 'loc_7E7'),
        (0x00000006, 'loc_7F7'),
        (0x00000007, 'loc_807'),
        (0x00000008, 'loc_817'),
        (0x00000009, 'loc_827'),
        (-1, 'loc_837'),
    )

    def _loc_797(): pass

    label('loc_797')

    Battle(0x00000407, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_841')

    def _loc_7A7(): pass

    label('loc_7A7')

    Battle(0x00000454, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_841')

    def _loc_7B7(): pass

    label('loc_7B7')

    Battle(0x00000398, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_841')

    def _loc_7C7(): pass

    label('loc_7C7')

    Battle(0x0000044C, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_841')

    def _loc_7D7(): pass

    label('loc_7D7')

    Battle(0x00000F3C, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_841')

    def _loc_7E7(): pass

    label('loc_7E7')

    Battle(0x0000079C, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_841')

    def _loc_7F7(): pass

    label('loc_7F7')

    Battle(0x0000079D, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_841')

    def _loc_807(): pass

    label('loc_807')

    Battle(0x0000079F, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_841')

    def _loc_817(): pass

    label('loc_817')

    Battle(0x00000F40, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_841')

    def _loc_827(): pass

    label('loc_827')

    Battle(0x000001BD, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_841')

    def _loc_837(): pass

    label('loc_837')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_841(): pass

    label('loc_841')

    Jump('func_05_620')

    def _loc_844(): pass

    label('loc_844')

    OP_5F(0x0002)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0006 offset: 0x852
@scena.Code('func_06_852')
def func_06_852():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9F3',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        2,
        10,
        80,
        1,
        (
            TXT(0x00, 'BC3600　（里）红莲之塔战斗地图\n'),
            TXT(0x01, 'BC3601　（里）红莲之塔战斗地图（塔顶boss战）\n'),
            TXT(0x02, 'BC3400　温泉源流战斗地图\n'),
            TXT(0x03, 'BC3401　温泉源流战斗地图（Boss战）\n'),
            TXT(0x04, 'BT0600　亚宁堡城墙（格鲁纳门）\n'),
            TXT(0x05, 'BC3101　雷斯顿要塞中庭\n'),
            TXT(0x06, 'BC3503　红莲之塔战斗地图\n'),
            TXT(0x07, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_976'),
        (0x00000001, 'loc_986'),
        (0x00000002, 'loc_996'),
        (0x00000003, 'loc_9A6'),
        (0x00000004, 'loc_9B6'),
        (0x00000005, 'loc_9C6'),
        (0x00000006, 'loc_9D6'),
        (-1, 'loc_9E6'),
    )

    def _loc_976(): pass

    label('loc_976')

    Battle(0x00000412, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_9F0')

    def _loc_986(): pass

    label('loc_986')

    Battle(0x00000455, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_9F0')

    def _loc_996(): pass

    label('loc_996')

    Battle(0x000003B0, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_9F0')

    def _loc_9A6(): pass

    label('loc_9A6')

    Battle(0x000003AF, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_9F0')

    def _loc_9B6(): pass

    label('loc_9B6')

    Battle(0x0000045A, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_9F0')

    def _loc_9C6(): pass

    label('loc_9C6')

    Battle(0x00000C80, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_9F0')

    def _loc_9D6(): pass

    label('loc_9D6')

    Battle(0x000001F5, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_9F0')

    def _loc_9E6(): pass

    label('loc_9E6')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_9F0(): pass

    label('loc_9F0')

    Jump('func_06_852')

    def _loc_9F3(): pass

    label('loc_9F3')

    OP_5F(0x0002)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0007 offset: 0xA01
@scena.Code('func_07_A01')
def func_07_A01():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B5E',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        2,
        10,
        80,
        1,
        (
            TXT(0x00, 'BT4403　王都格兰赛尔外部（码头）战斗地图（Boss）\n'),
            TXT(0x01, 'BT4404　王都格兰赛尔外部（码头）战斗地图（小怪）\n'),
            TXT(0x02, 'BT4405　王都格兰赛尔外部（码头）战斗地图（仓库内）\n'),
            TXT(0x03, 'BT4100　王都街区\n'),
            TXT(0x04, 'BT4200　城门前（桥）\n'),
            TXT(0x05, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_B01'),
        (0x00000001, 'loc_B11'),
        (0x00000002, 'loc_B21'),
        (0x00000003, 'loc_B31'),
        (0x00000004, 'loc_B41'),
        (-1, 'loc_B51'),
    )

    def _loc_B01(): pass

    label('loc_B01')

    Battle(0x0000045E, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_B5B')

    def _loc_B11(): pass

    label('loc_B11')

    Battle(0x0000045D, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_B5B')

    def _loc_B21(): pass

    label('loc_B21')

    Battle(0x0000045C, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_B5B')

    def _loc_B31(): pass

    label('loc_B31')

    Battle(0x0000079E, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_B5B')

    def _loc_B41(): pass

    label('loc_B41')

    Battle(0x00000550, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_B5B')

    def _loc_B51(): pass

    label('loc_B51')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_B5B(): pass

    label('loc_B5B')

    Jump('func_07_A01')

    def _loc_B5E(): pass

    label('loc_B5E')

    OP_5F(0x0002)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0008 offset: 0xB6C
@scena.Code('func_08_B6C')
def func_08_B6C():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BEE',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        2,
        10,
        80,
        1,
        (
            TXT(0x00, '卢·洛克尔，研究所，古罗力亚斯\n'),
            TXT(0x01, '中枢塔，辉之环\n'),
            TXT(0x02, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_BD3'),
        (0x00000001, 'loc_BDA'),
        (-1, 'loc_BE1'),
    )

    def _loc_BD3(): pass

    label('loc_BD3')

    Call(2, 0x0009)

    Jump('loc_BEB')

    def _loc_BDA(): pass

    label('loc_BDA')

    Call(2, 0x000A)

    Jump('loc_BEB')

    def _loc_BE1(): pass

    label('loc_BE1')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_BEB(): pass

    label('loc_BEB')

    Jump('func_08_B6C')

    def _loc_BEE(): pass

    label('loc_BEE')

    OP_5F(0x0002)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0009 offset: 0xBFC
@scena.Code('func_09_BFC')
def func_09_BFC():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_EE8',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        80,
        1,
        (
            TXT(0x00, 'BT5110　卢·洛克尔宿舍\n'),
            TXT(0x01, 'BC5500　卢·洛克尔训练场战斗地图（训练场１）\n'),
            TXT(0x02, 'BC5501　卢·洛克尔训练场战斗地图（训练场１Boss战）\n'),
            TXT(0x03, 'BC5502　卢·洛克尔训练场战斗地图（训练场２）\n'),
            TXT(0x04, 'BC5503　卢·洛克尔训练场战斗地图（训练场２Boss战）\n'),
            TXT(0x05, 'BC5504　卢·洛克尔训练场战斗地图（训练场３）\n'),
            TXT(0x06, 'BC5505　卢·洛克尔训练场战斗地图（训练场３Boss战）\n'),
            TXT(0x07, 'BC5610　研究所·房间战斗地图\n'),
            TXT(0x08, 'BC5611　研究所·通路战斗地图\n'),
            TXT(0x09, 'BC5400　古罗力亚斯通路\n'),
            TXT(0x0A, 'BC5408　古罗力亚斯甲板\n'),
            TXT(0x0B, 'BC5406　古罗力亚斯机库（Boss）\n'),
            TXT(0x0C, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_E1B'),
        (0x00000001, 'loc_E2B'),
        (0x00000002, 'loc_E3B'),
        (0x00000003, 'loc_E4B'),
        (0x00000004, 'loc_E5B'),
        (0x00000005, 'loc_E6B'),
        (0x00000006, 'loc_E7B'),
        (0x00000007, 'loc_E8B'),
        (0x00000008, 'loc_E9B'),
        (0x00000009, 'loc_EAB'),
        (0x0000000A, 'loc_EBB'),
        (0x0000000B, 'loc_ECB'),
        (-1, 'loc_EDB'),
    )

    def _loc_E1B(): pass

    label('loc_E1B')

    Battle(0x00000397, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_EE5')

    def _loc_E2B(): pass

    label('loc_E2B')

    Battle(0x00000387, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_EE5')

    def _loc_E3B(): pass

    label('loc_E3B')

    Battle(0x00000393, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_EE5')

    def _loc_E4B(): pass

    label('loc_E4B')

    Battle(0x00000389, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_EE5')

    def _loc_E5B(): pass

    label('loc_E5B')

    Battle(0x00000394, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_EE5')

    def _loc_E6B(): pass

    label('loc_E6B')

    Battle(0x0000038D, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_EE5')

    def _loc_E7B(): pass

    label('loc_E7B')

    Battle(0x00000395, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_EE5')

    def _loc_E8B(): pass

    label('loc_E8B')

    Battle(0x0000041A, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_EE5')

    def _loc_E9B(): pass

    label('loc_E9B')

    Battle(0x0000041C, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_EE5')

    def _loc_EAB(): pass

    label('loc_EAB')

    Battle(0x00000427, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_EE5')

    def _loc_EBB(): pass

    label('loc_EBB')

    Battle(0x00000428, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_EE5')

    def _loc_ECB(): pass

    label('loc_ECB')

    Battle(0x00000429, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_EE5')

    def _loc_EDB(): pass

    label('loc_EDB')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_EE5(): pass

    label('loc_EE5')

    Jump('func_09_BFC')

    def _loc_EE8(): pass

    label('loc_EE8')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x000A offset: 0xEF6
@scena.Code('func_0A_EF6')
def func_0A_EF6():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_12DC',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        80,
        1,
        (
            TXT(0x00, 'BC5800　辉之环居住区外侧（事件）\n'),
            TXT(0x01, 'BC5702　辉之环工场区古罗力亚斯前（事件）\n'),
            TXT(0x02, 'BC5200　辉之环地下道战斗地图 公园区～居住区\n'),
            TXT(0x03, 'BC5201　辉之环地下道战斗地图 居住区～工场区\n'),
            TXT(0x04, 'BC5202　辉之环地下道战斗地图 工场区～中枢塔\n'),
            TXT(0x05, 'BC5203　辉之环地下道战斗地图 中枢塔～公园区\n'),
            TXT(0x06, 'BC5300　中枢塔内部战斗地图\n'),
            TXT(0x07, 'BC5301　中枢塔内部中Boss战斗地图１\n'),
            TXT(0x08, 'BC5302　中枢塔内部中Boss战斗地图２\n'),
            TXT(0x09, 'BC5303　中枢塔内部顶上战斗地图 莱维\n'),
            TXT(0x0A, 'BC5304　中枢塔内部高速升降梯战斗地图 德尔基昂\n'),
            TXT(0x0B, 'BC5305　中枢塔内部Boss战斗地图１（通常空间）怀斯曼\n'),
            TXT(0x0C, 'BC5306　中枢塔内部Boss战斗地图２（异空间）本Boss第二形态\n'),
            TXT(0x0D, 'BC5100　中枢塔前通路\n'),
            TXT(0x0E, 'BC5801　辉之环居住区外侧\n'),
            TXT(0x0F, 'BC5700　辉之环工场区古罗力亚斯前\n'),
            TXT(0x10, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_11CF'),
        (0x00000001, 'loc_11DF'),
        (0x00000002, 'loc_11EF'),
        (0x00000003, 'loc_11FF'),
        (0x00000004, 'loc_120F'),
        (0x00000005, 'loc_121F'),
        (0x00000006, 'loc_122F'),
        (0x00000007, 'loc_123F'),
        (0x00000008, 'loc_124F'),
        (0x00000009, 'loc_125F'),
        (0x0000000A, 'loc_126F'),
        (0x0000000B, 'loc_127F'),
        (0x0000000C, 'loc_128F'),
        (0x0000000D, 'loc_129F'),
        (0x0000000E, 'loc_12AF'),
        (0x0000000F, 'loc_12BF'),
        (-1, 'loc_12CF'),
    )

    def _loc_11CF(): pass

    label('loc_11CF')

    Battle(0x0000050B, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_12D9')

    def _loc_11DF(): pass

    label('loc_11DF')

    Battle(0x00000518, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_12D9')

    def _loc_11EF(): pass

    label('loc_11EF')

    Battle(0x0000043A, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_12D9')

    def _loc_11FF(): pass

    label('loc_11FF')

    Battle(0x00000440, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_12D9')

    def _loc_120F(): pass

    label('loc_120F')

    Battle(0x00000449, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_12D9')

    def _loc_121F(): pass

    label('loc_121F')

    Battle(0x0000043D, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_12D9')

    def _loc_122F(): pass

    label('loc_122F')

    Battle(0x00000508, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_12D9')

    def _loc_123F(): pass

    label('loc_123F')

    Battle(0x00000509, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_12D9')

    def _loc_124F(): pass

    label('loc_124F')

    Battle(0x0000050A, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_12D9')

    def _loc_125F(): pass

    label('loc_125F')

    Battle(0x00000458, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_12D9')

    def _loc_126F(): pass

    label('loc_126F')

    Battle(0x00000450, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_12D9')

    def _loc_127F(): pass

    label('loc_127F')

    Battle(0x00000459, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_12D9')

    def _loc_128F(): pass

    label('loc_128F')

    Battle(0x00000452, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_12D9')

    def _loc_129F(): pass

    label('loc_129F')

    Battle(0x00000525, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_12D9')

    def _loc_12AF(): pass

    label('loc_12AF')

    Battle(0x0000050E, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_12D9')

    def _loc_12BF(): pass

    label('loc_12BF')

    Battle(0x00000514, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_12D9')

    def _loc_12CF(): pass

    label('loc_12CF')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_12D9(): pass

    label('loc_12D9')

    Jump('func_0A_EF6')

    def _loc_12DC(): pass

    label('loc_12DC')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x000B offset: 0x12EA
@scena.Code('func_0B_12EA')
def func_0B_12EA():
    Return()

# id: 0x000C offset: 0x12EB
@scena.Code('func_0C_12EB')
def func_0C_12EB():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_137B',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'C0100_01\n'),
            TXT(0x01, 'C0100_02\n'),
            TXT(0x02, 'C0100_03\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_133E'),
        (0x00000001, 'loc_134E'),
        (0x00000002, 'loc_135E'),
        (-1, 'loc_136E'),
    )

    def _loc_133E(): pass

    label('loc_133E')

    Battle(0x00000056, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1378')

    def _loc_134E(): pass

    label('loc_134E')

    Battle(0x00000057, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1378')

    def _loc_135E(): pass

    label('loc_135E')

    Battle(0x00000058, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1378')

    def _loc_136E(): pass

    label('loc_136E')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1378(): pass

    label('loc_1378')

    Jump('func_0C_12EB')

    def _loc_137B(): pass

    label('loc_137B')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x000D offset: 0x1389
@scena.Code('func_0D_1389')
def func_0D_1389():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1474',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'C0100_01\n'),
            TXT(0x01, 'C0100_02\n'),
            TXT(0x02, 'C0100_03\n'),
            TXT(0x03, 'C0100_20\n'),
            TXT(0x04, 'C0100_11\n'),
            TXT(0x05, 'BTL_EVENT001\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1407'),
        (0x00000001, 'loc_1417'),
        (0x00000002, 'loc_1427'),
        (0x00000003, 'loc_1437'),
        (0x00000004, 'loc_1447'),
        (0x00000005, 'loc_1457'),
        (-1, 'loc_1467'),
    )

    def _loc_1407(): pass

    label('loc_1407')

    Battle(0x0000003E, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1471')

    def _loc_1417(): pass

    label('loc_1417')

    Battle(0x0000003F, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1471')

    def _loc_1427(): pass

    label('loc_1427')

    Battle(0x00000040, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1471')

    def _loc_1437(): pass

    label('loc_1437')

    Battle(0x00000051, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1471')

    def _loc_1447(): pass

    label('loc_1447')

    Battle(0x00000048, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1471')

    def _loc_1457(): pass

    label('loc_1457')

    Battle(0x0000076D, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1471')

    def _loc_1467(): pass

    label('loc_1467')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1471(): pass

    label('loc_1471')

    Jump('func_0D_1389')

    def _loc_1474(): pass

    label('loc_1474')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x000E offset: 0x1482
@scena.Code('func_0E_1482')
def func_0E_1482():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1559',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'C0400_01\n'),
            TXT(0x01, 'C0400_02\n'),
            TXT(0x02, 'C0400_07\n'),
            TXT(0x03, 'C0400_13\n'),
            TXT(0x04, 'C0400_10\n'),
            TXT(0x05, 'BTL_EVENT002\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_14FC'),
        (0x00000001, 'loc_150C'),
        (0x00000002, 'loc_151C'),
        (0x00000003, 'loc_152C'),
        (0x00000004, 'loc_153C'),
        (-1, 'loc_154C'),
    )

    def _loc_14FC(): pass

    label('loc_14FC')

    Battle(0x00000031, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1556')

    def _loc_150C(): pass

    label('loc_150C')

    Battle(0x00000032, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1556')

    def _loc_151C(): pass

    label('loc_151C')

    Battle(0x00000037, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1556')

    def _loc_152C(): pass

    label('loc_152C')

    Battle(0x0000003D, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1556')

    def _loc_153C(): pass

    label('loc_153C')

    Battle(0x0000003A, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1556')

    def _loc_154C(): pass

    label('loc_154C')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1556(): pass

    label('loc_1556')

    Jump('func_0E_1482')

    def _loc_1559(): pass

    label('loc_1559')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x000F offset: 0x1567
@scena.Code('func_0F_1567')
def func_0F_1567():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1631',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'R0100_02\n'),
            TXT(0x01, 'R0100_05\n'),
            TXT(0x02, 'R0100_09\n'),
            TXT(0x03, 'R0100_11\n'),
            TXT(0x04, 'R0100_14\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_15D4'),
        (0x00000001, 'loc_15E4'),
        (0x00000002, 'loc_15F4'),
        (0x00000003, 'loc_1604'),
        (0x00000004, 'loc_1614'),
        (-1, 'loc_1624'),
    )

    def _loc_15D4(): pass

    label('loc_15D4')

    Battle(0x00000015, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_162E')

    def _loc_15E4(): pass

    label('loc_15E4')

    Battle(0x00000018, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_162E')

    def _loc_15F4(): pass

    label('loc_15F4')

    Battle(0x0000001C, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_162E')

    def _loc_1604(): pass

    label('loc_1604')

    Battle(0x0000001E, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_162E')

    def _loc_1614(): pass

    label('loc_1614')

    Battle(0x00000021, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_162E')

    def _loc_1624(): pass

    label('loc_1624')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_162E(): pass

    label('loc_162E')

    Jump('func_0F_1567')

    def _loc_1631(): pass

    label('loc_1631')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0010 offset: 0x163F
@scena.Code('func_10_163F')
def func_10_163F():
    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0011 offset: 0x164D
@scena.Code('func_11_164D')
def func_11_164D():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1717',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'R0300_02\n'),
            TXT(0x01, 'R0300_06\n'),
            TXT(0x02, 'R0300_09\n'),
            TXT(0x03, 'R0300_12\n'),
            TXT(0x04, 'R0300_17\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_16BA'),
        (0x00000001, 'loc_16CA'),
        (0x00000002, 'loc_16DA'),
        (0x00000003, 'loc_16EA'),
        (0x00000004, 'loc_16FA'),
        (-1, 'loc_170A'),
    )

    def _loc_16BA(): pass

    label('loc_16BA')

    Battle(0x00000065, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1714')

    def _loc_16CA(): pass

    label('loc_16CA')

    Battle(0x00000069, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1714')

    def _loc_16DA(): pass

    label('loc_16DA')

    Battle(0x0000006C, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1714')

    def _loc_16EA(): pass

    label('loc_16EA')

    Battle(0x0000006F, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1714')

    def _loc_16FA(): pass

    label('loc_16FA')

    Battle(0x00000074, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1714')

    def _loc_170A(): pass

    label('loc_170A')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1714(): pass

    label('loc_1714')

    Jump('func_11_164D')

    def _loc_1717(): pass

    label('loc_1717')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0012 offset: 0x1725
@scena.Code('func_12_1725')
def func_12_1725():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_17EF',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'C0500_01\n'),
            TXT(0x01, 'C0500_02\n'),
            TXT(0x02, 'C0500_03\n'),
            TXT(0x03, 'C0500_04\n'),
            TXT(0x04, 'C0500_07\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1792'),
        (0x00000001, 'loc_17A2'),
        (0x00000002, 'loc_17B2'),
        (0x00000003, 'loc_17C2'),
        (0x00000004, 'loc_17D2'),
        (-1, 'loc_17E2'),
    )

    def _loc_1792(): pass

    label('loc_1792')

    Battle(0x0000002A, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_17EC')

    def _loc_17A2(): pass

    label('loc_17A2')

    Battle(0x0000002B, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_17EC')

    def _loc_17B2(): pass

    label('loc_17B2')

    Battle(0x0000002C, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_17EC')

    def _loc_17C2(): pass

    label('loc_17C2')

    Battle(0x0000002D, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_17EC')

    def _loc_17D2(): pass

    label('loc_17D2')

    Battle(0x00000030, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_17EC')

    def _loc_17E2(): pass

    label('loc_17E2')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_17EC(): pass

    label('loc_17EC')

    Jump('func_12_1725')

    def _loc_17EF(): pass

    label('loc_17EF')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0013 offset: 0x17FD
@scena.Code('func_13_17FD')
def func_13_17FD():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_18C7',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'C1300_01\n'),
            TXT(0x01, 'C1300_02\n'),
            TXT(0x02, 'C1300_03\n'),
            TXT(0x03, 'C1300_04\n'),
            TXT(0x04, 'C1300_05\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_186A'),
        (0x00000001, 'loc_187A'),
        (0x00000002, 'loc_188A'),
        (0x00000003, 'loc_189A'),
        (0x00000004, 'loc_18AA'),
        (-1, 'loc_18BA'),
    )

    def _loc_186A(): pass

    label('loc_186A')

    Battle(0x000000A1, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_18C4')

    def _loc_187A(): pass

    label('loc_187A')

    Battle(0x000000A2, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_18C4')

    def _loc_188A(): pass

    label('loc_188A')

    Battle(0x000000A3, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_18C4')

    def _loc_189A(): pass

    label('loc_189A')

    Battle(0x000000A4, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_18C4')

    def _loc_18AA(): pass

    label('loc_18AA')

    Battle(0x000000A5, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_18C4')

    def _loc_18BA(): pass

    label('loc_18BA')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_18C4(): pass

    label('loc_18C4')

    Jump('func_13_17FD')

    def _loc_18C7(): pass

    label('loc_18C7')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0014 offset: 0x18D5
@scena.Code('func_14_18D5')
def func_14_18D5():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_199F',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'C1400_01\n'),
            TXT(0x01, 'C1400_02\n'),
            TXT(0x02, 'C1400_03\n'),
            TXT(0x03, 'C1400_04\n'),
            TXT(0x04, 'C1400_05\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1942'),
        (0x00000001, 'loc_1952'),
        (0x00000002, 'loc_1962'),
        (0x00000003, 'loc_1972'),
        (0x00000004, 'loc_1982'),
        (-1, 'loc_1992'),
    )

    def _loc_1942(): pass

    label('loc_1942')

    Battle(0x000000B5, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_199C')

    def _loc_1952(): pass

    label('loc_1952')

    Battle(0x000000B6, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_199C')

    def _loc_1962(): pass

    label('loc_1962')

    Battle(0x000000B7, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_199C')

    def _loc_1972(): pass

    label('loc_1972')

    Battle(0x000000B8, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_199C')

    def _loc_1982(): pass

    label('loc_1982')

    Battle(0x000000B9, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_199C')

    def _loc_1992(): pass

    label('loc_1992')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_199C(): pass

    label('loc_199C')

    Jump('func_14_18D5')

    def _loc_199F(): pass

    label('loc_199F')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0015 offset: 0x19AD
@scena.Code('func_15_19AD')
def func_15_19AD():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A77',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'C1500_01\n'),
            TXT(0x01, 'C1500_02\n'),
            TXT(0x02, 'C1500_03\n'),
            TXT(0x03, 'C1500_04\n'),
            TXT(0x04, 'C1500_05\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1A1A'),
        (0x00000001, 'loc_1A2A'),
        (0x00000002, 'loc_1A3A'),
        (0x00000003, 'loc_1A4A'),
        (0x00000004, 'loc_1A5A'),
        (-1, 'loc_1A6A'),
    )

    def _loc_1A1A(): pass

    label('loc_1A1A')

    Battle(0x000000C9, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1A74')

    def _loc_1A2A(): pass

    label('loc_1A2A')

    Battle(0x000000CA, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1A74')

    def _loc_1A3A(): pass

    label('loc_1A3A')

    Battle(0x000000CB, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1A74')

    def _loc_1A4A(): pass

    label('loc_1A4A')

    Battle(0x000000CC, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1A74')

    def _loc_1A5A(): pass

    label('loc_1A5A')

    Battle(0x000000CD, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1A74')

    def _loc_1A6A(): pass

    label('loc_1A6A')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1A74(): pass

    label('loc_1A74')

    Jump('func_15_19AD')

    def _loc_1A77(): pass

    label('loc_1A77')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0016 offset: 0x1A85
@scena.Code('func_16_1A85')
def func_16_1A85():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B4F',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'R1100_01\n'),
            TXT(0x01, 'R1100_02\n'),
            TXT(0x02, 'R1100_20\n'),
            TXT(0x03, 'R1100_04\n'),
            TXT(0x04, 'R1100_05\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1AF2'),
        (0x00000001, 'loc_1B02'),
        (0x00000002, 'loc_1B12'),
        (0x00000003, 'loc_1B22'),
        (0x00000004, 'loc_1B32'),
        (-1, 'loc_1B42'),
    )

    def _loc_1AF2(): pass

    label('loc_1AF2')

    Battle(0x000000DD, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1B4C')

    def _loc_1B02(): pass

    label('loc_1B02')

    Battle(0x000000DE, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1B4C')

    def _loc_1B12(): pass

    label('loc_1B12')

    Battle(0x000000F0, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1B4C')

    def _loc_1B22(): pass

    label('loc_1B22')

    Battle(0x000000E0, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1B4C')

    def _loc_1B32(): pass

    label('loc_1B32')

    Battle(0x000000E1, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1B4C')

    def _loc_1B42(): pass

    label('loc_1B42')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1B4C(): pass

    label('loc_1B4C')

    Jump('func_16_1A85')

    def _loc_1B4F(): pass

    label('loc_1B4F')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0017 offset: 0x1B5D
@scena.Code('func_17_1B5D')
def func_17_1B5D():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1C27',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'R1200_01\n'),
            TXT(0x01, 'R1200_02\n'),
            TXT(0x02, 'R1200_03\n'),
            TXT(0x03, 'R1200_04\n'),
            TXT(0x04, 'R1200_05\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1BCA'),
        (0x00000001, 'loc_1BDA'),
        (0x00000002, 'loc_1BEA'),
        (0x00000003, 'loc_1BFA'),
        (0x00000004, 'loc_1C0A'),
        (-1, 'loc_1C1A'),
    )

    def _loc_1BCA(): pass

    label('loc_1BCA')

    Battle(0x000000F1, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1C24')

    def _loc_1BDA(): pass

    label('loc_1BDA')

    Battle(0x000000F2, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1C24')

    def _loc_1BEA(): pass

    label('loc_1BEA')

    Battle(0x000000F3, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1C24')

    def _loc_1BFA(): pass

    label('loc_1BFA')

    Battle(0x000000F4, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1C24')

    def _loc_1C0A(): pass

    label('loc_1C0A')

    Battle(0x000000F5, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1C24')

    def _loc_1C1A(): pass

    label('loc_1C1A')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1C24(): pass

    label('loc_1C24')

    Jump('func_17_1B5D')

    def _loc_1C27(): pass

    label('loc_1C27')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0018 offset: 0x1C35
@scena.Code('func_18_1C35')
def func_18_1C35():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1CFF',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'R1300_01\n'),
            TXT(0x01, 'R1300_02\n'),
            TXT(0x02, 'R1300_03\n'),
            TXT(0x03, 'R1300_04\n'),
            TXT(0x04, 'R1300_05\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1CA2'),
        (0x00000001, 'loc_1CB2'),
        (0x00000002, 'loc_1CC2'),
        (0x00000003, 'loc_1CD2'),
        (0x00000004, 'loc_1CE2'),
        (-1, 'loc_1CF2'),
    )

    def _loc_1CA2(): pass

    label('loc_1CA2')

    Battle(0x00000105, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1CFC')

    def _loc_1CB2(): pass

    label('loc_1CB2')

    Battle(0x00000106, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1CFC')

    def _loc_1CC2(): pass

    label('loc_1CC2')

    Battle(0x00000107, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1CFC')

    def _loc_1CD2(): pass

    label('loc_1CD2')

    Battle(0x00000108, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1CFC')

    def _loc_1CE2(): pass

    label('loc_1CE2')

    Battle(0x00000109, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1CFC')

    def _loc_1CF2(): pass

    label('loc_1CF2')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1CFC(): pass

    label('loc_1CFC')

    Jump('func_18_1C35')

    def _loc_1CFF(): pass

    label('loc_1CFF')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0019 offset: 0x1D0D
@scena.Code('func_19_1D0D')
def func_19_1D0D():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1DD7',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'R1400_01\n'),
            TXT(0x01, 'R1400_02\n'),
            TXT(0x02, 'R1400_03\n'),
            TXT(0x03, 'R1400_04\n'),
            TXT(0x04, 'R1400_05\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1D7A'),
        (0x00000001, 'loc_1D8A'),
        (0x00000002, 'loc_1D9A'),
        (0x00000003, 'loc_1DAA'),
        (0x00000004, 'loc_1DBA'),
        (-1, 'loc_1DCA'),
    )

    def _loc_1D7A(): pass

    label('loc_1D7A')

    Battle(0x00000119, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1DD4')

    def _loc_1D8A(): pass

    label('loc_1D8A')

    Battle(0x0000011A, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1DD4')

    def _loc_1D9A(): pass

    label('loc_1D9A')

    Battle(0x0000011B, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1DD4')

    def _loc_1DAA(): pass

    label('loc_1DAA')

    Battle(0x0000011C, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1DD4')

    def _loc_1DBA(): pass

    label('loc_1DBA')

    Battle(0x0000011D, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1DD4')

    def _loc_1DCA(): pass

    label('loc_1DCA')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1DD4(): pass

    label('loc_1DD4')

    Jump('func_19_1D0D')

    def _loc_1DD7(): pass

    label('loc_1DD7')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x001A offset: 0x1DE5
@scena.Code('func_1A_1DE5')
def func_1A_1DE5():
    Return()

# id: 0x001B offset: 0x1DE6
@scena.Code('func_1B_1DE6')
def func_1B_1DE6():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1EB0',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'C1100_01\n'),
            TXT(0x01, 'C1100_02\n'),
            TXT(0x02, 'C1100_03\n'),
            TXT(0x03, 'C1100_04\n'),
            TXT(0x04, 'C1100_05\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1E53'),
        (0x00000001, 'loc_1E63'),
        (0x00000002, 'loc_1E73'),
        (0x00000003, 'loc_1E83'),
        (0x00000004, 'loc_1E93'),
        (-1, 'loc_1EA3'),
    )

    def _loc_1E53(): pass

    label('loc_1E53')

    Battle(0x00000141, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1EAD')

    def _loc_1E63(): pass

    label('loc_1E63')

    Battle(0x00000142, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1EAD')

    def _loc_1E73(): pass

    label('loc_1E73')

    Battle(0x00000143, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1EAD')

    def _loc_1E83(): pass

    label('loc_1E83')

    Battle(0x00000144, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1EAD')

    def _loc_1E93(): pass

    label('loc_1E93')

    Battle(0x00000145, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1EAD')

    def _loc_1EA3(): pass

    label('loc_1EA3')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1EAD(): pass

    label('loc_1EAD')

    Jump('func_1B_1DE6')

    def _loc_1EB0(): pass

    label('loc_1EB0')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x001C offset: 0x1EBE
@scena.Code('func_1C_1EBE')
def func_1C_1EBE():
    Return()

# id: 0x001D offset: 0x1EBF
@scena.Code('func_1D_1EBF')
def func_1D_1EBF():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1F89',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'R2100_01\n'),
            TXT(0x01, 'R2100_02\n'),
            TXT(0x02, 'R2100_03\n'),
            TXT(0x03, 'R2100_04\n'),
            TXT(0x04, 'R2100_05\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1F2C'),
        (0x00000001, 'loc_1F3C'),
        (0x00000002, 'loc_1F4C'),
        (0x00000003, 'loc_1F5C'),
        (0x00000004, 'loc_1F6C'),
        (-1, 'loc_1F7C'),
    )

    def _loc_1F2C(): pass

    label('loc_1F2C')

    Battle(0x00000169, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1F86')

    def _loc_1F3C(): pass

    label('loc_1F3C')

    Battle(0x0000016A, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1F86')

    def _loc_1F4C(): pass

    label('loc_1F4C')

    Battle(0x0000016B, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1F86')

    def _loc_1F5C(): pass

    label('loc_1F5C')

    Battle(0x0000016C, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1F86')

    def _loc_1F6C(): pass

    label('loc_1F6C')

    Battle(0x0000016D, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1F86')

    def _loc_1F7C(): pass

    label('loc_1F7C')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1F86(): pass

    label('loc_1F86')

    Jump('func_1D_1EBF')

    def _loc_1F89(): pass

    label('loc_1F89')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x001E offset: 0x1F97
@scena.Code('func_1E_1F97')
def func_1E_1F97():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_20DC',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'R2200_01主场景\n'),
            TXT(0x01, 'R2200_02\n'),
            TXT(0x02, 'R2201_01沙滩\n'),
            TXT(0x03, 'R2201_02\n'),
            TXT(0x04, 'R2202_01主场景（黄昏）\n'),
            TXT(0x05, 'R2202_02\n'),
            TXT(0x06, 'R2203_01沙滩（黄昏）\n'),
            TXT(0x07, 'R2203_02\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_204F'),
        (0x00000001, 'loc_205F'),
        (0x00000002, 'loc_206F'),
        (0x00000003, 'loc_207F'),
        (0x00000004, 'loc_208F'),
        (0x00000005, 'loc_209F'),
        (0x00000006, 'loc_20AF'),
        (0x00000007, 'loc_20BF'),
        (-1, 'loc_20CF'),
    )

    def _loc_204F(): pass

    label('loc_204F')

    Battle(0x0000017D, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_20D9')

    def _loc_205F(): pass

    label('loc_205F')

    Battle(0x0000017E, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_20D9')

    def _loc_206F(): pass

    label('loc_206F')

    Battle(0x00000187, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_20D9')

    def _loc_207F(): pass

    label('loc_207F')

    Battle(0x00000188, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_20D9')

    def _loc_208F(): pass

    label('loc_208F')

    Battle(0x00000321, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_20D9')

    def _loc_209F(): pass

    label('loc_209F')

    Battle(0x00000322, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_20D9')

    def _loc_20AF(): pass

    label('loc_20AF')

    Battle(0x0000032B, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_20D9')

    def _loc_20BF(): pass

    label('loc_20BF')

    Battle(0x0000032C, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_20D9')

    def _loc_20CF(): pass

    label('loc_20CF')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_20D9(): pass

    label('loc_20D9')

    Jump('func_1E_1F97')

    def _loc_20DC(): pass

    label('loc_20DC')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x001F offset: 0x20EA
@scena.Code('func_1F_20EA')
def func_1F_20EA():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_226D',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'R2300_01\n'),
            TXT(0x01, 'R2300_02\n'),
            TXT(0x02, 'R2300_03\n'),
            TXT(0x03, 'R2300_04\n'),
            TXT(0x04, 'R2300_05\n'),
            TXT(0x05, 'R2301_01（黄昏）\n'),
            TXT(0x06, 'R2301_02（黄昏）\n'),
            TXT(0x07, 'R2301_03（黄昏）\n'),
            TXT(0x08, 'R2301_04（黄昏）\n'),
            TXT(0x09, 'R2301_05（黄昏）\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_21C0'),
        (0x00000001, 'loc_21D0'),
        (0x00000002, 'loc_21E0'),
        (0x00000003, 'loc_21F0'),
        (0x00000004, 'loc_2200'),
        (0x00000005, 'loc_2210'),
        (0x00000006, 'loc_2220'),
        (0x00000007, 'loc_2230'),
        (0x00000008, 'loc_2240'),
        (0x00000009, 'loc_2250'),
        (-1, 'loc_2260'),
    )

    def _loc_21C0(): pass

    label('loc_21C0')

    Battle(0x00000191, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_226A')

    def _loc_21D0(): pass

    label('loc_21D0')

    Battle(0x00000192, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_226A')

    def _loc_21E0(): pass

    label('loc_21E0')

    Battle(0x00000193, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_226A')

    def _loc_21F0(): pass

    label('loc_21F0')

    Battle(0x00000194, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_226A')

    def _loc_2200(): pass

    label('loc_2200')

    Battle(0x00000195, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_226A')

    def _loc_2210(): pass

    label('loc_2210')

    Battle(0x00000335, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_226A')

    def _loc_2220(): pass

    label('loc_2220')

    Battle(0x00000336, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_226A')

    def _loc_2230(): pass

    label('loc_2230')

    Battle(0x00000337, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_226A')

    def _loc_2240(): pass

    label('loc_2240')

    Battle(0x00000338, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_226A')

    def _loc_2250(): pass

    label('loc_2250')

    Battle(0x00000339, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_226A')

    def _loc_2260(): pass

    label('loc_2260')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_226A(): pass

    label('loc_226A')

    Jump('func_1F_20EA')

    def _loc_226D(): pass

    label('loc_226D')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0020 offset: 0x227B
@scena.Code('func_20_227B')
def func_20_227B():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2345',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'R2400_01\n'),
            TXT(0x01, 'R2400_02\n'),
            TXT(0x02, 'R2400_03\n'),
            TXT(0x03, 'R2400_04\n'),
            TXT(0x04, 'R2400_05\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_22E8'),
        (0x00000001, 'loc_22F8'),
        (0x00000002, 'loc_2308'),
        (0x00000003, 'loc_2318'),
        (0x00000004, 'loc_2328'),
        (-1, 'loc_2338'),
    )

    def _loc_22E8(): pass

    label('loc_22E8')

    Battle(0x000001A5, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2342')

    def _loc_22F8(): pass

    label('loc_22F8')

    Battle(0x000001A6, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2342')

    def _loc_2308(): pass

    label('loc_2308')

    Battle(0x000001A7, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2342')

    def _loc_2318(): pass

    label('loc_2318')

    Battle(0x000001A8, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2342')

    def _loc_2328(): pass

    label('loc_2328')

    Battle(0x000001A9, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2342')

    def _loc_2338(): pass

    label('loc_2338')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2342(): pass

    label('loc_2342')

    Jump('func_20_227B')

    def _loc_2345(): pass

    label('loc_2345')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0021 offset: 0x2353
@scena.Code('func_21_2353')
def func_21_2353():
    Return()

# id: 0x0022 offset: 0x2354
@scena.Code('func_22_2354')
def func_22_2354():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2435',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'BTL_EVENT011（迪恩）\n'),
            TXT(0x01, 'BTL_EVENT012（雷斯）\n'),
            TXT(0x02, 'BTL_EVENT013（洛克）\n'),
            TXT(0x03, 'BTL_EVENT014（黑衣男子）\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_23E8'),
        (0x00000001, 'loc_23F8'),
        (0x00000002, 'loc_2408'),
        (0x00000003, 'loc_2418'),
        (-1, 'loc_2428'),
    )

    def _loc_23E8(): pass

    label('loc_23E8')

    Battle(0x00000777, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2432')

    def _loc_23F8(): pass

    label('loc_23F8')

    Battle(0x00000778, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2432')

    def _loc_2408(): pass

    label('loc_2408')

    Battle(0x00000779, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2432')

    def _loc_2418(): pass

    label('loc_2418')

    Battle(0x0000077A, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2432')

    def _loc_2428(): pass

    label('loc_2428')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2432(): pass

    label('loc_2432')

    Jump('func_22_2354')

    def _loc_2435(): pass

    label('loc_2435')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0023 offset: 0x2443
@scena.Code('func_23_2443')
def func_23_2443():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_254A',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        2,
        10,
        80,
        1,
        (
            TXT(0x00, '卡鲁迪亚隧道\n'),
            TXT(0x01, '卡鲁迪亚钟乳洞\n'),
            TXT(0x02, '红莲之塔\n'),
            TXT(0x03, '托兰特平原道\n'),
            TXT(0x04, '利塔街道\n'),
            TXT(0x05, '佐达特军用道\n'),
            TXT(0x06, '雷斯顿水上要塞\n'),
            TXT(0x07, '红莲之塔（事件）\n'),
            TXT(0x08, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_24FC'),
        (0x00000001, 'loc_2503'),
        (0x00000002, 'loc_250A'),
        (0x00000003, 'loc_2511'),
        (0x00000004, 'loc_2518'),
        (0x00000005, 'loc_251F'),
        (0x00000006, 'loc_2526'),
        (0x00000007, 'loc_252D'),
        (-1, 'loc_253D'),
    )

    def _loc_24FC(): pass

    label('loc_24FC')

    Call(2, 0x0024)

    Jump('loc_2547')

    def _loc_2503(): pass

    label('loc_2503')

    Call(2, 0x0025)

    Jump('loc_2547')

    def _loc_250A(): pass

    label('loc_250A')

    Call(2, 0x0026)

    Jump('loc_2547')

    def _loc_2511(): pass

    label('loc_2511')

    Call(2, 0x0027)

    Jump('loc_2547')

    def _loc_2518(): pass

    label('loc_2518')

    Call(2, 0x0028)

    Jump('loc_2547')

    def _loc_251F(): pass

    label('loc_251F')

    Call(2, 0x0029)

    Jump('loc_2547')

    def _loc_2526(): pass

    label('loc_2526')

    Call(2, 0x002A)

    Jump('loc_2547')

    def _loc_252D(): pass

    label('loc_252D')

    Battle(0x00000788, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2547')

    def _loc_253D(): pass

    label('loc_253D')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2547(): pass

    label('loc_2547')

    Jump('func_23_2443')

    def _loc_254A(): pass

    label('loc_254A')

    OP_5F(0x0002)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0024 offset: 0x2558
@scena.Code('func_24_2558')
def func_24_2558():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2605',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'R3400_01\n'),
            TXT(0x01, 'R3400_02\n'),
            TXT(0x02, 'R3400_03\n'),
            TXT(0x03, 'R3400_04\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_25B8'),
        (0x00000001, 'loc_25C8'),
        (0x00000002, 'loc_25D8'),
        (0x00000003, 'loc_25E8'),
        (-1, 'loc_25F8'),
    )

    def _loc_25B8(): pass

    label('loc_25B8')

    Battle(0x000001CD, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2602')

    def _loc_25C8(): pass

    label('loc_25C8')

    Battle(0x000001CE, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2602')

    def _loc_25D8(): pass

    label('loc_25D8')

    Battle(0x000001CF, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2602')

    def _loc_25E8(): pass

    label('loc_25E8')

    Battle(0x000001D0, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2602')

    def _loc_25F8(): pass

    label('loc_25F8')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2602(): pass

    label('loc_2602')

    Jump('func_24_2558')

    def _loc_2605(): pass

    label('loc_2605')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0025 offset: 0x2613
@scena.Code('func_25_2613')
def func_25_2613():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2738',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'C3300_01\n'),
            TXT(0x01, 'C3300_02\n'),
            TXT(0x02, 'C3300_03\n'),
            TXT(0x03, 'C3300_04\n'),
            TXT(0x04, 'C3300_05\n'),
            TXT(0x05, 'C3300_06\n'),
            TXT(0x06, 'C3300_07\n'),
            TXT(0x07, 'BTL_EVENT020\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_26AB'),
        (0x00000001, 'loc_26BB'),
        (0x00000002, 'loc_26CB'),
        (0x00000003, 'loc_26DB'),
        (0x00000004, 'loc_26EB'),
        (0x00000005, 'loc_26FB'),
        (0x00000006, 'loc_270B'),
        (0x00000007, 'loc_271B'),
        (-1, 'loc_272B'),
    )

    def _loc_26AB(): pass

    label('loc_26AB')

    Battle(0x000001E1, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2735')

    def _loc_26BB(): pass

    label('loc_26BB')

    Battle(0x000001E2, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2735')

    def _loc_26CB(): pass

    label('loc_26CB')

    Battle(0x000001E3, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2735')

    def _loc_26DB(): pass

    label('loc_26DB')

    Battle(0x000001E4, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2735')

    def _loc_26EB(): pass

    label('loc_26EB')

    Battle(0x000001E5, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2735')

    def _loc_26FB(): pass

    label('loc_26FB')

    Battle(0x000001E6, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2735')

    def _loc_270B(): pass

    label('loc_270B')

    Battle(0x000001E7, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2735')

    def _loc_271B(): pass

    label('loc_271B')

    Battle(0x00000780, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2735')

    def _loc_272B(): pass

    label('loc_272B')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2735(): pass

    label('loc_2735')

    Jump('func_25_2613')

    def _loc_2738(): pass

    label('loc_2738')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0026 offset: 0x2746
@scena.Code('func_26_2746')
def func_26_2746():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2810',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'C3511_01\n'),
            TXT(0x01, 'C3511_02\n'),
            TXT(0x02, 'C3511_03\n'),
            TXT(0x03, 'C3511_04\n'),
            TXT(0x04, 'C3511_05\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_27B3'),
        (0x00000001, 'loc_27C3'),
        (0x00000002, 'loc_27D3'),
        (0x00000003, 'loc_27E3'),
        (0x00000004, 'loc_27F3'),
        (-1, 'loc_2803'),
    )

    def _loc_27B3(): pass

    label('loc_27B3')

    Battle(0x000001F5, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_280D')

    def _loc_27C3(): pass

    label('loc_27C3')

    Battle(0x000001F6, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_280D')

    def _loc_27D3(): pass

    label('loc_27D3')

    Battle(0x000001F7, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_280D')

    def _loc_27E3(): pass

    label('loc_27E3')

    Battle(0x000001F8, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_280D')

    def _loc_27F3(): pass

    label('loc_27F3')

    Battle(0x000001F9, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_280D')

    def _loc_2803(): pass

    label('loc_2803')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_280D(): pass

    label('loc_280D')

    Jump('func_26_2746')

    def _loc_2810(): pass

    label('loc_2810')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0027 offset: 0x281E
@scena.Code('func_27_281E')
def func_27_281E():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2979',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'R3100_01\n'),
            TXT(0x01, 'R3100_02\n'),
            TXT(0x02, 'R3100_03\n'),
            TXT(0x03, 'R3100_04\n'),
            TXT(0x04, 'R3101_05\n'),
            TXT(0x05, 'R3101_01\n'),
            TXT(0x06, 'R3101_02\n'),
            TXT(0x07, 'R3101_03\n'),
            TXT(0x08, 'R3101_04\n'),
            TXT(0x09, 'R3101_05\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_28CC'),
        (0x00000001, 'loc_28DC'),
        (0x00000002, 'loc_28EC'),
        (0x00000003, 'loc_28FC'),
        (0x00000004, 'loc_290C'),
        (0x00000005, 'loc_291C'),
        (0x00000006, 'loc_292C'),
        (0x00000007, 'loc_293C'),
        (0x00000008, 'loc_294C'),
        (0x00000009, 'loc_295C'),
        (-1, 'loc_296C'),
    )

    def _loc_28CC(): pass

    label('loc_28CC')

    Battle(0x00000209, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2976')

    def _loc_28DC(): pass

    label('loc_28DC')

    Battle(0x0000020A, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2976')

    def _loc_28EC(): pass

    label('loc_28EC')

    Battle(0x0000020B, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2976')

    def _loc_28FC(): pass

    label('loc_28FC')

    Battle(0x0000020C, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2976')

    def _loc_290C(): pass

    label('loc_290C')

    Battle(0x0000020D, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2976')

    def _loc_291C(): pass

    label('loc_291C')

    Battle(0x00000349, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2976')

    def _loc_292C(): pass

    label('loc_292C')

    Battle(0x0000034A, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2976')

    def _loc_293C(): pass

    label('loc_293C')

    Battle(0x0000034B, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2976')

    def _loc_294C(): pass

    label('loc_294C')

    Battle(0x0000034C, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2976')

    def _loc_295C(): pass

    label('loc_295C')

    Battle(0x0000034D, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2976')

    def _loc_296C(): pass

    label('loc_296C')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2976(): pass

    label('loc_2976')

    Jump('func_27_281E')

    def _loc_2979(): pass

    label('loc_2979')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0028 offset: 0x2987
@scena.Code('func_28_2987')
def func_28_2987():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2A51',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'R3200_01\n'),
            TXT(0x01, 'R3200_02\n'),
            TXT(0x02, 'R3200_03\n'),
            TXT(0x03, 'R3200_04\n'),
            TXT(0x04, 'R3200_05\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_29F4'),
        (0x00000001, 'loc_2A04'),
        (0x00000002, 'loc_2A14'),
        (0x00000003, 'loc_2A24'),
        (0x00000004, 'loc_2A34'),
        (-1, 'loc_2A44'),
    )

    def _loc_29F4(): pass

    label('loc_29F4')

    Battle(0x0000021D, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2A4E')

    def _loc_2A04(): pass

    label('loc_2A04')

    Battle(0x0000021E, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2A4E')

    def _loc_2A14(): pass

    label('loc_2A14')

    Battle(0x0000021F, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2A4E')

    def _loc_2A24(): pass

    label('loc_2A24')

    Battle(0x00000220, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2A4E')

    def _loc_2A34(): pass

    label('loc_2A34')

    Battle(0x00000221, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2A4E')

    def _loc_2A44(): pass

    label('loc_2A44')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2A4E(): pass

    label('loc_2A4E')

    Jump('func_28_2987')

    def _loc_2A51(): pass

    label('loc_2A51')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0029 offset: 0x2A5F
@scena.Code('func_29_2A5F')
def func_29_2A5F():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2B29',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'R3300_01\n'),
            TXT(0x01, 'R3300_02\n'),
            TXT(0x02, 'R3300_03\n'),
            TXT(0x03, 'R3300_04\n'),
            TXT(0x04, 'R3300_05\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2ACC'),
        (0x00000001, 'loc_2ADC'),
        (0x00000002, 'loc_2AEC'),
        (0x00000003, 'loc_2AFC'),
        (0x00000004, 'loc_2B0C'),
        (-1, 'loc_2B1C'),
    )

    def _loc_2ACC(): pass

    label('loc_2ACC')

    Battle(0x00000231, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2B26')

    def _loc_2ADC(): pass

    label('loc_2ADC')

    Battle(0x00000232, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2B26')

    def _loc_2AEC(): pass

    label('loc_2AEC')

    Battle(0x00000233, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2B26')

    def _loc_2AFC(): pass

    label('loc_2AFC')

    Battle(0x00000234, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2B26')

    def _loc_2B0C(): pass

    label('loc_2B0C')

    Battle(0x00000235, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2B26')

    def _loc_2B1C(): pass

    label('loc_2B1C')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2B26(): pass

    label('loc_2B26')

    Jump('func_29_2A5F')

    def _loc_2B29(): pass

    label('loc_2B29')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x002A offset: 0x2B37
@scena.Code('func_2A_2B37')
def func_2A_2B37():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2C26',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'C3107_01\n'),
            TXT(0x01, 'C3107_02\n'),
            TXT(0x02, 'C3107_10\n'),
            TXT(0x03, 'C3107_11\n'),
            TXT(0x04, 'C3107_12\n'),
            TXT(0x05, 'C3107_14特务兵Ｃ\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2BB9'),
        (0x00000001, 'loc_2BC9'),
        (0x00000002, 'loc_2BD9'),
        (0x00000003, 'loc_2BE9'),
        (0x00000004, 'loc_2BF9'),
        (0x00000005, 'loc_2C09'),
        (-1, 'loc_2C19'),
    )

    def _loc_2BB9(): pass

    label('loc_2BB9')

    Battle(0x00000245, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2C23')

    def _loc_2BC9(): pass

    label('loc_2BC9')

    Battle(0x00000246, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2C23')

    def _loc_2BD9(): pass

    label('loc_2BD9')

    Battle(0x0000024E, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2C23')

    def _loc_2BE9(): pass

    label('loc_2BE9')

    Battle(0x0000024F, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2C23')

    def _loc_2BF9(): pass

    label('loc_2BF9')

    Battle(0x00000250, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2C23')

    def _loc_2C09(): pass

    label('loc_2C09')

    Battle(0x00000252, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2C23')

    def _loc_2C19(): pass

    label('loc_2C19')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2C23(): pass

    label('loc_2C23')

    Jump('func_2A_2B37')

    def _loc_2C26(): pass

    label('loc_2C26')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x002B offset: 0x2C34
@scena.Code('func_2B_2C34')
def func_2B_2C34():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2D68',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        2,
        10,
        80,
        1,
        (
            TXT(0x00, '艾尔贝周游道\n'),
            TXT(0x01, '下水道\n'),
            TXT(0x02, '封印区域\n'),
            TXT(0x03, '庭园大道\n'),
            TXT(0x04, '艾尔贝离宫外部  中庭，回廊（夜晚）\n'),
            TXT(0x05, '艾尔贝离宫外部  内部（夜晚）\n'),
            TXT(0x06, '格兰赛尔城内部，中庭，女王宫内\n'),
            TXT(0x07, '格兰赛尔城内部，空中庭园\n'),
            TXT(0x08, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2D23'),
        (0x00000001, 'loc_2D2A'),
        (0x00000002, 'loc_2D31'),
        (0x00000003, 'loc_2D38'),
        (0x00000004, 'loc_2D3F'),
        (0x00000005, 'loc_2D46'),
        (0x00000006, 'loc_2D4D'),
        (0x00000007, 'loc_2D54'),
        (-1, 'loc_2D5B'),
    )

    def _loc_2D23(): pass

    label('loc_2D23')

    Call(2, 0x002C)

    Jump('loc_2D65')

    def _loc_2D2A(): pass

    label('loc_2D2A')

    Call(2, 0x002D)

    Jump('loc_2D65')

    def _loc_2D31(): pass

    label('loc_2D31')

    Call(2, 0x002E)

    Jump('loc_2D65')

    def _loc_2D38(): pass

    label('loc_2D38')

    Call(2, 0x002F)

    Jump('loc_2D65')

    def _loc_2D3F(): pass

    label('loc_2D3F')

    Call(2, 0x0030)

    Jump('loc_2D65')

    def _loc_2D46(): pass

    label('loc_2D46')

    Call(2, 0x0031)

    Jump('loc_2D65')

    def _loc_2D4D(): pass

    label('loc_2D4D')

    Call(2, 0x0032)

    Jump('loc_2D65')

    def _loc_2D54(): pass

    label('loc_2D54')

    Call(2, 0x0033)

    Jump('loc_2D65')

    def _loc_2D5B(): pass

    label('loc_2D5B')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2D65(): pass

    label('loc_2D65')

    Jump('func_2B_2C34')

    def _loc_2D68(): pass

    label('loc_2D68')

    OP_5F(0x0002)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x002C offset: 0x2D76
@scena.Code('func_2C_2D76')
def func_2C_2D76():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2E40',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'C4100_01\n'),
            TXT(0x01, 'C4100_02\n'),
            TXT(0x02, 'C4100_03\n'),
            TXT(0x03, 'C4100_04\n'),
            TXT(0x04, 'C4100_05\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2DE3'),
        (0x00000001, 'loc_2DF3'),
        (0x00000002, 'loc_2E03'),
        (0x00000003, 'loc_2E13'),
        (0x00000004, 'loc_2E23'),
        (-1, 'loc_2E33'),
    )

    def _loc_2DE3(): pass

    label('loc_2DE3')

    Battle(0x00000259, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2E3D')

    def _loc_2DF3(): pass

    label('loc_2DF3')

    Battle(0x0000025A, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2E3D')

    def _loc_2E03(): pass

    label('loc_2E03')

    Battle(0x0000025B, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2E3D')

    def _loc_2E13(): pass

    label('loc_2E13')

    Battle(0x0000025C, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2E3D')

    def _loc_2E23(): pass

    label('loc_2E23')

    Battle(0x0000025D, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2E3D')

    def _loc_2E33(): pass

    label('loc_2E33')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2E3D(): pass

    label('loc_2E3D')

    Jump('func_2C_2D76')

    def _loc_2E40(): pass

    label('loc_2E40')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x002D offset: 0x2E4E
@scena.Code('func_2D_2E4E')
def func_2D_2E4E():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2F8C',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'C4200_01\n'),
            TXT(0x01, 'C4200_02\n'),
            TXT(0x02, 'C4200_03\n'),
            TXT(0x03, 'C4200_04\n'),
            TXT(0x04, 'C4200_05\n'),
            TXT(0x05, 'C4200_06\n'),
            TXT(0x06, 'C4200_07\n'),
            TXT(0x07, 'C4200_08\n'),
            TXT(0x08, 'C4200_09\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2EEF'),
        (0x00000001, 'loc_2EFF'),
        (0x00000002, 'loc_2F0F'),
        (0x00000003, 'loc_2F1F'),
        (0x00000004, 'loc_2F2F'),
        (0x00000005, 'loc_2F3F'),
        (0x00000006, 'loc_2F4F'),
        (0x00000007, 'loc_2F5F'),
        (0x00000008, 'loc_2F6F'),
        (-1, 'loc_2F7F'),
    )

    def _loc_2EEF(): pass

    label('loc_2EEF')

    Battle(0x0000026D, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2F89')

    def _loc_2EFF(): pass

    label('loc_2EFF')

    Battle(0x0000026E, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2F89')

    def _loc_2F0F(): pass

    label('loc_2F0F')

    Battle(0x0000026F, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2F89')

    def _loc_2F1F(): pass

    label('loc_2F1F')

    Battle(0x00000270, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2F89')

    def _loc_2F2F(): pass

    label('loc_2F2F')

    Battle(0x00000271, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2F89')

    def _loc_2F3F(): pass

    label('loc_2F3F')

    Battle(0x00000272, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2F89')

    def _loc_2F4F(): pass

    label('loc_2F4F')

    Battle(0x00000273, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2F89')

    def _loc_2F5F(): pass

    label('loc_2F5F')

    Battle(0x00000274, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2F89')

    def _loc_2F6F(): pass

    label('loc_2F6F')

    Battle(0x00000275, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2F89')

    def _loc_2F7F(): pass

    label('loc_2F7F')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2F89(): pass

    label('loc_2F89')

    Jump('func_2D_2E4E')

    def _loc_2F8C(): pass

    label('loc_2F8C')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x002E offset: 0x2F9A
@scena.Code('func_2E_2F9A')
def func_2E_2F9A():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_30F5',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'C4300_01\n'),
            TXT(0x01, 'C4300_02\n'),
            TXT(0x02, 'C4300_03\n'),
            TXT(0x03, 'C4300_04\n'),
            TXT(0x04, 'C4300_05\n'),
            TXT(0x05, 'C4300_06\n'),
            TXT(0x06, 'C4300_07\n'),
            TXT(0x07, 'C4300_08\n'),
            TXT(0x08, 'C4300_09\n'),
            TXT(0x09, 'C4300_10\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_3048'),
        (0x00000001, 'loc_3058'),
        (0x00000002, 'loc_3068'),
        (0x00000003, 'loc_3078'),
        (0x00000004, 'loc_3088'),
        (0x00000005, 'loc_3098'),
        (0x00000006, 'loc_30A8'),
        (0x00000007, 'loc_30B8'),
        (0x00000008, 'loc_30C8'),
        (0x00000009, 'loc_30D8'),
        (-1, 'loc_30E8'),
    )

    def _loc_3048(): pass

    label('loc_3048')

    Battle(0x00000281, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_30F2')

    def _loc_3058(): pass

    label('loc_3058')

    Battle(0x00000282, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_30F2')

    def _loc_3068(): pass

    label('loc_3068')

    Battle(0x00000283, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_30F2')

    def _loc_3078(): pass

    label('loc_3078')

    Battle(0x00000284, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_30F2')

    def _loc_3088(): pass

    label('loc_3088')

    Battle(0x00000285, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_30F2')

    def _loc_3098(): pass

    label('loc_3098')

    Battle(0x00000286, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_30F2')

    def _loc_30A8(): pass

    label('loc_30A8')

    Battle(0x00000287, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_30F2')

    def _loc_30B8(): pass

    label('loc_30B8')

    Battle(0x00000288, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_30F2')

    def _loc_30C8(): pass

    label('loc_30C8')

    Battle(0x00000289, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_30F2')

    def _loc_30D8(): pass

    label('loc_30D8')

    Battle(0x0000028A, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_30F2')

    def _loc_30E8(): pass

    label('loc_30E8')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_30F2(): pass

    label('loc_30F2')

    Jump('func_2E_2F9A')

    def _loc_30F5(): pass

    label('loc_30F5')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x002F offset: 0x3103
@scena.Code('func_2F_3103')
def func_2F_3103():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_31CD',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'R4100_01\n'),
            TXT(0x01, 'R4100_02\n'),
            TXT(0x02, 'R4100_03\n'),
            TXT(0x03, 'R4100_04\n'),
            TXT(0x04, 'R4100_05\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_3170'),
        (0x00000001, 'loc_3180'),
        (0x00000002, 'loc_3190'),
        (0x00000003, 'loc_31A0'),
        (0x00000004, 'loc_31B0'),
        (-1, 'loc_31C0'),
    )

    def _loc_3170(): pass

    label('loc_3170')

    Battle(0x00000295, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_31CA')

    def _loc_3180(): pass

    label('loc_3180')

    Battle(0x00000296, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_31CA')

    def _loc_3190(): pass

    label('loc_3190')

    Battle(0x00000297, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_31CA')

    def _loc_31A0(): pass

    label('loc_31A0')

    Battle(0x00000298, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_31CA')

    def _loc_31B0(): pass

    label('loc_31B0')

    Battle(0x00000299, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_31CA')

    def _loc_31C0(): pass

    label('loc_31C0')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_31CA(): pass

    label('loc_31CA')

    Jump('func_2F_3103')

    def _loc_31CD(): pass

    label('loc_31CD')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0030 offset: 0x31DB
@scena.Code('func_30_31DB')
def func_30_31DB():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_32A5',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'T4301_01\n'),
            TXT(0x01, 'T4301_02\n'),
            TXT(0x02, 'T4301_03\n'),
            TXT(0x03, 'T4301_04\n'),
            TXT(0x04, 'T4301_05\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_3248'),
        (0x00000001, 'loc_3258'),
        (0x00000002, 'loc_3268'),
        (0x00000003, 'loc_3278'),
        (0x00000004, 'loc_3288'),
        (-1, 'loc_3298'),
    )

    def _loc_3248(): pass

    label('loc_3248')

    Battle(0x000002BD, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_32A2')

    def _loc_3258(): pass

    label('loc_3258')

    Battle(0x000002BE, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_32A2')

    def _loc_3268(): pass

    label('loc_3268')

    Battle(0x000002BF, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_32A2')

    def _loc_3278(): pass

    label('loc_3278')

    Battle(0x000002C0, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_32A2')

    def _loc_3288(): pass

    label('loc_3288')

    Battle(0x000002C1, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_32A2')

    def _loc_3298(): pass

    label('loc_3298')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_32A2(): pass

    label('loc_32A2')

    Jump('func_30_31DB')

    def _loc_32A5(): pass

    label('loc_32A5')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0031 offset: 0x32B3
@scena.Code('func_31_32B3')
def func_31_32B3():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_337D',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'T4310_01\n'),
            TXT(0x01, 'T4310_02\n'),
            TXT(0x02, 'T4310_03\n'),
            TXT(0x03, 'T4310_04\n'),
            TXT(0x04, 'T4310_05\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_3320'),
        (0x00000001, 'loc_3330'),
        (0x00000002, 'loc_3340'),
        (0x00000003, 'loc_3350'),
        (0x00000004, 'loc_3360'),
        (-1, 'loc_3370'),
    )

    def _loc_3320(): pass

    label('loc_3320')

    Battle(0x000002D1, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_337A')

    def _loc_3330(): pass

    label('loc_3330')

    Battle(0x000002D2, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_337A')

    def _loc_3340(): pass

    label('loc_3340')

    Battle(0x000002D3, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_337A')

    def _loc_3350(): pass

    label('loc_3350')

    Battle(0x000002D4, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_337A')

    def _loc_3360(): pass

    label('loc_3360')

    Battle(0x000002D5, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_337A')

    def _loc_3370(): pass

    label('loc_3370')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_337A(): pass

    label('loc_337A')

    Jump('func_31_32B3')

    def _loc_337D(): pass

    label('loc_337D')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0032 offset: 0x338B
@scena.Code('func_32_338B')
def func_32_338B():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3455',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'T4210_01\n'),
            TXT(0x01, 'T4210_02\n'),
            TXT(0x02, 'T4210_03\n'),
            TXT(0x03, 'T4210_04\n'),
            TXT(0x04, 'T4210_05\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_33F8'),
        (0x00000001, 'loc_3408'),
        (0x00000002, 'loc_3418'),
        (0x00000003, 'loc_3428'),
        (0x00000004, 'loc_3438'),
        (-1, 'loc_3448'),
    )

    def _loc_33F8(): pass

    label('loc_33F8')

    Battle(0x000002E5, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_3452')

    def _loc_3408(): pass

    label('loc_3408')

    Battle(0x000002E6, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_3452')

    def _loc_3418(): pass

    label('loc_3418')

    Battle(0x000002E7, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_3452')

    def _loc_3428(): pass

    label('loc_3428')

    Battle(0x000002E8, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_3452')

    def _loc_3438(): pass

    label('loc_3438')

    Battle(0x000002E9, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_3452')

    def _loc_3448(): pass

    label('loc_3448')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_3452(): pass

    label('loc_3452')

    Jump('func_32_338B')

    def _loc_3455(): pass

    label('loc_3455')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0033 offset: 0x3463
@scena.Code('func_33_3463')
def func_33_3463():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_352D',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'T4201_01\n'),
            TXT(0x01, 'T4201_02\n'),
            TXT(0x02, 'T4201_03\n'),
            TXT(0x03, 'T4201_04\n'),
            TXT(0x04, 'T4201_05\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_34D0'),
        (0x00000001, 'loc_34E0'),
        (0x00000002, 'loc_34F0'),
        (0x00000003, 'loc_3500'),
        (0x00000004, 'loc_3510'),
        (-1, 'loc_3520'),
    )

    def _loc_34D0(): pass

    label('loc_34D0')

    Battle(0x000002F9, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_352A')

    def _loc_34E0(): pass

    label('loc_34E0')

    Battle(0x000002FA, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_352A')

    def _loc_34F0(): pass

    label('loc_34F0')

    Battle(0x000002FB, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_352A')

    def _loc_3500(): pass

    label('loc_3500')

    Battle(0x000002FC, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_352A')

    def _loc_3510(): pass

    label('loc_3510')

    Battle(0x000002FD, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_352A')

    def _loc_3520(): pass

    label('loc_3520')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_352A(): pass

    label('loc_352A')

    Jump('func_33_3463')

    def _loc_352D(): pass

    label('loc_352D')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0034 offset: 0x353B
@scena.Code('func_34_353B')
def func_34_353B():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3605',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'R4100_21\n'),
            TXT(0x01, 'R4100_22\n'),
            TXT(0x02, 'R4100_23\n'),
            TXT(0x03, 'R4100_24\n'),
            TXT(0x04, 'R4100_25\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_35A8'),
        (0x00000001, 'loc_35B8'),
        (0x00000002, 'loc_35C8'),
        (0x00000003, 'loc_35D8'),
        (0x00000004, 'loc_35E8'),
        (-1, 'loc_35F8'),
    )

    def _loc_35A8(): pass

    label('loc_35A8')

    Battle(0x000002A9, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_3602')

    def _loc_35B8(): pass

    label('loc_35B8')

    Battle(0x000002AA, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_3602')

    def _loc_35C8(): pass

    label('loc_35C8')

    Battle(0x000002AB, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_3602')

    def _loc_35D8(): pass

    label('loc_35D8')

    Battle(0x000002AC, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_3602')

    def _loc_35E8(): pass

    label('loc_35E8')

    Battle(0x000002AD, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_3602')

    def _loc_35F8(): pass

    label('loc_35F8')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_3602(): pass

    label('loc_3602')

    Jump('func_34_353B')

    def _loc_3605(): pass

    label('loc_3605')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0035 offset: 0x3613
@scena.Code('func_35_3613')
def func_35_3613():
    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_361D(): pass

    label('loc_361D')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3805',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        2,
        10,
        100,
        1,
        (
            TXT(0x00, '布卢布兰\n'),
            TXT(0x01, '瓦鲁特\n'),
            TXT(0x02, '露茜奥拉\n'),
            TXT(0x03, '玲\n'),
            TXT(0x04, '莱维\n'),
            TXT(0x05, '怀斯曼\n'),
            TXT(0x06, '猎兵克鲁茨\n'),
            TXT(0x07, '猎兵卡露娜\n'),
            TXT(0x08, '猎兵库拉茨\n'),
            TXT(0x09, '洗脑库拉茨\n'),
            TXT(0x0A, '洗脑卡露娜\n'),
            TXT(0x0B, '洗脑亚妮拉丝\n'),
            TXT(0x0C, '猎兵基尔巴特\n'),
            TXT(0x0D, '穆拉\n'),
            TXT(0x0E, '希德\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_3708'),
        (0x00000001, 'loc_3718'),
        (0x00000002, 'loc_3728'),
        (0x00000003, 'loc_3738'),
        (0x00000004, 'loc_3748'),
        (0x00000005, 'loc_3758'),
        (0x00000006, 'loc_3768'),
        (0x00000007, 'loc_3778'),
        (0x00000008, 'loc_3788'),
        (0x00000009, 'loc_3798'),
        (0x0000000A, 'loc_37A8'),
        (0x0000000B, 'loc_37B8'),
        (0x0000000C, 'loc_37C8'),
        (0x0000000D, 'loc_37D8'),
        (0x0000000E, 'loc_37E8'),
        (-1, 'loc_37F8'),
    )

    def _loc_3708(): pass

    label('loc_3708')

    Battle(0x00000802, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_3802')

    def _loc_3718(): pass

    label('loc_3718')

    Battle(0x00000803, 0x0030000D, 0x00, 0x0000, 0xFF)

    Jump('loc_3802')

    def _loc_3728(): pass

    label('loc_3728')

    Battle(0x00000804, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_3802')

    def _loc_3738(): pass

    label('loc_3738')

    Battle(0x00000805, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_3802')

    def _loc_3748(): pass

    label('loc_3748')

    Battle(0x00000806, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_3802')

    def _loc_3758(): pass

    label('loc_3758')

    Battle(0x00000807, 0x0030000C, 0x00, 0x0000, 0xFF)

    Jump('loc_3802')

    def _loc_3768(): pass

    label('loc_3768')

    Battle(0x00000395, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_3802')

    def _loc_3778(): pass

    label('loc_3778')

    Battle(0x00000394, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_3802')

    def _loc_3788(): pass

    label('loc_3788')

    Battle(0x00000397, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_3802')

    def _loc_3798(): pass

    label('loc_3798')

    Battle(0x0000041E, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_3802')

    def _loc_37A8(): pass

    label('loc_37A8')

    Battle(0x0000041F, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_3802')

    def _loc_37B8(): pass

    label('loc_37B8')

    Battle(0x00000420, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_3802')

    def _loc_37C8(): pass

    label('loc_37C8')

    Battle(0x0000042A, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_3802')

    def _loc_37D8(): pass

    label('loc_37D8')

    Battle(0x000000A8, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_3802')

    def _loc_37E8(): pass

    label('loc_37E8')

    Battle(0x00000C82, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_3802')

    def _loc_37F8(): pass

    label('loc_37F8')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_3802(): pass

    label('loc_3802')

    Jump('loc_361D')

    def _loc_3805(): pass

    label('loc_3805')

    OP_5F(0x0002)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0036 offset: 0x3813
@scena.Code('func_36_3813')
def func_36_3813():
    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_381D(): pass

    label('loc_381D')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_39F9',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        2,
        10,
        100,
        1,
        (
            TXT(0x00, '前篇最终Boss\n'),
            TXT(0x01, '风暴袭击者\n'),
            TXT(0x02, '幻想乐曲·德尔基昂\n'),
            TXT(0x03, '雷格纳特\n'),
            TXT(0x04, '奥尔杰尤\n'),
            TXT(0x05, '帕蒂尔·玛蒂尔\n'),
            TXT(0x06, '帕蒂尔·玛蒂尔（玲附着）\n'),
            TXT(0x07, '天使·怀斯曼第一形态\n'),
            TXT(0x08, '天使·怀斯曼第二形态\n'),
            TXT(0x09, '天使·怀斯曼不能取胜\n'),
            TXT(0x0A, '天使·怀斯曼第二形态（效果）\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_3936'),
        (0x00000001, 'loc_3946'),
        (0x00000002, 'loc_3956'),
        (0x00000003, 'loc_3966'),
        (0x00000004, 'loc_3976'),
        (0x00000005, 'loc_3986'),
        (0x00000006, 'loc_3996'),
        (0x00000007, 'loc_39A6'),
        (0x00000008, 'loc_39B6'),
        (0x00000009, 'loc_39C6'),
        (0x0000000A, 'loc_39DC'),
        (-1, 'loc_39EC'),
    )

    def _loc_3936(): pass

    label('loc_3936')

    Battle(0x000007D3, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_39F6')

    def _loc_3946(): pass

    label('loc_3946')

    Battle(0x0000044C, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_39F6')

    def _loc_3956(): pass

    label('loc_3956')

    Battle(0x00000450, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_39F6')

    def _loc_3966(): pass

    label('loc_3966')

    Battle(0x0000044F, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_39F6')

    def _loc_3976(): pass

    label('loc_3976')

    Battle(0x0000044E, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_39F6')

    def _loc_3986(): pass

    label('loc_3986')

    Battle(0x00000463, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_39F6')

    def _loc_3996(): pass

    label('loc_3996')

    Battle(0x00000453, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_39F6')

    def _loc_39A6(): pass

    label('loc_39A6')

    Battle(0x00000451, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_39F6')

    def _loc_39B6(): pass

    label('loc_39B6')

    Battle(0x00000452, 0x00300017, 0x00, 0x0000, 0xFF)

    Jump('loc_39F6')

    def _loc_39C6(): pass

    label('loc_39C6')

    SetScenaFlags(ScenaFlag(0x0453, 0, 0x2298))
    Battle(0x00000465, 0x00300014, 0x00, 0x0000, 0xFF)
    ClearScenaFlags(ScenaFlag(0x0453, 0, 0x2298))

    Jump('loc_39F6')

    def _loc_39DC(): pass

    label('loc_39DC')

    Battle(0x000007D8, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_39F6')

    def _loc_39EC(): pass

    label('loc_39EC')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_39F6(): pass

    label('loc_39F6')

    Jump('loc_381D')

    def _loc_39F9(): pass

    label('loc_39F9')

    OP_5F(0x0002)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0037 offset: 0x3A07
@scena.Code('func_37_3A07')
def func_37_3A07():
    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_3A11(): pass

    label('loc_3A11')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3AA1',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        2,
        10,
        100,
        1,
        (
            TXT(0x00, '螃蟹老大\n'),
            TXT(0x01, '企鹅老大\n'),
            TXT(0x02, '猿羊老大\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_3A64'),
        (0x00000001, 'loc_3A74'),
        (0x00000002, 'loc_3A84'),
        (-1, 'loc_3A94'),
    )

    def _loc_3A64(): pass

    label('loc_3A64')

    Battle(0x00000059, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_3A9E')

    def _loc_3A74(): pass

    label('loc_3A74')

    Battle(0x000001EA, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_3A9E')

    def _loc_3A84(): pass

    label('loc_3A84')

    Battle(0x000001EB, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_3A9E')

    def _loc_3A94(): pass

    label('loc_3A94')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_3A9E(): pass

    label('loc_3A9E')

    Jump('loc_3A11')

    def _loc_3AA1(): pass

    label('loc_3AA1')

    OP_5F(0x0002)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0038 offset: 0x3AAF
@scena.Code('func_38_3AAF')
def func_38_3AAF():
    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_3AB9(): pass

    label('loc_3AB9')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3BB0',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        2,
        10,
        100,
        1,
        (
            TXT(0x00, '８章，露茜奥拉～玲\n'),
            TXT(0x01, '８章，布卢布兰\n'),
            TXT(0x02, '９章，约修亚ＶＳ艾丝蒂尔\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_3B2C'),
        (0x00000001, 'loc_3B7A'),
        (0x00000002, 'loc_3B93'),
        (-1, 'loc_3BA3'),
    )

    def _loc_3B2C(): pass

    label('loc_3B2C')

    ExecExpressionWithVar(
        0x30,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Battle(0x00002710, 0x0030000F, 0x00, 0x0000, 0xFF)

    ExecExpressionWithVar(
        0x30,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Battle(0x00002711, 0x00300010, 0x00, 0x0000, 0xFF)

    ExecExpressionWithVar(
        0x30,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Battle(0x00002712, 0x00300011, 0x00, 0x0000, 0xFF)

    ExecExpressionWithVar(
        0x30,
        (
            (Expr.PushLong, 0x10),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3BAD')

    def _loc_3B7A(): pass

    label('loc_3B7A')

    ExecExpressionWithVar(
        0x30,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Battle(0x00002713, 0x00300012, 0x00, 0x0000, 0xFF)

    Jump('loc_3BAD')

    def _loc_3B93(): pass

    label('loc_3B93')

    Battle(0x00002714, 0x00300013, 0x00, 0x0000, 0xFF)

    Jump('loc_3BAD')

    def _loc_3BA3(): pass

    label('loc_3BA3')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_3BAD(): pass

    label('loc_3BAD')

    Jump('loc_3AB9')

    def _loc_3BB0(): pass

    label('loc_3BB0')

    OP_5F(0x0002)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0039 offset: 0x3BBE
@scena.Code('func_39_3BBE')
def func_39_3BBE():
    Return()

# id: 0x003A offset: 0x3BBF
@scena.Code('func_3A_3BBF')
def func_3A_3BBF():
    ChrSetStatus(ChrTable['艾丝蒂尔'], 0x00, 85)
    ChrSetStatus(ChrTable['约修亚'], 0x00, 85)
    ChrSetStatus(ChrTable['雪拉扎德'], 0x00, 85)
    ChrSetStatus(ChrTable['奥利维尔'], 0x00, 85)
    ChrSetStatus(ChrTable['提妲'], 0x00, 85)
    ChrSetStatus(ChrTable['科洛丝'], 0x00, 85)
    ChrSetStatus(ChrTable['阿加特'], 0x00, 85)
    ChrSetStatus(ChrTable['金'], 0x00, 85)
    ChrSetStatus(ChrTable['凯文神父'], 0x00, 85)
    ChrSetStatus(ChrTable['亚妮拉丝'], 0x00, 85)
    ChrSetStatus(ChrTable['乔丝特'], 0x00, 85)
    ChrSetStatus(ChrTable['理查德'], 0x00, 85)
    ChrSetStatus(ChrTable['穆拉'], 0x00, 85)
    ChrSetStatus(ChrTable['凯诺娜'], 0x00, 85)
    ChrSetStatus(ChrTable['克鲁茨'], 0x00, 85)
    ChrSetStatus(ChrTable['尤莉亚上尉'], 0x00, 85)
    ChrSetStatus(ChrTable['艾丝蒂尔'], 0x05, 100)
    ChrSetStatus(ChrTable['约修亚'], 0x05, 100)
    ChrSetStatus(ChrTable['雪拉扎德'], 0x05, 100)
    ChrSetStatus(ChrTable['奥利维尔'], 0x05, 100)
    ChrSetStatus(ChrTable['提妲'], 0x05, 100)
    ChrSetStatus(ChrTable['科洛丝'], 0x05, 100)
    ChrSetStatus(ChrTable['阿加特'], 0x05, 100)
    ChrSetStatus(ChrTable['金'], 0x05, 100)
    ChrSetStatus(ChrTable['凯文神父'], 0x05, 100)
    ChrSetStatus(ChrTable['亚妮拉丝'], 0x05, 100)
    ChrSetStatus(ChrTable['乔丝特'], 0x05, 100)
    ChrSetStatus(ChrTable['理查德'], 0x05, 100)
    ChrSetStatus(ChrTable['穆拉'], 0x05, 100)
    ChrSetStatus(ChrTable['凯诺娜'], 0x05, 100)
    ChrSetStatus(ChrTable['克鲁茨'], 0x05, 100)
    ChrSetStatus(ChrTable['尤莉亚上尉'], 0x05, 100)
    OP_37(0x00, 0xFF)
    OP_37(0x01, 0xFF)
    OP_37(0x02, 0xFF)
    OP_37(0x03, 0xFF)
    OP_37(0x06, 0xFF)
    OP_37(0x04, 0xFF)
    OP_37(0x05, 0xFF)
    OP_37(0x07, 0xFF)
    OP_37(0x08, 0xFF)
    OP_37(0x09, 0xFF)
    OP_37(0x0A, 0xFF)
    OP_37(0x0B, 0xFF)
    OP_37(0x0F, 0xFF)
    OP_37(0x0C, 0xFF)
    OP_37(0x0D, 0xFF)
    OP_37(0x0E, 0xFF)
    AddItem(ItemTable['大回复药'], 99)
    AddItem(ItemTable['全回复药'], 99)
    AddItem(ItemTable['痊愈之药'], 99)
    AddItem(ItemTable['复苏药'], 99)
    AddItem(ItemTable['圣灵药'], 10)
    AddItem(ItemTable['还魂胶囊'], 8)
    AddItem(ItemTable['EP填充剂Ⅱ'], 99)
    AddItem(ItemTable['EP填充剂Ⅱ'], 99)
    OP_34(0x01, 0x003C)
    OP_34(0x01, 0x003E)
    OP_34(0x01, 0x0041)
    OP_34(0x01, 0x003F)
    OP_34(0x01, 0x005F)
    OP_34(0x01, 0x0060)
    OP_34(0x01, 0x0069)
    OP_34(0x01, 0x006A)
    OP_34(0x00, 0x001E)
    OP_34(0x00, 0x001F)
    OP_34(0x00, 0x0020)
    OP_34(0x00, 0x0023)
    OP_34(0x00, 0x0025)
    OP_34(0x00, 0x006E)
    OP_34(0x00, 0x006F)
    OP_34(0x00, 0x0070)
    OP_34(0x00, 0x0076)
    OP_34(0x00, 0x0077)
    OP_34(0x00, 0x0078)
    OP_34(0x02, 0x0032)
    OP_34(0x02, 0x0033)
    OP_34(0x02, 0x0034)
    OP_34(0x02, 0x0036)
    OP_34(0x02, 0x0037)
    OP_34(0x03, 0x0064)
    OP_34(0x03, 0x0069)
    OP_34(0x03, 0x0069)
    OP_34(0x03, 0x004B)
    OP_34(0x03, 0x004C)
    OP_34(0x04, 0x006E)
    OP_34(0x04, 0x006F)
    OP_34(0x04, 0x0070)
    OP_34(0x04, 0x0072)
    OP_34(0x04, 0x0073)
    OP_34(0x04, 0x0076)
    OP_34(0x04, 0x0077)
    OP_34(0x04, 0x0078)
    OP_34(0x05, 0x001E)
    OP_34(0x05, 0x001F)
    OP_34(0x05, 0x0020)
    OP_34(0x06, 0x0056)
    OP_34(0x06, 0x0057)
    OP_34(0x06, 0x0058)
    OP_34(0x06, 0x006E)
    OP_34(0x06, 0x006F)
    OP_34(0x06, 0x0076)
    OP_34(0x07, 0x000B)
    OP_34(0x07, 0x000D)
    OP_34(0x07, 0x0010)
    OP_34(0x07, 0x004B)
    OP_34(0x07, 0x004C)
    AddCraft(ChrTable['艾丝蒂尔'], 0x0000)
    AddCraft(ChrTable['约修亚'], 0x0000)
    AddCraft(ChrTable['雪拉扎德'], 0x0000)
    AddCraft(ChrTable['奥利维尔'], 0x0000)
    AddCraft(ChrTable['科洛丝'], 0x0000)
    AddCraft(ChrTable['阿加特'], 0x0000)
    AddCraft(ChrTable['提妲'], 0x0000)
    AddCraft(ChrTable['金'], 0x0000)
    AddCraft(ChrTable['凯文神父'], 0x0000)
    AddCraft(ChrTable['乔丝特'], 0x0000)
    AddCraft(ChrTable['理查德'], 0x0000)
    AddCraft(ChrTable['尤莉亚上尉'], 0x0000)
    AddCraft(ChrTable['穆拉'], 0x0000)
    AddCraft(ChrTable['克鲁茨'], 0x0000)
    AddCraft(ChrTable['亚妮拉丝'], 0x0000)
    AddCraft(ChrTable['凯诺娜'], 0x0000)
    EquipCmd(ChrTable['艾丝蒂尔'], ItemTable['斗神'], 0xFF)
    EquipCmd(ChrTable['艾丝蒂尔'], ItemTable['大地女神之服'], 0xFF)
    EquipCmd(ChrTable['艾丝蒂尔'], ItemTable['超重装甲服'], 0xFF)
    EquipCmd(ChrTable['约修亚'], ItemTable['光之环'], 0xFF)
    EquipCmd(ChrTable['约修亚'], ItemTable['大地女神之服'], 0xFF)
    EquipCmd(ChrTable['约修亚'], ItemTable['普罗米修斯神靴'], 0xFF)
    EquipCmd(ChrTable['雪拉扎德'], ItemTable['赤蔷薇'], 0xFF)
    EquipCmd(ChrTable['雪拉扎德'], ItemTable['大地女神之服'], 0xFF)
    EquipCmd(ChrTable['雪拉扎德'], ItemTable['普罗米修斯神靴'], 0xFF)
    EquipCmd(ChrTable['奥利维尔'], ItemTable['殂击神'], 0xFF)
    EquipCmd(ChrTable['奥利维尔'], ItemTable['大地女神之服'], 0xFF)
    EquipCmd(ChrTable['奥利维尔'], ItemTable['普罗米修斯神靴'], 0xFF)
    EquipCmd(ChrTable['科洛丝'], ItemTable['七星剑'], 0xFF)
    EquipCmd(ChrTable['科洛丝'], ItemTable['大地女神之服'], 0xFF)
    EquipCmd(ChrTable['科洛丝'], ItemTable['普罗米修斯神靴'], 0xFF)
    EquipCmd(ChrTable['阿加特'], ItemTable['狮子王剑'], 0xFF)
    EquipCmd(ChrTable['阿加特'], ItemTable['大地女神之服'], 0xFF)
    EquipCmd(ChrTable['阿加特'], ItemTable['普罗米修斯神靴'], 0xFF)
    EquipCmd(ChrTable['提妲'], ItemTable['Ω巨无霸'], 0xFF)
    EquipCmd(ChrTable['提妲'], ItemTable['大地女神之服'], 0xFF)
    EquipCmd(ChrTable['提妲'], ItemTable['普罗米修斯神靴'], 0xFF)
    EquipCmd(ChrTable['金'], ItemTable['千手钢腕'], 0xFF)
    EquipCmd(ChrTable['金'], ItemTable['大地女神之服'], 0xFF)
    EquipCmd(ChrTable['金'], ItemTable['普罗米修斯神靴'], 0xFF)

    Return()

# id: 0x003B offset: 0x3E3C
@scena.Code('func_3B_3E3C')
def func_3B_3E3C():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_40C7',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        1,
        10,
        100,
        1,
        (
            TXT(0x00, '迷你游戏00俄罗斯轮盘\n'),
            TXT(0x01, '迷你游戏01游戏机\n'),
            TXT(0x02, '迷你游戏02 21点\n'),
            TXT(0x03, '迷你游戏03钓鱼\n'),
            TXT(0x04, '迷你游戏04纸牌\n'),
            TXT(0x05, '迷你游戏05\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x00FF)
    OP_56(0x00)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_3EE4'),
        (0x00000001, 'loc_3F1D'),
        (0x00000002, 'loc_3F56'),
        (0x00000003, 'loc_3F8F'),
        (0x00000004, 'loc_4048'),
        (0x00000005, 'loc_4081'),
        (-1, 'loc_40BA'),
    )

    def _loc_3EE4(): pass

    label('loc_3EE4')

    FadeOut(300, 0, -1)
    OP_0D()
    OP_C0(0x0B, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    FadeIn(300, 0)

    Jump('loc_40BA')

    def _loc_3F1D(): pass

    label('loc_3F1D')

    FadeOut(300, 0, -1)
    OP_0D()
    OP_C0(0x0C, 0x0000000A, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    FadeIn(300, 0)

    Jump('loc_40BA')

    def _loc_3F56(): pass

    label('loc_3F56')

    FadeOut(300, 0, -1)
    OP_0D()
    OP_C0(0x0D, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    FadeIn(300, 0)

    Jump('loc_40BA')

    def _loc_3F8F(): pass

    label('loc_3F8F')

    AddItem(ItemTable['竹竿'], 10)
    AddItem(0x024F, 10)
    AddItem(ItemTable['雨太公'], 10)
    AddItem(ItemTable['湖泊大帝Ⅱ世'], 10)
    AddItem(ItemTable['海风之星'], 10)
    AddItem(ItemTable['钢竿潜水艇'], 10)
    AddItem(ItemTable['碧玉之星'], 10)
    AddItem(ItemTable['蚯蚓'], 10)
    AddItem(ItemTable['川虫'], 10)
    AddItem(ItemTable['熬炼丸子'], 10)
    AddItem(ItemTable['鲑鱼卵'], 10)
    AddItem(ItemTable['田螺'], 10)
    AddItem(ItemTable['青蛙'], 10)
    AddItem(ItemTable['红虫'], 10)
    AddItem(ItemTable['海参'], 10)
    AddItem(ItemTable['虾米'], 10)
    AddItem(0x03DD, 10)
    AddItem(0x03DE, 10)
    AddItem(ItemTable['水耀晶片'], 10)
    AddItem(ItemTable['火耀晶片'], 10)
    AddItem(ItemTable['地耀晶片'], 10)
    AddItem(ItemTable['时耀晶片'], 10)
    AddItem(ItemTable['空耀晶片'], 10)

    Talk(
        (
            '因为移动到布莱特家，\n',
            '请寻找后面池子的钓鱼点\n',
            '开始钓鱼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    NewScene('ED6_DT21/T0300._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_40BA')

    def _loc_4048(): pass

    label('loc_4048')

    FadeOut(300, 0, -1)
    OP_0D()
    OP_C0(0x0F, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    FadeIn(300, 0)

    Jump('loc_40BA')

    def _loc_4081(): pass

    label('loc_4081')

    FadeOut(300, 0, -1)
    OP_0D()
    OP_C0(0x11, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    FadeIn(300, 0)

    Jump('loc_40BA')

    def _loc_40BA(): pass

    label('loc_40BA')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('func_3B_3E3C')

    def _loc_40C7(): pass

    label('loc_40C7')

    OP_5F(0x0001)
    OP_56(0x00)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
