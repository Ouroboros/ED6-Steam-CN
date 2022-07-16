import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T1102_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1102   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '售票员泰德'),
    TXT(0x02, '拉克斯'),
    TXT(0x03, '诺尔姆'),
    TXT(0x04, '阿尔丹'),
    TXT(0x05, '哈尔德'),
    TXT(0x06, '贝尔娜'),
    TXT(0x07, '飞空艇'),
    TXT(0x08, '飞空艇影子'),
    TXT(0x09, '柏斯市·北街区'),
    TXT(0x0A, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1102.x'
    header.mapIndex       = 1
    header.bgm            = 11
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x3CE5
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x0000B3B0,
            dword_04        = 0x00000000,
            dword_08        = 0x00004074,
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
        ('ED6_DT07/CH01290._CH', 'ED6_DT07/CH01290P._CP'),
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT06/CH20038._CH', 'ED6_DT06/CH20038P._CP'),
    ]

# id: 0x10002 offset: 0xDA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 46050,
            z                   = 0,
            y                   = 19400,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 27300,
            z                   = -10000,
            y                   = 26800,
            direction           = 315,
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
            x                   = 48500,
            z                   = 1500,
            y                   = 36800,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 51400,
            z                   = 1500,
            y                   = 47600,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = 29100,
            z                   = -3000,
            y                   = 17200,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = 51400,
            z                   = 0,
            y                   = 14100,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 48090,
            z                   = 3000,
            y                   = -20910,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x1FA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x1FA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x1FA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 46070,
            triggerZ            = 0,
            triggerY            = 18140,
            triggerRange        = 600,
            actorX              = 46050,
            actorZ              = 1500,
            actorY              = 19400,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 47780,
            triggerZ            = 0,
            triggerY            = 15880,
            triggerRange        = 800,
            actorX              = 47780,
            actorZ              = 2200,
            actorY              = 15880,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000D,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 34950,
            triggerZ            = -10000,
            triggerY            = 24520,
            triggerRange        = 800,
            actorX              = 34950,
            actorZ              = -7800,
            actorY              = 24520,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000E,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 60000,
            triggerZ            = 0,
            triggerY            = 17090,
            triggerRange        = 800,
            actorX              = 60000,
            actorZ              = 1500,
            actorY              = 17090,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000F,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x28A
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 1, 0x339)),
            Expr.Return,
        ),
        'loc_2E7',
    )

    SetChrPos(0x000A, 33980, -9750, 27260, 0)
    SetChrPos(0x0009, 51270, 1800, 37990, 90)
    SetChrPos(0x000B, 51220, 1500, 51120, 90)
    SetChrPos(0x000C, 45170, 0, 17540, 0)

    If(
        (
            (Expr.Eval, "OP_29(0x0010, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_2E4',
    )

    SetChrFlags(0x000C, 0x0080)

    def _loc_2E4(): pass

    label('loc_2E4')

    Jump('loc_350')

    def _loc_2E7(): pass

    label('loc_2E7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_344',
    )

    SetChrPos(0x000A, 33980, -9750, 27260, 0)
    SetChrPos(0x0009, 51270, 1800, 37990, 90)
    SetChrPos(0x000B, 48710, 1500, 33310, 315)
    SetChrPos(0x000C, 45170, 0, 17540, 0)

    If(
        (
            (Expr.Eval, "OP_29(0x0010, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_341',
    )

    SetChrFlags(0x000C, 0x0080)

    def _loc_341(): pass

    label('loc_341')

    Jump('loc_350')

    def _loc_344(): pass

    label('loc_344')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_350',
    )

    SetChrFlags(0x000C, 0x0080)

    def _loc_350(): pass

    label('loc_350')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_367',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x58),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x000A)

    def _loc_367(): pass

    label('loc_367')

    Return()

# id: 0x0001 offset: 0x368
@scena.Code('Init')
def Init():
    OP_16(0x02, 4000, -97000, -92000, 196674)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0072, 1, 0x391)),
            (Expr.TestScenaFlags, ScenaFlag(0x0072, 2, 0x392)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_38F',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_38F(): pass

    label('loc_38F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 4, 0x35C)),
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3C5',
    )

    OP_B1('T1102_1')
    OP_71(0x0007, 0x0004)
    OP_71(0x0008, 0x0004)
    OP_72(0x0007, 0x0020)
    OP_72(0x0008, 0x0020)
    OP_71(0x000B, 0x0004)
    OP_71(0x000C, 0x0004)

    Jump('loc_44A')

    def _loc_3C5(): pass

    label('loc_3C5')

    OP_B1('T1102_2')
    OP_71(0x0007, 0x0004)
    OP_71(0x0008, 0x0004)
    OP_71(0x0009, 0x0004)
    OP_71(0x000A, 0x0004)
    OP_6F(0x000B, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_402',
    )

    OP_72(0x0007, 0x0004)
    OP_72(0x0008, 0x0004)

    Jump('loc_413')

    def _loc_402(): pass

    label('loc_402')

    OP_71(0x0007, 0x0004)
    OP_71(0x0008, 0x0004)
    OP_6F(0x000C, 100)

    def _loc_413(): pass

    label('loc_413')

    OP_72(0x0007, 0x0020)
    OP_72(0x0008, 0x0020)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 1, 0x339)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_436',
    )

    OP_72(0x0009, 0x0004)
    OP_72(0x000A, 0x0004)

    Jump('loc_440')

    def _loc_436(): pass

    label('loc_436')

    OP_71(0x0009, 0x0004)
    OP_71(0x000A, 0x0004)

    def _loc_440(): pass

    label('loc_440')

    OP_72(0x0009, 0x0020)
    OP_72(0x000A, 0x0020)

    def _loc_44A(): pass

    label('loc_44A')

    Return()

