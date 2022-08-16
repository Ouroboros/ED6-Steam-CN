import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4214_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4214   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4214.x'
    header.mapIndex       = 1
    header.bgm            = 17
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
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10000 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH02460._CH', 'ED6_DT07/CH02460P._CP'),
        ('ED6_DT07/CH02540._CH', 'ED6_DT07/CH02540P._CP'),
        ('ED6_DT07/CH01350._CH', 'ED6_DT07/CH01350P._CP'),
    ]

# id: 0x10001 offset: 0xC2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '希尔丹夫人',
            x                   = 68000,
            z                   = 0,
            y                   = 69570,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '茜亚',
            x                   = 72500,
            z                   = 0,
            y                   = 67450,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '布莉姆',
            x                   = 66670,
            z                   = 0,
            y                   = 99650,
            direction           = 12,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
    )

# id: 0x10002 offset: 0x122
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x122
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x122
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x122
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Return,
        ),
        'loc_136',
    )

    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)

    Jump('loc_168')

    def _loc_136(): pass

    label('loc_136')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_14A',
    )

    ChrSetFlags(0x0008, 0x0080)
    ChrClearFlags(0x000A, 0x0080)

    Jump('loc_168')

    def _loc_14A(): pass

    label('loc_14A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_154',
    )

    Jump('loc_168')

    def _loc_154(): pass

    label('loc_154')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_168',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 6, 0x1626)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_168',
    )

    ChrSetFlags(0x0008, 0x0080)

    def _loc_168(): pass

    label('loc_168')

    Return()

# id: 0x0001 offset: 0x169
@scena.Code('func_01_169')
def func_01_169():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_185',
    )

    OP_B1('t4214_y')

    Jump('loc_18E')

    def _loc_185(): pass

    label('loc_185')

    OP_B1('t4214_n')

    def _loc_18E(): pass

    label('loc_18E')

    Return()

# id: 0x0002 offset: 0x18F
@scena.Code('func_02_18F')
def func_02_18F():
    ExecExpressionWithReg(
        0x0001,
        (
            Expr.Rand,
            (Expr.PushLong, 0xE),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1B4',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_2F6')

    def _loc_1B4(): pass

    label('loc_1B4')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1CD',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_2F6')

    def _loc_1CD(): pass

    label('loc_1CD')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1E6',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_2F6')

    def _loc_1E6(): pass

    label('loc_1E6')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1FF',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_2F6')

    def _loc_1FF(): pass

    label('loc_1FF')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_218',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_2F6')

    def _loc_218(): pass

    label('loc_218')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_231',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_2F6')

    def _loc_231(): pass

    label('loc_231')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_24A',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_2F6')

    def _loc_24A(): pass

    label('loc_24A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_263',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_2F6')

    def _loc_263(): pass

    label('loc_263')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_27C',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_2F6')

    def _loc_27C(): pass

    label('loc_27C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_295',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_2F6')

    def _loc_295(): pass

    label('loc_295')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2AE',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_2F6')

    def _loc_2AE(): pass

    label('loc_2AE')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2C7',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_2F6')

    def _loc_2C7(): pass

    label('loc_2C7')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2E0',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_2F6')

    def _loc_2E0(): pass

    label('loc_2E0')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2F6',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_2F6(): pass

    label('loc_2F6')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_30B',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_2F6')

    def _loc_30B(): pass

    label('loc_30B')

    Return()

# id: 0x0003 offset: 0x30C
@scena.Code('func_03_30C')
def func_03_30C():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_32F',
    )

    OP_8D(0x00FE, 66030, 72430, 70230, 65960, 2000)

    Jump('func_03_30C')

    def _loc_32F(): pass

    label('loc_32F')

    Return()