# id: 0x0002 offset: 0x44B
@scena.Code('ReInit')
def ReInit():
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
        'loc_470',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_5B2')

    def _loc_470(): pass

    label('loc_470')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_489',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_5B2')

    def _loc_489(): pass

    label('loc_489')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4A2',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_5B2')

    def _loc_4A2(): pass

    label('loc_4A2')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4BB',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_5B2')

    def _loc_4BB(): pass

    label('loc_4BB')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4D4',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_5B2')

    def _loc_4D4(): pass

    label('loc_4D4')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4ED',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_5B2')

    def _loc_4ED(): pass

    label('loc_4ED')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_506',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_5B2')

    def _loc_506(): pass

    label('loc_506')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_51F',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_5B2')

    def _loc_51F(): pass

    label('loc_51F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_538',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_5B2')

    def _loc_538(): pass

    label('loc_538')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_551',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_5B2')

    def _loc_551(): pass

    label('loc_551')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_56A',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_5B2')

    def _loc_56A(): pass

    label('loc_56A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_583',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_5B2')

    def _loc_583(): pass

    label('loc_583')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_59C',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_5B2')

    def _loc_59C(): pass

    label('loc_59C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5B2',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_5B2(): pass

    label('loc_5B2')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5C7',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_5B2')

    def _loc_5C7(): pass

    label('loc_5C7')

    Return()

# id: 0x0003 offset: 0x5C8
@scena.Code('func_03_5C8')
def func_03_5C8():
    Call(0, 0x0004)

    Return()