# id: 0x0004 offset: 0x330
@scena.Code('func_04_330')
def func_04_330():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_5DE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02CC, 7, 0x1667)),
            Expr.Return,
        ),
        'loc_3FA',
    )

    ChrTalk(
        0x00FE,
        (
            '#0650271468V……#0713F对凯诺娜小姐来说\n',
            '上校就是一切。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650271469V#0710F对她的心情和行为，\n',
            '同样作为女性的我也\n',
            '绝非不能理解……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650271470V#0714F接下来就等女王\n',
            '陛下来裁决吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5DB')

    def _loc_3FA(): pass

    label('loc_3FA')

    ChrTalk(
        0x00FE,
        (
            '#0650271471V#0712F科洛蒂娅殿下和艾丝蒂尔小姐……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650271472V#0710F……关于恐吓信那件事，看来\n',
            '不只是单纯的恶作剧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650271473V想不到过去的情报部\n',
            '竟然牵连在内……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271474V#1007F没错没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010271475V#1015F想不到又和凯诺娜上尉\n',
            '打了一回。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0650271468V……#0713F对凯诺娜小姐来说\n',
            '上校就是一切。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650271477V#0710F对她的心情和行为，\n',
            '同样身为女性的我也\n',
            '绝非不能理解……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060271478V#042F希尔丹夫人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0650271479V#0710F接下来就等女王\n',
            '陛下来裁决吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x02CC, 7, 0x1667))

    def _loc_5DB(): pass

    label('loc_5DB')

    Jump('loc_64B')

    def _loc_5DE(): pass

    label('loc_5DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_64B',
    )

    ChrTalk(
        0x00FE,
        (
            '#0650271480V#0712F想不到那位小姐\n',
            '竟会变成这样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650271481V#0710F真希望她能快点\n',
            '找到双亲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_64B(): pass

    label('loc_64B')

    TalkEnd(0x0008)

    Return()

# id: 0x0005 offset: 0x64F
@scena.Code('func_05_64F')
def func_05_64F():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_784',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_73C',
    )

    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '啊，约修亚先生……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F茜亚小姐，好久不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '您能平安返回真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F是茜亚？　感觉你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你还是那么漂亮。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1044F咦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没、没什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_781')

    def _loc_73C(): pass

    label('loc_73C')

    ChrTalk(
        0x00FE,
        (
            '科洛蒂娅殿下\n',
            '去了谒见室哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我想希尔丹夫人应该和她在一起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_781(): pass

    label('loc_781')

    Jump('loc_E3B')

    def _loc_784(): pass

    label('loc_784')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_7D9',
    )

    ChrTalk(
        0x00FE,
        (
            '签字仪式的准备外加这次的\n',
            '善后处理……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真为女王陛下的身体担心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E3B')

    def _loc_7D9(): pass

    label('loc_7D9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_E3B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 6, 0x1626)),
            Expr.Return,
        ),
        'loc_83C',
    )

    ChrTalk(
        0x00FE,
        (
            '各位似乎见到了\n',
            '希尔丹夫人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个……方便的话要不要\n',
            '我来准备些饮料呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E3B')

    def _loc_83C(): pass

    label('loc_83C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 1, 0x1629)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DE1',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8D2',
    )

    ChrTalk(
        0x00FE,
        (
            '#2300251105V艾丝蒂尔小姐！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(600)

    ChrTurnDirection(0x00FE, 0x0105, 400)
    Sleep(600)

    ChrTurnDirection(0x00FE, 0x0108, 400)

    ChrTalk(
        0x00FE,
        (
            '#2300251106V科洛蒂娅殿下和金先生也在！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A83')

    def _loc_8D2(): pass

    label('loc_8D2')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_96A',
    )

    ChrTalk(
        0x00FE,
        (
            '#2300251107V啊，科洛蒂娅殿下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(600)

    ChrTurnDirection(0x00FE, 0x0101, 400)
    Sleep(600)

    ChrTurnDirection(0x00FE, 0x0108, 400)

    ChrTalk(
        0x00FE,
        (
            '#2300251108V哎呀，艾丝蒂尔小姐和金先生也在！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A83')

    def _loc_96A(): pass

    label('loc_96A')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9F8',
    )

    ChrTalk(
        0x00FE,
        (
            '#2300251109V金先生！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(600)

    ChrTurnDirection(0x00FE, 0x0105, 400)
    Sleep(600)

    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#2300251110V科洛蒂娅殿下和艾丝蒂尔小姐也在！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A83')

    def _loc_9F8(): pass

    label('loc_9F8')

    ChrTurnDirection(0x00FE, 0x0105, 0)
    Sleep(600)

    ChrTalk(
        0x00FE,
        (
            '#2300251111V科洛蒂娅殿下！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(600)

    ChrTurnDirection(0x00FE, 0x0101, 400)
    Sleep(600)

    ChrTurnDirection(0x00FE, 0x0108, 400)

    ChrTalk(
        0x00FE,
        (
            '#2300251112V艾丝蒂尔小姐和金先生也在！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A83(): pass

    label('loc_A83')

    ChrTurnDirection(0x00FE, 0x0000, 0)

    ChrTalk(
        0x00FE,
        (
            '#2300251113V真、真是失礼了……\n',
            '久疏问候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080251114V#070F哈哈，好久不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251115V#1001F嗯嗯，我还记得让茜亚小姐\n',
            '给我们穿女佣装的事儿呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040251116V#033F哟……艾丝蒂尔你穿女佣装？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251117V#1000F嗯，为了见到女王陛下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251118V对了对了，还硬让\n',
            '约修亚穿上了呢，\n',
            '是茜亚小姐给他化的妆。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251119V#1001F那时候的茜亚小姐啊，\n',
            '在化妆时好像很兴奋呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060251120V#044F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2300251121V不、不好意思……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040251122V#037F完美扮演了塞茜莉亚\n',
            '公主的约修亚的侍女身姿……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040251123V啊，想必是\n',
            '很可爱吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040251124V#034F没能参加公爵的晚宴\n',
            '真是我心中最大的懊恼啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060251125V#045F呵呵……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060251126V#040F对了对了，茜亚小姐，\n',
            '你知道希尔丹夫人\n',
            '去了哪里吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2300251127V哦，希尔丹夫人现在\n',
            '应该在资料室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2300251128V我记得她说有事\n',
            '要调查……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251129V#1001F资料室啊，ＯＫ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x02C5, 1, 0x1629))

    Jump('loc_E3B')

    def _loc_DE1(): pass

    label('loc_DE1')

    ChrTalk(
        0x00FE,
        (
            '#2300251130V希尔丹夫人现在\n',
            '应该在资料室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2300251128V我记得她说有事\n',
            '要调查……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E3B(): pass

    label('loc_E3B')

    TalkEnd(0x0009)

    Return()

# id: 0x0006 offset: 0xE3F
@scena.Code('func_06_E3F')
def func_06_E3F():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_E66',
    )

    ChrTalk(
        0x00FE,
        (
            '呀！！\n',
            '请、请别偷看～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E66(): pass

    label('loc_E66')

    TalkEnd(0x00FE)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