# id: 0x0004 offset: 0x5CD
@scena.Code('func_04_5CD')
def func_04_5CD():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_6EE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_67F',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '虽然犯人们终于被抓获了，\n',
            '不过这样的事件\n',
            '毕竟还是发生了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '乘客之中也有人\n',
            '提出了各种各样的疑虑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我们得重新审视一下\n',
            '定期船的安保方案才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6EB')

    def _loc_67F(): pass

    label('loc_67F')

    ChrTalk(
        0x0008,
        (
            '虽然犯人们已经被抓获，\n',
            '不过这样的事件毕竟还是发生了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我们得重新审视一下\n',
            '定期船的安保方案才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6EB(): pass

    label('loc_6EB')

    Jump('loc_CC8')

    def _loc_6EE(): pass

    label('loc_6EE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_834',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7E1',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '『赛希莉亚号』\n',
            '刚才往卢安方向飞走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '呼……之后就是\n',
            '东向航线的『林德号』了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '虽然飞艇被发现的时候没出什么问题，\n',
            '但听说现在仍然在军队的监控下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我想可能要等它回到公社之后，\n',
            '才可以决定能否重新起航吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_831')

    def _loc_7E1(): pass

    label('loc_7E1')

    ChrTalk(
        0x0008,
        (
            '我想可能要等\n',
            '东向航线的『林德号』回到公社之后，\n',
            '才可以决定能否重新起航吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_831(): pass

    label('loc_831')

    Jump('loc_CC8')

    def _loc_834(): pass

    label('loc_834')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_949',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8C3',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '虽然只有『赛希莉亚号』能投入运营，\n',
            '但是定期船恢复通航也算是个好消息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '各位搭乘本飞艇的旅客，\n',
            '请从这边的门进入！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_946')

    def _loc_8C3(): pass

    label('loc_8C3')

    ChrTalk(
        0x0008,
        (
            '梅贝尔市长\n',
            '终于将一系列的案件说明清楚了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '原来『林德号』失踪等等事情\n',
            '都是空贼所为。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我非常担心\n',
            '那些乘客是否安全……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_946(): pass

    label('loc_946')

    Jump('loc_CC8')

    def _loc_949(): pass

    label('loc_949')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_A58',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9F7',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '如果再这样继续停航下去，\n',
            '公社的信用就丧失殆尽了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '以前没有发生过这样的事故，\n',
            '也不曾处理过这样的问题……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '如果能尽快\n',
            '把情况说明清楚就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A55')

    def _loc_9F7(): pass

    label('loc_9F7')

    ChrTalk(
        0x0008,
        (
            '如果再这样继续停航下去，\n',
            '公社的信用就丧失殆尽了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '如果能尽快\n',
            '把情况说明清楚就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A55(): pass

    label('loc_A55')

    Jump('loc_CC8')

    def _loc_A58(): pass

    label('loc_A58')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_B4F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AF4',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '公社那边也还没有\n',
            '收到来自军队的任何说明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '超市那边进货出货等事宜\n',
            '也停滞下来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '从各个地方都相继\n',
            '传来了不满和抱怨啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B4C')

    def _loc_AF4(): pass

    label('loc_AF4')

    ChrTalk(
        0x0008,
        (
            '超市那边进货出货等事宜\n',
            '也停滞下来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '从各个地方都相继\n',
            '传来了不满和抱怨啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B4C(): pass

    label('loc_B4C')

    Jump('loc_CC8')

    def _loc_B4F(): pass

    label('loc_B4F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_C43',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BC7',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '现在，\n',
            '定期船的航行计划被无限期推迟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '而且非常抱歉的是， \n',
            '这停航的状态不知道何时能解除。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C40')

    def _loc_BC7(): pass

    label('loc_BC7')

    ChrTalk(
        0x0008,
        (
            '虽然我对乘客们说明了情况，\n',
            '但是连我自己也不知道\n',
            '定期船失踪的真正原因……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '王国军队的搜索，\n',
            '到底进行得怎么样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C40(): pass

    label('loc_C40')

    Jump('loc_CC8')

    def _loc_C43(): pass

    label('loc_C43')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_CC8',
    )

    ChrTalk(
        0x0008,
        (
            '定期船现在仍然处于停航状态，\n',
            '重新开航的期限到现在也没有确定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '对一直在空港等候的各位，\n',
            '我代表公社表示万分的歉意……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CC8(): pass

    label('loc_CC8')

    TalkEnd(0x0008)

    Return()

# id: 0x0005 offset: 0xCCC
@scena.Code('func_05_CCC')
def func_05_CCC():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_D7C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D46',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '经历了这样的事件之后，\n',
            '检修工作要更加用心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了恢复公社的信誉，\n',
            '必须要努力工作才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D79')

    def _loc_D46(): pass

    label('loc_D46')

    ChrTalk(
        0x00FE,
        (
            '经历了这样的事件之后，\n',
            '检修工作要更加用心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D79(): pass

    label('loc_D79')

    Jump('loc_11E8')

    def _loc_D7C(): pass

    label('loc_D7C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_E74',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E0B',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '被发现的『林德号』\n',
            '好像还不能重新起航。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这也难怪，机长、乘务员，\n',
            '还有乘客一个都没有找到呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是急人啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E71')

    def _loc_E0B(): pass

    label('loc_E0B')

    ChrTalk(
        0x00FE,
        (
            '被发现的『林德号』\n',
            '好像还不能重新起航。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这也难怪，机长、乘务员，\n',
            '还有乘客一个都没有找到呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E71(): pass

    label('loc_E71')

    Jump('loc_11E8')

    def _loc_E74(): pass

    label('loc_E74')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 1, 0x339)),
            Expr.Return,
        ),
        'loc_EF6',
    )

    ChrTalk(
        0x00FE,
        (
            '因为王国军的警备飞艇要优先考虑，\n',
            '『赛希莉亚号』的检修只能晚一些进行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因此，\n',
            '定期船的出发时间也只能推迟了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11E8')

    def _loc_EF6(): pass

    label('loc_EF6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_1010',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_FAD',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '在卢安待命的\n',
            '『赛希莉亚号』来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且没有想到的是，\n',
            '连雷斯顿要塞的警备飞艇也出动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也要摩拳擦掌啦……\n',
            '虽然这么说，\n',
            '不过感觉手艺生疏了很多啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_100D')

    def _loc_FAD(): pass

    label('loc_FAD')

    ChrTalk(
        0x00FE,
        (
            '在卢安待命的\n',
            '『赛希莉亚号』来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且没有想到的是，\n',
            '连雷斯顿要塞的警备飞艇也出动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_100D(): pass

    label('loc_100D')

    Jump('loc_11E8')

    def _loc_1010(): pass

    label('loc_1010')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_1082',
    )

    ChrTalk(
        0x00FE,
        (
            '我觉得至少让西向航线的\n',
            '『赛希莉亚号』能够起航也好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '警戒如此的森严，\n',
            '看来事态还真是严重啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11E8')

    def _loc_1082(): pass

    label('loc_1082')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_10C6',
    )

    ChrTalk(
        0x00FE,
        (
            '啊呀啊呀，真是辛苦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '光在这里等着就很辛苦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11E8')

    def _loc_10C6(): pass

    label('loc_10C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_11B1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_117B',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '让我们在此待命，\n',
            '到底是因为公社也还没弄清情况呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还是说，\n',
            '已经派飞艇过来了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……已经这么久了，\n',
            '连个说明也没有，\n',
            '大概公社也搞不清现状吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11AE')

    def _loc_117B(): pass

    label('loc_117B')

    ChrTalk(
        0x00FE,
        (
            '这么久了也没有联络。\n',
            '大概公社也搞不清现状吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11AE(): pass

    label('loc_11AE')

    Jump('loc_11E8')

    def _loc_11B1(): pass

    label('loc_11B1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_11E8',
    )

    ChrTalk(
        0x00FE,
        (
            '飞艇还是没有来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到底是怎么一回事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11E8(): pass

    label('loc_11E8')

    TalkEnd(0x0009)

    Return()

# id: 0x0006 offset: 0x11EC
@scena.Code('func_06_11EC')
def func_06_11EC():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_1242',
    )

    ChrTalk(
        0x00FE,
        (
            '飞往帝国的国际航线\n',
            '也一直处于停航状态。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果能赶快恢复就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19ED')

    def _loc_1242(): pass

    label('loc_1242')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_1473',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1323',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '虽然今天没有来，\n',
            '不过这里还是帝国商用飞艇停靠的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '它们都是为了运送货物\n',
            '而到柏斯超市来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正因为如此，\n',
            '这里的飞艇坪有两个跑道哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有两个跑道的城市，\n',
            '除了这里就只有王都格兰赛尔了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1470')

    def _loc_1323(): pass

    label('loc_1323')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_13EF',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '因为有两个跑道，\n',
            '所以要比其他的飞艇坪繁忙多了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，干这项工作，\n',
            '在飞艇平安起飞的瞬间，\n',
            '我们能得到非常大的充实感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然有时候会很辛苦，\n',
            '但是我还是觉得自己很适合这份工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1470')

    def _loc_13EF(): pass

    label('loc_13EF')

    ChrTalk(
        0x00FE,
        (
            '干这项工作，\n',
            '在飞艇平安起飞的瞬间，\n',
            '我们能得到非常大的充实感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然有时候会很辛苦，\n',
            '但是我还是觉得自己很适合这份工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1470(): pass

    label('loc_1470')

    Jump('loc_19ED')

    def _loc_1473(): pass

    label('loc_1473')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 1, 0x339)),
            Expr.Return,
        ),
        'loc_151A',
    )

    ChrTalk(
        0x00FE,
        (
            '就在刚才，\n',
            '王国军的警备飞艇飞走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有一个看上去虽然很年轻\n',
            '却有着显赫地位的将校乘上去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '接下来，要去给正在检修\n',
            '『赛希莉亚号』的主任帮忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19ED')

    def _loc_151A(): pass

    label('loc_151A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_1628',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_15D5',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '在主任检查『赛希莉亚号』的时候，\n',
            '我必须要赶快完成\n',
            '对警备飞艇的基础检查……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不快点完成的话，\n',
            '又要被臭骂一顿了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管是空着还是忙着，\n',
            '我总是会被他痛骂。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1625')

    def _loc_15D5(): pass

    label('loc_15D5')

    ChrTalk(
        0x00FE,
        (
            '在主任检查『赛希莉亚号』的时候，\n',
            '我必须要赶快完成\n',
            '对警备飞艇的基础检查……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1625(): pass

    label('loc_1625')

    Jump('loc_19ED')

    def _loc_1628(): pass

    label('loc_1628')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_16F9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_16C3',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '虽然现在没事可干，\n',
            '但是就这样闲着肯定又要挨骂了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还是去找点事情做吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明明很清闲却要装成忙碌的样子，\n',
            '还真是辛苦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16F6')

    def _loc_16C3(): pass

    label('loc_16C3')

    ChrTalk(
        0x00FE,
        (
            '明明很清闲却要装成忙碌的样子，\n',
            '还真是辛苦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_16F6(): pass

    label('loc_16F6')

    Jump('loc_19ED')

    def _loc_16F9(): pass

    label('loc_16F9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_175F',
    )

    ChrTalk(
        0x00FE,
        (
            '拉克斯主任看上去\n',
            '也非常急躁不安呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '平常就是一幅严肃的面孔，\n',
            '现在显得更加可怕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19ED')

    def _loc_175F(): pass

    label('loc_175F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_1997',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1961',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    ClearMapFlags(0x00000001)

    ChrTalk(
        0x00FE,
        (
            '拉克斯主任在\n',
            '定期船开始运营之前，\n',
            '就已经是飞艇的修理员了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说起来，还是我的老前辈呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算这样，他也太过于严厉了。\n',
            '每天都要挨他的骂……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x000A, 0)

    ChrTalk(
        0x0009,
        (
            '喂，诺尔姆！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrJumpToRelative(0x00FE, 0, 0, 0, 800, 12000)

    If(
        (
            (Expr.PushValueByIndex, 0x64),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            (Expr.PushValueByIndex, 0x64),
            (Expr.PushLong, 0x5A),
            Expr.Leq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1885',
    )

    @scena.Lambda('lambda_1871')
    def lambda_1871():
        OP_6C(135000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1871)

    OP_69(0x0009, 5000)

    Jump('loc_18BB')

    def _loc_1885(): pass

    label('loc_1885')

    If(
        (
            (Expr.PushValueByIndex, 0x64),
            (Expr.PushLong, 0x10E),
            Expr.Geq,
            (Expr.PushValueByIndex, 0x64),
            (Expr.PushLong, 0x168),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_18B4',
    )

    @scena.Lambda('lambda_18A0')
    def lambda_18A0():
        OP_6C(225000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_18A0)

    OP_69(0x0009, 5000)

    Jump('loc_18BB')

    def _loc_18B4(): pass

    label('loc_18B4')

    OP_69(0x0009, 3000)

    def _loc_18BB(): pass

    label('loc_18BB')

    ChrTalk(
        0x0009,
        (
            '我不是告诉你如果闲着\n',
            '就去自己找点工作做吗！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '有聊天的功夫，\n',
            '还不如去整理一下工具！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0009, 0)
    OP_69(0x0000, 3000)
    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '好、好的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0009, 270, 0)
    SetMapFlags(0x00000001)

    Jump('loc_1994')

    def _loc_1961(): pass

    label('loc_1961')

    ChrTalk(
        0x00FE,
        (
            '对不起……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正说着话呢，\n',
            '又被他给骂了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1994(): pass

    label('loc_1994')

    Jump('loc_19ED')

    def _loc_1997(): pass

    label('loc_1997')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_19ED',
    )

    ChrTalk(
        0x00FE,
        (
            '根据公社的指示，\n',
            '我们维修员也将马上到空港待命了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要等到什么时候呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19ED(): pass

    label('loc_19ED')

    TalkEnd(0x000A)

    Return()

# id: 0x0007 offset: 0x19F1
@scena.Code('func_07_19F1')
def func_07_19F1():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_1A5A',
    )

    ChrTalk(
        0x00FE,
        (
            '终于拍到了我的目标——\n',
            '『林德号』的照片了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔，赶快去把\n',
            '它的勇猛身姿显像出来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2118')

    def _loc_1A5A(): pass

    label('loc_1A5A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_1B95',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1B20',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '接下来就是在这里\n',
            '等『林德号』来了……\n',
            '怎么还不来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是啊，\n',
            '其实我最想拍的还是\n',
            '王家的『埃尔赛尤号』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管怎么说也是最新型的飞艇，\n',
            '听说设计方面做得相当有水准。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B92')

    def _loc_1B20(): pass

    label('loc_1B20')

    ChrTalk(
        0x00FE,
        (
            '接下来就是在这里\n',
            '等『林德号』来了……\n',
            '怎么还不来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是啊，\n',
            '其实我最想拍的还是\n',
            '王家的『埃尔赛尤号』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B92(): pass

    label('loc_1B92')

    Jump('loc_2118')

    def _loc_1B95(): pass

    label('loc_1B95')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 1, 0x339)),
            Expr.Return,
        ),
        'loc_1C4A',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然有点偶然，\n',
            '不过今天亲眼看到了\n',
            '王国军配备的新锐机型。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且，\n',
            '还完整地用照相机拍了下来，\n',
            '真是意外的大收获啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在这个飞艇坪等候着，\n',
            '这个决定真是太英明了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2118')

    def _loc_1C4A(): pass

    label('loc_1C4A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_1D8D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D13',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '那、那部飞艇是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难不成那就是\n',
            '王国军的警备飞艇？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说起军队的警备飞艇，\n',
            '它们在十年前的战争中被投入使用，\n',
            '结果带来了丰硕的战果而一举成名。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '厉害～\n',
            '飞艇真是棒啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D8A')

    def _loc_1D13(): pass

    label('loc_1D13')

    ChrTalk(
        0x00FE,
        (
            '说起军队的警备飞艇，\n',
            '它们在十年前的战争中被投入使用，\n',
            '结果带来了丰硕的战果而一举成名。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '厉害～\n',
            '飞艇真是棒啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D8A(): pass

    label('loc_1D8A')

    Jump('loc_2118')

    def _loc_1D8D(): pass

    label('loc_1D8D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_1EE1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1E74',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '在利贝尔国内运营的定期船\n',
            '现在一共有两艘。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '东向航线的『林德号』，\n',
            '以及西向航线的『赛希莉亚号』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然是同一年开始启用的，\n',
            '不过外观的颜色却完全不同。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且『林德号』的导力引擎\n',
            '年代也比较古老。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EDE')

    def _loc_1E74(): pass

    label('loc_1E74')

    ChrTalk(
        0x00FE,
        (
            '在利贝尔国内运营的定期船\n',
            '现在一共有两艘。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '东向航线的『林德号』，\n',
            '以及西向航线的『赛希莉亚号』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1EDE(): pass

    label('loc_1EDE')

    Jump('loc_2118')

    def _loc_1EE1(): pass

    label('loc_1EE1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_1FAF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1F83',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '这里每周一次，\n',
            '都会接待从帝国来的货船。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '柏斯超市的货物\n',
            '就是由它们运走出口的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个稍微有点压迫感的设计\n',
            '倒有点像帝国的风格呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1FAC')

    def _loc_1F83(): pass

    label('loc_1F83')

    ChrTalk(
        0x00FE,
        (
            '啊啊，\n',
            '军队的禁令能不能早点解除啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1FAC(): pass

    label('loc_1FAC')

    Jump('loc_2118')

    def _loc_1FAF(): pass

    label('loc_1FAF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_20C5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2063',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '柏斯的空港因为是国际空港，\n',
            '所以会有各种各样的飞艇来这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我本来是打算把它们\n',
            '都拍进这个导力照相机的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是一艘也没有来，\n',
            '到底是怎么回事啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20C2')

    def _loc_2063(): pass

    label('loc_2063')

    ChrTalk(
        0x00FE,
        (
            '我本来是打算\n',
            '来这里拍摄\n',
            '各种各样的飞艇的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是一艘也没有来，\n',
            '到底是怎么回事啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_20C2(): pass

    label('loc_20C2')

    Jump('loc_2118')

    def _loc_20C5(): pass

    label('loc_20C5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_2118',
    )

    ChrTalk(
        0x00FE,
        (
            '嘿嘿嘿，\n',
            '这里可是最好的摄影场所哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，飞艇啊，\n',
            '快点到这里来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2118(): pass

    label('loc_2118')

    TalkEnd(0x000B)

    Return()

# id: 0x0008 offset: 0x211C
@scena.Code('func_08_211C')
def func_08_211C():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_2491',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0010, 0x01, 0x0002)"),
            (Expr.Eval, "OP_29(0x0010, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2413',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0010, 0x01, 0x2000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2334',
    )

    OP_28(0x0010, 0x01, 0x2000)

    ChrTalk(
        0x00FE,
        (
            '#1370151304V啊，是你们…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1370151305V实在很抱歉，\n',
            '到古罗尼山顶的护卫委托\n',
            '已经取消了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1370151306V因为定期船复航了，\n',
            '我打算乘坐定期船\n',
            '到卢安去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010151307V#004F啊，是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020151308V#013F对不起，\n',
            '我们没有完成委托……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#1370151309V没关系没关系，\n',
            '你们也有很忙的事情嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1370151310V你们现在不是在搜查\n',
            '南街区的强盗事件吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1370151311V游击士真的很辛苦阿。\n',
            '连休息的时间也没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1370151312V你们可要好好努力\n',
            '把空贼集团一网打尽哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010151313V#006F嗯，交给我们吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2410')

    def _loc_2334(): pass

    label('loc_2334')

    ChrTalk(
        0x00FE,
        (
            '#1370151305V实在很抱歉，\n',
            '到古罗尼山顶的护卫委托\n',
            '已经取消了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1370151315V因为定期船复航了，\n',
            '我打算乘坐定期船\n',
            '到卢安去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1370151316V呼，\n',
            '这下子终于能够去谈判了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1370151317V不过耽误了这么长时间，\n',
            '交易也应该告吹了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2410(): pass

    label('loc_2410')

    Jump('loc_248E')

    def _loc_2413(): pass

    label('loc_2413')

    ChrTalk(
        0x00FE,
        (
            '#1370151318V我都快等得不耐烦了。\n',
            '这下终于能够到卢安去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1370151319V但是，\n',
            '此次的商谈估计已经告吹了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1370151320V唉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_248E(): pass

    label('loc_248E')

    Jump('loc_26E7')

    def _loc_2491(): pass

    label('loc_2491')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_2510',
    )

    ChrTalk(
        0x00FE,
        (
            '#1370151321V说起来，\n',
            '竟然不向乘客说明事情的原因，\n',
            '这究竟是怎么一回事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1370151322V再怎么说，\n',
            '这也有点太过分了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26E7')

    def _loc_2510(): pass

    label('loc_2510')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_257C',
    )

    ChrTalk(
        0x00FE,
        (
            '#1370151323V也不知道什么时候\n',
            '定期船才能够重新开航……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1370151324V现在只能在空港\n',
            '乖乖地等下去啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26E7')

    def _loc_257C(): pass

    label('loc_257C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_2683',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2631',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '#1370151298V真是糟糕……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1370151299V本来打算去卢安的，\n',
            '定期船竟然停止运营了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1370151300V唉，虽说是无法避免的事情，\n',
            '但是商谈迟到的话\n',
            '是会丢柏斯商人的脸的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2680')

    def _loc_2631(): pass

    label('loc_2631')

    ChrTalk(
        0x00FE,
        (
            '#1370151300V唉，虽说是无法避免的事情，\n',
            '但是商谈迟到的话\n',
            '是会丢柏斯商人的脸的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2680(): pass

    label('loc_2680')

    Jump('loc_26E7')

    def _loc_2683(): pass

    label('loc_2683')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_26E7',
    )

    ChrTalk(
        0x00FE,
        (
            '#1370151302V哎呀，\n',
            '我是为了坐定期船才来这儿的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1370151303V不过飞船完全没有要来的样子啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_26E7(): pass

    label('loc_26E7')

    TalkEnd(0x000C)

    Return()

# id: 0x0009 offset: 0x26EB
@scena.Code('func_09_26EB')
def func_09_26EB():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_2805',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2792',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '空贼被逮捕了，\n',
            '失踪的船员和乘客\n',
            '也都平安返回了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '空港的接待员说，\n',
            '西向航线的客船\n',
            '马上就可以恢复运行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊～\n',
            '真是让我等好久了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2802')

    def _loc_2792(): pass

    label('loc_2792')

    ChrTalk(
        0x00FE,
        (
            '空贼被逮捕了，\n',
            '失踪的船员和乘客\n',
            '也都平安返回了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '空港的接待员说，\n',
            '西向航线的客船\n',
            '马上就可以恢复运行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2802(): pass

    label('loc_2802')

    Jump('loc_2A96')

    def _loc_2805(): pass

    label('loc_2805')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_2884',
    )

    ChrTalk(
        0x00FE,
        (
            '东向航线的飞艇\n',
            '好像暂时还无法起飞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然有点绕远路，\n',
            '但是坐西向航线的飞艇\n',
            '来绕道去王都可能比较快一点吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A96')

    def _loc_2884(): pass

    label('loc_2884')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_2901',
    )

    ChrTalk(
        0x00FE,
        (
            '卢安那边的飞艇\n',
            '好像已经到达了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且，\n',
            '王国军的飞艇好像也来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他们是来调查\n',
            '那件强盗案件的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A96')

    def _loc_2901(): pass

    label('loc_2901')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_294F',
    )

    ChrTalk(
        0x00FE,
        (
            '这样干等着\n',
            '还真不是一般的累啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我要不要\n',
            '先回家一趟呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A96')

    def _loc_294F(): pass

    label('loc_294F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_29B3',
    )

    ChrTalk(
        0x00FE,
        (
            '空港的工作人员好像\n',
            '对具体的情况也不是很熟悉呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难道说飞行船\n',
            '碰到什么事故了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A96')

    def _loc_29B3(): pass

    label('loc_29B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_2A47',
    )

    ChrTalk(
        0x00FE,
        (
            '现在乘坐飞艇\n',
            '好像是不太可能了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然目前没什么急事，\n',
            '不会感到很难办……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是，\n',
            '至少让我知道什么时候\n',
            '运营能够恢复正常啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A96')

    def _loc_2A47(): pass

    label('loc_2A47')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_2A96',
    )

    ChrTalk(
        0x00FE,
        (
            '我曾经想过到王都旅行的，\n',
            '但是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要搭乘的飞艇\n',
            '却一直没有来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A96(): pass

    label('loc_2A96')

    TalkEnd(0x000D)

    Return()

# id: 0x000A offset: 0x2A9A
@scena.Code('func_0A_2A9A')
def func_0A_2A9A():
    EventBegin(0x00)
    CameraMove(26480, 1500, 26090, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2370, 0)
    OP_6C(45000, 0)
    OP_6E(534, 0)
    SetChrPos(0x0104, 49846, 1500, 40813, 0)
    SetChrPos(0x0103, 48769, 1500, 40913, 0)
    SetChrPos(0x0101, 49846, 1500, 43000, 180)
    SetChrPos(0x0102, 48769, 1500, 43000, 180)
    SetChrPos(0x0009, 51290, 1500, 48590, 90)
    OP_72(0x0007, 0x0004)
    OP_71(0x0007, 0x0002)
    OP_72(0x0008, 0x0004)
    OP_71(0x0008, 0x0002)
    OP_6F(0x0007, 1)
    OP_70(0x0007, 1)
    PlaySE(117, 0x00, 0x64)
    FadeIn(2000, 0)
    CameraMove(49700, 1500, 42500, 5000)
    OP_0D()
    Fade(1000)
    CameraSetDistance(1370, 0)
    OP_0D()

    ChrTalk(
        0x0103,
        (
            '#0030032001V#022F那么我就\n',
            '先回洛连特了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030032002V#025F唔～我还是有点担心啊。\n',
            '真的不用我陪你们吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010032003V#506F都说了～没关系啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010032004V#006F这可是以正游击士为目标的旅行，\n',
            '雪拉姐在的话就不算是修行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020032005V#010F#1P雪拉姐姐再不回去的话，\n',
            '洛连特支部就要一团糟了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020032006V放心吧，我们能办得到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030032007V#025F唔，你们这么说的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030032008V#020F在你们这种年纪\n',
            '就以正游击士为目标实在是很难得。\n',
            '不管怎么说，千万不能太蛮干哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030032009V要是遇到什么麻烦的话，\n',
            '记得马上联络洛连特支部。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030032010V无论你们在哪，\n',
            '我都会火速赶到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010032011V#008F嗯……谢谢，雪拉姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010032012V#506F雪拉姐也是，\n',
            '记得不要喝太多酒哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010032013V我可是只担心这个呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030032014V#520F哈哈……\n',
            '嗯，我会有分寸呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040032015V#035F呵呵，你们就不用担心嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040032016V无论发生什么事，\n',
            '我都会陪在雪拉君身边的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0103, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010032017V#509F……为、为什么\n',
            '你这家伙也要去洛连特？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010032018V而且是和雪拉姐一起……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040032019V#030F哈·哈·哈。\n',
            '因为本人已经尝尽了柏斯的乡土料理。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040032020V正想着差不多\n',
            '该到其他地方看看了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040032021V#031F听说洛连特的蔬菜是极品中的极品，\n',
            '而且雪拉君说过会带我去品尝一番呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030032022V#025F你在胡扯什么呀，\n',
            '我可从没打算为你介绍什么美味的饭店。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030032023V#027F因为你太缠人了，\n',
            '所以我才勉强以陪我去酒馆喝酒为条件，\n',
            '特别准许你跟我去洛连特的哦㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010032024V#007F呜哇～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020032025V#014F#1P奥利维尔……\n',
            '你真的没问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040032026V#030F呵呵，我奥利维尔为了佳人和美食，\n',
            '可是万死不辞的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040032027V#034F不过其实……\n',
            '我也很想可以陪着约修亚君你呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040032028V这真是令人感到迷茫的抉择……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020032029V#017F#1P你迷茫的话我会很困扰的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010032030V#007F真是个超级胡来的家伙……\n',
            '别扰乱洛连特的治安就好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010032031V#006F工作时间之外的\n',
            '雪拉姐可是完全没有节制的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010032032V真心劝你做好准备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030032033V#022F什么话嘛，真没礼貌。\n',
            '爱娜会陪我一起喝的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010032034V#509F她更是个无底洞啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040032035V#033F没有节制？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040032036V那个……难道说……\n',
            '比上次还要可怕吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020032037V#013F#1P……怎么说呢……\n',
            '我觉得上次根本就不值一提。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040032038V#033F唔，是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0104, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    OP_63(0x0104)

    ChrTalk(
        0x0104,
        (
            '#0040032039V#036F#3S咦！？',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    @scena.Lambda('lambda_33A3')
    def lambda_33A3():
        CameraSetDistance(1500, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_33A3)

    @scena.Lambda('lambda_33B3')
    def lambda_33B3():
        CameraMove(51410, 1600, 40400, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_33B3)

    PlaySE(166, 0x00, 0x64)
    Sleep(1000)

    SetMessageWindowPos(72, 320, 56, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('女性的声音')

    Talk(
        (
            '#0880032040V',
            (TxtCtl.SetColor, 0x5),
            '开往洛连特的\n',
            '定期船马上就要起飞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0880032041V',
            (TxtCtl.SetColor, 0x5),
            '请尚未登机的乘客尽快登机。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    ChrTurnDirection(0x0103, 0x0104, 400)

    ChrTalk(
        0x0103,
        (
            '#0030032042V#023F啊，要出发了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030032043V#021F好了奥利维尔，要快点了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0103, 49042, 1500, 40336, 3000, 0x00)

    ChrTalk(
        0x0104,
        (
            '#0040032044V#036F雪、雪拉君，\n',
            '再稍稍等一下嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040032045V再给我点时间考虑，\n',
            '求求你～了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030032046V#021F都要马上登机了，\n',
            '你还想说些什～么呀？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x0103,
        (
            '#0030032047V#024F#5S是男人就不要吞吞吐吐！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 100, 3000, 100)
    CloseMessageWindow()
    OP_62(0x0104, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0104,
        (
            '#0040032048V#036F呜啊啊啊～～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0104, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_35C2')
    def lambda_35C2():
        ChrTurnDirection(0x00FE, 0x0103, 0)
        Yield()

        Jump('lambda_35C2')

    DispatchAsync2(0x0101, 0x0002, lambda_35C2)

    @scena.Lambda('lambda_35D3')
    def lambda_35D3():
        ChrTurnDirection(0x00FE, 0x0103, 0)
        Yield()

        Jump('lambda_35D3')

    DispatchAsync2(0x0102, 0x0002, lambda_35D3)

    @scena.Lambda('lambda_35E4')
    def lambda_35E4():
        ChrWalkTo(0x0101, 49846, 1500, 40813, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_35E4)

    @scena.Lambda('lambda_35FF')
    def lambda_35FF():
        ChrWalkTo(0x0102, 48769, 1500, 40913, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_35FF)

    CreateThread(0x0104, 0x01, 0x00, 0x000C)
    CreateThread(0x0103, 0x01, 0x00, 0x000B)
    Sleep(1000)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010032049V#001F雪拉姐，再见了～！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010032050V帮我向洛连特的各位问好哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020032051V#019F你们两个都要保重哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Sleep(1000)

    WaitForThreadExit(0x0103, 0x0001)
    WaitForThreadExit(0x0104, 0x0001)
    OP_A1(0x000E, 0x0007)
    OP_72(0x0007, 0x0004)
    OP_72(0x0007, 0x0020)
    SetChrPos(0x000E, 62250, -5650, 41990, 0)
    SetChrFlags(0x000E, 0x0004)
    OP_A1(0x000F, 0x0008)
    OP_72(0x0008, 0x0004)
    SetChrPos(0x000F, 62250, -5500, 41990, 0)
    SetChrFlags(0x000F, 0x0004)
    PlaySE(120, 0x00, 0x64)
    OP_6F(0x0009, 0)
    OP_6F(0x000A, 0)
    OP_70(0x0009, 100)
    OP_70(0x000A, 100)
    OP_73(0x0009)
    PlaySE(118, 0x00, 0x64)
    OP_6F(0x0007, 1)
    OP_70(0x0007, 60)
    OP_73(0x0007)
    Fade(2000)
    CameraMove(60000, -1550, 51540, 0)
    OP_67(0, 5760, -10000, 0)
    CameraSetDistance(3240, 0)
    OP_6C(195000, 0)
    OP_6E(550, 0)
    SetChrFlags(0x0103, 0x0080)
    SetChrFlags(0x0104, 0x0080)
    Sleep(2000)

    PlaySE(119, 0x00, 0x64)
    OP_6F(0x0007, 61)
    OP_70(0x0007, 160)
    OP_73(0x0007)
    OP_71(0x0007, 0x0020)
    OP_6F(0x0007, 161)
    OP_70(0x0007, 260)

    @scena.Lambda('lambda_37AC')
    def lambda_37AC():
        CameraMove(60000, -1550, 51540, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_37AC)

    @scena.Lambda('lambda_37C4')
    def lambda_37C4():
        OP_67(0, 11230, -10000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_37C4)

    @scena.Lambda('lambda_37DC')
    def lambda_37DC():
        CameraSetDistance(2260, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_37DC)

    @scena.Lambda('lambda_37EC')
    def lambda_37EC():
        OP_6C(204000, 10000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_37EC)

    @scena.Lambda('lambda_37FC')
    def lambda_37FC():
        OP_6E(801, 10000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_37FC)

    ChrMoveToRelativeAsync(0x000E, 0, 500, 0, 300, 0x00)
    ChrMoveToRelativeAsync(0x000E, 0, 1000, 0, 600, 0x00)
    Sleep(2000)

    @scena.Lambda('lambda_3839')
    def lambda_3839():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_3839)

    OP_94(0x01, 0x000E, 0x0000, 0x000003E8, 0x000003E8, 0x00)

    @scena.Lambda('lambda_385E')
    def lambda_385E():
        OP_94(0x01, 0x00FE, 0x0000, 0x000004B0, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_385E)

    OP_94(0x01, 0x000E, 0x0000, 0x000004B0, 0x000007D0, 0x00)

    @scena.Lambda('lambda_3883')
    def lambda_3883():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000578, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_3883)

    OP_94(0x01, 0x000E, 0x0000, 0x00000578, 0x00000BB8, 0x00)

    @scena.Lambda('lambda_38A8')
    def lambda_38A8():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000640, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_38A8)

    OP_94(0x01, 0x000E, 0x0000, 0x00000640, 0x00000FA0, 0x00)

    @scena.Lambda('lambda_38CD')
    def lambda_38CD():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000708, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_38CD)

    OP_94(0x01, 0x000E, 0x0000, 0x00000708, 0x00001388, 0x00)

    @scena.Lambda('lambda_38F2')
    def lambda_38F2():
        OP_94(0x01, 0x00FE, 0x0000, 0x000007D0, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_38F2)

    OP_94(0x01, 0x000E, 0x0000, 0x000007D0, 0x00001770, 0x00)

    @scena.Lambda('lambda_3917')
    def lambda_3917():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000898, 0x00001B58, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_3917)

    OP_20(0x00000BB8)
    FadeOut(4000, 0, -1)
    OP_94(0x01, 0x000E, 0x0000, 0x00000898, 0x00001B58, 0x00)

    @scena.Lambda('lambda_394B')
    def lambda_394B():
        OP_94(0x01, 0x00FE, 0x0000, 0x0000C350, 0x00001F40, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_394B)

    @scena.Lambda('lambda_3961')
    def lambda_3961():
        OP_94(0x01, 0x00FE, 0x0000, 0x0000C350, 0x00001F40, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_3961)

    OP_0D()
    OP_24(0x0075, 0x5A)
    OP_24(0x0077, 0x5A)
    Sleep(100)

    OP_24(0x0075, 0x50)
    OP_24(0x0077, 0x50)
    Sleep(100)

    OP_24(0x0075, 0x46)
    OP_24(0x0077, 0x46)
    Sleep(100)

    OP_24(0x0075, 0x3C)
    OP_24(0x0077, 0x3C)
    Sleep(100)

    OP_24(0x0075, 0x32)
    OP_24(0x0077, 0x32)
    Sleep(100)

    OP_24(0x0075, 0x28)
    OP_24(0x0077, 0x28)
    Sleep(100)

    OP_24(0x0075, 0x1E)
    OP_24(0x0077, 0x1E)
    Sleep(100)

    OP_24(0x0075, 0x14)
    OP_24(0x0077, 0x14)
    Sleep(100)

    OP_24(0x0075, 0x0A)
    OP_24(0x0077, 0x0A)
    Sleep(100)

    OP_23(0x0075)
    OP_23(0x0077)
    OP_0D()
    OP_21()
    Sleep(1000)

    OP_AD('ED6_DT04/C_VIS046._CH', 0x0000, 0x0000, 0x00000064)
    Sleep(4000)

    OP_56(0x02)
    WaitEffect(0x12, 0x00)
    SetScenaFlags(ScenaFlag(0x0072, 1, 0x391))

    ExecExpressionWithVar(
        0x31,
        (
            (Expr.PushLong, 0xF1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(100000, -100000, 100000, 0)
    FadeIn(0, 0)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        240,
        180,
        0,
        (
            TXT(0x00, '【保存进度】\n'),
            TXT(0x01, '【进入下一章】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3A73',
    )

    ShowSaveMenu()

    def _loc_3A73(): pass

    label('loc_3A73')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_AE(0x000000C8)
    Sleep(2000)

    SetScenaFlags(ScenaFlag(0x0072, 2, 0x392))
    SetChrStatus(0x0000, 0xFE, 0)
    SetChrStatus(0x0001, 0xFE, 0)
    SetChrStatus(0x0002, 0xFE, 0)
    SetChrStatus(0x0003, 0xFE, 0)
    SetChrStatus(0x0004, 0xFE, 0)
    SetChrStatus(0x0005, 0xFE, 0)
    SetChrStatus(0x0006, 0xFE, 0)
    SetChrStatus(0x0007, 0xFE, 0)
    ClearMapFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/E0000._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000B offset: 0x3ACD
@scena.Code('func_0B_3ACD')
def func_0B_3ACD():
    ChrWalkTo(0x00FE, 49169, 1500, 38199, 3000, 0x00)
    ChrWalkTo(0x00FE, 57632, 1500, 38199, 3000, 0x00)
    SetChrFlags(0x00FE, 0x0004)
    ChrWalkTo(0x00FE, 59330, 1500, 39130, 3000, 0x00)
    ChrTurnDirection(0x00FE, 0x0101, 400)

    Return()

# id: 0x000C offset: 0x3B16
@scena.Code('func_0C_3B16')
def func_0C_3B16():
    SetChrDirection(0x00FE, 0, 0)
    ChrMoveTo(0x00FE, 49169, 1500, 38199, 3000, 0x00)
    SetChrDirection(0x00FE, 270, 0)
    ChrMoveTo(0x00FE, 57632, 1500, 38199, 3000, 0x00)
    SetChrFlags(0x00FE, 0x0004)
    ChrMoveTo(0x00FE, 58870, 1500, 38200, 3000, 0x00)
    Sleep(1000)

    ChrTurnDirection(0x00FE, 0x0101, 400)

    Return()

# id: 0x000D offset: 0x3B72
@scena.Code('func_0D_3B72')
def func_0D_3B72():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '定期船起降坪\n',
            '≡　开往洛连特市\n',
            '≡　开往卢安市\n',
            '≡　开往埃雷波尼亚帝国',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x000E offset: 0x3BE8
@scena.Code('func_0E_3BE8')
def func_0E_3BE8():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※请勿携带易燃物和危险品\n',
            '　　　　　利贝尔飞艇公社',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x000F offset: 0x3C4C
@scena.Code('func_0F_3C4C')
def func_0F_3C4C():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　　　飞艇坪塔台　　　　\n',
            '　※无关人员禁止入内　　\n',
            '『利贝尔飞艇公社』　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
