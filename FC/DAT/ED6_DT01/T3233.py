import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3233_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3233   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '拜舍尔'),
    TXT(0x02, '艾德'),
    TXT(0x03, '林'),
    TXT(0x04, '莉西亚'),
    TXT(0x05, '希利尔'),
    TXT(0x06, '艾缇'),
    TXT(0x07, '拉克'),
    TXT(0x08, '希玛'),
    TXT(0x09, '库安'),
    TXT(0x0A, '西加罗'),
    TXT(0x0B, '艾德尔'),
    TXT(0x0C, '艾丝蒂尔的篮子'),
    TXT(0x0D, '提妲的篮子'),
    TXT(0x0E, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3233.x'
    header.mapIndex       = 1
    header.bgm            = 84
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1FAE
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
        ('ED6_DT07/CH02300._CH', 'ED6_DT07/CH02300P._CP'),
        ('ED6_DT07/CH02310._CH', 'ED6_DT07/CH02310P._CP'),
        ('ED6_DT07/CH02290._CH', 'ED6_DT07/CH02290P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01270._CH', 'ED6_DT07/CH01270P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH01160._CH', 'ED6_DT07/CH01160P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01060._CH', 'ED6_DT07/CH01060P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
        ('ED6_DT06/CH20145._CH', 'ED6_DT06/CH20145P._CP'),
        ('ED6_DT06/CH20146._CH', 'ED6_DT06/CH20146P._CP'),
    ]

# id: 0x10002 offset: 0x132
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1245198,
            chipIndex           = 14,
            npcIndex            = 0x01E6,
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
            dword_10            = 1310734,
            chipIndex           = 14,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x2D2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x2D2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x2D2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -1900,
            triggerZ            = 0,
            triggerY            = 5070,
            triggerRange        = 800,
            actorX              = -1900,
            actorZ              = 1000,
            actorY              = 5070,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000E,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -1890,
            triggerZ            = 0,
            triggerY            = -4990,
            triggerRange        = 800,
            actorX              = -1890,
            actorZ              = 1000,
            actorY              = -4990,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000E,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x31A
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_324',
    )

    Jump('loc_3B3')

    def _loc_324(): pass

    label('loc_324')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_32E',
    )

    Jump('loc_3B3')

    def _loc_32E(): pass

    label('loc_32E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_34E',
    )

    ClearChrFlags(0x0011, 0x0080)
    SetChrPos(0x0011, -1080, 0, 440, 85)

    Jump('loc_3B3')

    def _loc_34E(): pass

    label('loc_34E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_36E',
    )

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, -1090, 0, -900, 82)

    Jump('loc_3B3')

    def _loc_36E(): pass

    label('loc_36E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_378',
    )

    Jump('loc_3B3')

    def _loc_378(): pass

    label('loc_378')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_382',
    )

    Jump('loc_3B3')

    def _loc_382(): pass

    label('loc_382')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Return,
        ),
        'loc_38C',
    )

    Jump('loc_3B3')

    def _loc_38C(): pass

    label('loc_38C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_396',
    )

    Jump('loc_3B3')

    def _loc_396(): pass

    label('loc_396')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_3B3',
    )

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, -1090, 0, -900, 82)

    def _loc_3B3(): pass

    label('loc_3B3')

    Return()

# id: 0x0001 offset: 0x3B4
@scena.Code('Init')
def Init():
    OP_72(0x0008, 0x0010)
    OP_72(0x0009, 0x0010)

    Return()

# id: 0x0002 offset: 0x3BF
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3D4',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_3D4(): pass

    label('loc_3D4')

    Return()

# id: 0x0003 offset: 0x3D5
@scena.Code('func_03_3D5')
def func_03_3D5():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_3E2',
    )

    Jump('loc_42F')

    def _loc_3E2(): pass

    label('loc_3E2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_3EC',
    )

    Jump('loc_42F')

    def _loc_3EC(): pass

    label('loc_3EC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_3F6',
    )

    Jump('loc_42F')

    def _loc_3F6(): pass

    label('loc_3F6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_400',
    )

    Jump('loc_42F')

    def _loc_400(): pass

    label('loc_400')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_40A',
    )

    Jump('loc_42F')

    def _loc_40A(): pass

    label('loc_40A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_414',
    )

    Jump('loc_42F')

    def _loc_414(): pass

    label('loc_414')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Return,
        ),
        'loc_41E',
    )

    Jump('loc_42F')

    def _loc_41E(): pass

    label('loc_41E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_428',
    )

    Jump('loc_42F')

    def _loc_428(): pass

    label('loc_428')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_42F',
    )

    def _loc_42F(): pass

    label('loc_42F')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x433
@scena.Code('func_04_433')
def func_04_433():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_440',
    )

    Jump('loc_539')

    def _loc_440(): pass

    label('loc_440')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_44A',
    )

    Jump('loc_539')

    def _loc_44A(): pass

    label('loc_44A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_4A0',
    )

    ChrTalk(
        0x00FE,
        (
            '蔡斯那边\n',
            '好像发生了什么大事件呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '早早地赶到这里真是明智啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_539')

    def _loc_4A0(): pass

    label('loc_4A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_4AA',
    )

    Jump('loc_539')

    def _loc_4AA(): pass

    label('loc_4AA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_514',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，真是好温泉。\n',
            '身体从内到外都感觉很暖和。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '泡温泉的时候\n',
            '可以把讨厌的事全都给忘掉呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_539')

    def _loc_514(): pass

    label('loc_514')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_51E',
    )

    Jump('loc_539')

    def _loc_51E(): pass

    label('loc_51E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Return,
        ),
        'loc_528',
    )

    Jump('loc_539')

    def _loc_528(): pass

    label('loc_528')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_532',
    )

    Jump('loc_539')

    def _loc_532(): pass

    label('loc_532')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_539',
    )

    def _loc_539(): pass

    label('loc_539')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x53D
@scena.Code('func_05_53D')
def func_05_53D():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_54A',
    )

    Jump('loc_6E9')

    def _loc_54A(): pass

    label('loc_54A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_554',
    )

    Jump('loc_6E9')

    def _loc_554(): pass

    label('loc_554')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_55E',
    )

    Jump('loc_6E9')

    def _loc_55E(): pass

    label('loc_55E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_64D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_5BA',
    )

    ChrTalk(
        0x00FE,
        (
            '原来如此，池钓吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '回到钓公师团的总部之后\n',
            '就立刻去找钓鱼场吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_64A')

    def _loc_5BA(): pass

    label('loc_5BA')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '呵呵，一大早就不由自主\n',
            '想来露天温泉泡个澡。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里的浴池果然很大。\n',
            '有点像个池塘啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，池塘吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对了，\n',
            '下次试试池钓吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_64A(): pass

    label('loc_64A')

    Jump('loc_6E9')

    def _loc_64D(): pass

    label('loc_64D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_657',
    )

    Jump('loc_6E9')

    def _loc_657(): pass

    label('loc_657')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_661',
    )

    Jump('loc_6E9')

    def _loc_661(): pass

    label('loc_661')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Return,
        ),
        'loc_66B',
    )

    Jump('loc_6E9')

    def _loc_66B(): pass

    label('loc_66B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_675',
    )

    Jump('loc_6E9')

    def _loc_675(): pass

    label('loc_675')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_6E9',
    )

    ChrTalk(
        0x00FE,
        (
            '从大白天开始\n',
            '就一直泡澡，\n',
            '这可是温泉的绝妙之处啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀，从温泉出来的时候\n',
            '迎面吹来的风真是清爽啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6E9(): pass

    label('loc_6E9')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x6ED
@scena.Code('func_06_6ED')
def func_06_6ED():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x6F4
@scena.Code('func_07_6F4')
def func_07_6F4():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x6FB
@scena.Code('func_08_6FB')
def func_08_6FB():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x702
@scena.Code('func_09_702')
def func_09_702():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x709
@scena.Code('func_0A_709')
def func_0A_709():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x710
@scena.Code('func_0B_710')
def func_0B_710():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x717
@scena.Code('func_0C_717')
def func_0C_717():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x71E
@scena.Code('func_0D_71E')
def func_0D_71E():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x725
@scena.Code('func_0E_725')
def func_0E_725():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 7, 0x527)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1ECC',
    )

    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x00A5, 0, 0x528))

    If(
        (
            (Expr.GetChrWork, 0x0, 0x3),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_7F5',
    )

    Fade(1000)
    CameraMove(-1360, 0, 5070, 0)
    SetChrPos(0x0101, -150, 0, 4200, 270)
    SetChrPos(0x0102, -800, 0, 3380, 0)
    SetChrPos(0x0107, -580, 0, 5360, 270)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010080372V#000F嗯……\n',
            '这里就是澡堂的入口吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080373V#060F嗯，这里是女浴室，\n',
            '那边的是男浴室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8D2')

    def _loc_7F5(): pass

    label('loc_7F5')

    Fade(1000)
    CameraMove(-1360, 0, -4840, 0)
    SetChrPos(0x0101, -150, 0, -5600, 270)
    SetChrPos(0x0102, -800, 0, -6530, 0)
    SetChrPos(0x0107, -580, 0, -4450, 270)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010080374V#000F嗯……\n',
            '这里就是澡堂的入口吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0107,
        (
            '#0070080375V#065F艾、艾丝蒂尔姐姐。\n',
            '这边是男浴室。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080376V前面那个才是女浴室呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8D2(): pass

    label('loc_8D2')

    ChrTalk(
        0x0101,
        (
            '#0010080377V#004F啊，原来是这样啊。\n',
            '男女分开的啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080378V#001F哈哈，不过那也是当然的。\n',
            '因为要换衣服嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080379V#015F咳咳……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080380V#010F那样的话，\n',
            '我们要暂时分开一会儿了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0102, 400)
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010080381V#001F嗯，待会见⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080382V#560F失陪了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(1000)

    CameraMove(-32439, 0, 28640, 0)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0014, 0x0080)
    SetChrPos(0x0013, -31500, 1300, 29300, 0)
    SetChrPos(0x0014, -30300, 1300, 29300, 0)
    FadeIn(1500, 0)
    OP_0D()
    Sleep(1500)

    Fade(1000)
    CameraMove(-63400, -750, 28960, 0)
    SetChrPos(0x0107, -65290, -550, 25260, 90)
    SetChrPos(0x0101, -64140, -550, 26490, 180)
    SetChrFlags(0x0101, 0x0020)
    SetChrFlags(0x0101, 0x0020)
    SetChrFlags(0x0101, 0x0002)
    SetChrFlags(0x0107, 0x0002)
    SetChrFlags(0x0101, 0x0004)
    SetChrFlags(0x0107, 0x0004)
    SetChrChipByIndex(0x0101, 15)
    SetChrChipByIndex(0x0107, 16)
    SetChrSubChip(0x0101, 0)
    SetChrSubChip(0x0107, 0)
    PlaySE(162, 0x00, 0x64)
    PlaySE(455, 0x01, 0x64)
    CameraMove(-65690, -750, 27830, 3000)
    Sleep(400)

    OP_99(0x0101, 0x00, 0x02, 800)
    OP_99(0x0101, 0x02, 0x01, 800)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010080383V#378F#2P呼～真是享受啊，享受。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080384V这还是我第一次泡温泉呢，\n',
            '真是出乎意料的舒服。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080385V#443F虽然没到朵洛希那样痴迷的程度，\n',
            '但还真是挺容易上瘾的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0107, 7)
    Sleep(400)

    ChrTalk(
        0x0107,
        (
            '#0070080386V#391F#5P呵呵……\n',
            '其实我的瘾也挺大的哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080387V从我还小的时候开始，\n',
            '爷爷就经常带我来这里泡温泉呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0101, 3)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010080388V#370F#2P是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x000000C8, 1600, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    OP_99(0x0101, 0x03, 0x05, 800)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010080389V#374F#4P咦，那个门是做什么用的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0107, 1)
    Sleep(400)

    ChrTalk(
        0x0107,
        (
            '#0070080390V#390F#6P啊，刚才不是说过吗，\n',
            '那扇门是连着露天温泉的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080391V里面可是很大的，\n',
            '大概可以十个人一起泡哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080392V#370F#4P哎～是这样啊～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0101, 0x05, 0x03, 800)
    Sleep(100)

    SetChrSubChip(0x0101, 6)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010080393V#377F#2P呼～这样泡一下，\n',
            '感觉之前旅行的疲劳都释放了出来～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0107, 7)
    Sleep(400)

    ChrTalk(
        0x0107,
        (
            '#0070080394V#390F#5P艾丝蒂尔姐姐，\n',
            '你们是徒步旅行的吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080395V为什么不搭乘定期船呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0101, 0x03, 0x02, 800)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010080396V#442F#2P嗯……算是为了修行吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080397V#442F#2P还有……\n',
            '用老爸的话来说，\n',
            '是为了获得在各地修行时的阅历吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0107, 0x07, 0x09, 1200)
    OP_99(0x0107, 0x09, 0x07, 1200)
    OP_99(0x0107, 0x07, 0x09, 1200)
    OP_99(0x0107, 0x09, 0x07, 1200)
    Sleep(400)

    ChrTalk(
        0x0107,
        (
            '#0070080398V#393F#5P卡西乌斯叔叔……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0101, 0x02, 0x04, 800)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010080399V#376F#2P老爸的徒弟雪拉扎德\n',
            '这样对我和约修亚说的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080400V因为老爸以前劝导雪拉姐\n',
            '在修行的时候一定要徒步旅行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080401V要守护一片土地，\n',
            '首先就要自己脚踏实地去看一看……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080402V#396F#5P哇，好帅呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080403V#378F#2P虽然老爸平时总是爱开玩笑，\n',
            '不过关键时刻还是挺靠得住的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0101, 0x04, 0x03, 800)
    Sleep(100)

    SetChrSubChip(0x0101, 6)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010080404V#377F#2P唉……\n',
            '不知他现在又跑到哪里去了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080405V#392F#5P……艾丝蒂尔姐姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0101, 0x03, 0x04, 800)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010080406V#443F#2P啊哈哈，不好意思，\n',
            '这话题好像沉重了点。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080407V#376F#2P不过，游击士为了修行，\n',
            '总不能担心这个那个的而停滞不前吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0101, 0x04, 0x00, 1000)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010080408V#440F#2P现在能做到的……\n',
            '嗯……只有相信老爸他了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080409V#393F#5P相信……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080410V…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x000000C8, 1600, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    OP_99(0x0101, 0x00, 0x04, 1000)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010080411V#370F#2P咦，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0107, 2)
    Sleep(80)

    SetChrSubChip(0x0107, 3)
    Sleep(80)

    SetChrSubChip(0x0107, 2)
    Sleep(80)

    SetChrSubChip(0x0107, 4)
    Sleep(80)

    SetChrSubChip(0x0107, 2)
    Sleep(80)

    SetChrSubChip(0x0107, 3)
    Sleep(80)

    SetChrSubChip(0x0107, 2)
    Sleep(80)

    SetChrSubChip(0x0107, 4)
    Sleep(80)

    SetChrSubChip(0x0107, 2)
    Sleep(400)

    ChrTalk(
        0x0107,
        (
            '#0070080412V#390F#5P不，没什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0107, 0x09, 0x07, 800)
    Sleep(400)

    ChrTalk(
        0x0107,
        (
            '#0070080413V#396F#5P啊……对了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080414V我有一个问题\n',
            '想问艾丝蒂尔姐姐呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080415V#370F#2P有问题要问我？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080416V什么什么？\n',
            '问什么都可以哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080417V#395F#5P嗯嗯，就是～～那个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080418V艾丝蒂尔姐姐和约修亚哥哥\n',
            '是不是已经结婚了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080419V#371F#2P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080420V#396F#5P……（紧张紧张）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    SetChrSubChip(0x0101, 9)
    OP_0D()
    OP_99(0x0101, 0x09, 0x07, 800)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010080421V#370F#2P哎，不好意思。\n',
            '刚才没听清楚你说的那句话。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080422V我和约修亚怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0107, 0x07, 0x05, 800)
    Sleep(400)

    ChrTalk(
        0x0107,
        (
            '#0070080423V#397F#5P啊～嗯，人家是说……\n',
            '你们俩是不是已经结婚了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0101, 15, 0, 300, 4000)

    ChrTalk(
        0x0101,
        (
            '#0010080424V#374F#2P怎、怎、怎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010080425V#372F#2P#3S怎么会有这种想法！？',
            TxtCtl.Enter,
        ),
    )

    SetChrSubChip(0x0101, 10)
    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    OP_99(0x0107, 0x07, 0x09, 1300)
    OP_99(0x0107, 0x09, 0x07, 1300)
    OP_99(0x0107, 0x07, 0x09, 1300)
    OP_99(0x0107, 0x09, 0x07, 1300)
    Sleep(400)

    ChrTalk(
        0x0107,
        (
            '#0070080426V#394F#5P因、因为你们用同一个姓氏啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080427V而且你们的长相又不像兄妹，\n',
            '我还以为一定是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0101, 11)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010080428V#444F#2P长、长相不像是因为\n',
            '我们没有血缘关系啦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080429V姓氏相同是因为\n',
            '约修亚是老爸的养子啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080430V#393F#5P啊，原来是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080431V#395F嘿嘿，对不起。\n',
            '我之前一直误会你们俩是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0101, 12)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010080432V#377F#2P根、根本就是天大的误会……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080433V而且……\n',
            '我和约修亚都只有１６岁。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080434V结婚什么的还早得很呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080435V#395F#5P说、说的也是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080436V无论两人怎样喜欢对方，\n',
            '都不能这么早就结婚的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080437V#377F#2P……（晕倒）',
            TxtCtl.Enter,
        ),
    )

    SetChrSubChip(0x0101, 13)
    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010080438V#375F#2P#3S都、都说了嘛！\n',
            '我和约修亚根本\n',
            '就不是什么恋人啦！',
            TxtCtl.Enter,
        ),
    )

    SetChrSubChip(0x0101, 14)
    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080439V#375F#2P#3S只是家人啦，家人！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    OP_99(0x0107, 0x0A, 0x0C, 1000)
    OP_99(0x0107, 0x0C, 0x0A, 1000)
    Sleep(400)

    ChrTalk(
        0x0107,
        (
            '#0070080440V#394F#5P是、是这样吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0101, 0x0E, 0x10, 1000)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010080441V#377F#2P当然是这样啦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080442V………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0101, 11)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010080443V#444F#2P那个，提妲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080444V我和约修亚之间……\n',
            '看起来像那样的关系吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080445V#393F#5P那样的关系？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0101, 17)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010080446V#441F#2P就、就是说……\n',
            '恋、恋人那样的……关系啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080447V爱意浓浓、情意绵绵……\n',
            '如胶似漆、难舍难分……之类的啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0107, 0x0B, 0x0C, 800)
    Sleep(400)

    ChrTalk(
        0x0107,
        (
            '#0070080448V#395F#5P啊……\n',
            '倒没那样的感觉呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080449V可是可是，你们总是在一起，\n',
            '相处得又那么自然、那么温馨，\n',
            '感觉两人好像彼此都互通心意似的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0101, 10)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010080450V#442F#2P唔，如果是你说的那样，\n',
            '倒是可能有那么的一点……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080451V可是这种……\n',
            '不是家人或亲友间的关系吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080452V也许，我和约修亚之间\n',
            '真的一直都是那样的关系……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_AD('ED6_DT04/C_VIS022._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(1200)

    OP_77(0x00, 0x00, 0x00, 0x00, 0x00000000)
    OP_AD('ED6_DT04/C_VIS020._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(1200)

    OP_AD('ED6_DT04/C_VIS023._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(1200)

    OP_AD('ED6_DT04/C_VIS021._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(1200)

    OP_AD('ED6_DT04/C_VIS024._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(1200)

    OP_77(0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_AE(0x000001F4)
    Sleep(500)

    OP_62(0x0101, 0x000000C8, 1600, 0x10, 0x13, 0x000000FA, 0x01)
    Sleep(1500)

    ChrTalk(
        0x0101,
        (
            '#0010080453V#375F#2P#3S（呀！我在想什么呀～！）',
            TxtCtl.Enter,
        ),
    )

    SetChrSubChip(0x0101, 19)
    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    SetChrSubChip(0x0101, 18)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010080454V#441F#2P（这么说，到现在为止，\n',
            '　我竟然连那样令人害羞的事都坦然地……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0107, 0x0B, 0x0A, 800)
    Sleep(400)

    ChrTalk(
        0x0107,
        (
            '#0070080455V#393F#5P？？？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080456V艾丝蒂尔姐姐？\n',
            '你的脸……好红呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0101, 0x0C, 0x0A, 1000)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010080457V#378F#2P咦咦咦咦……\n',
            '没什么啦，什么都没有！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080458V哎呀～话说回来，\n',
            '这里的温泉真的很舒服不是吗！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080459V不过对血液循环的促进过于有效了吧。\n',
            '头开始有点晕乎乎的了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080460V#393F#5P是、是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080461V#371F#2P说、说起来，\n',
            '外面就是露天澡堂是吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080462V头有点晕了，\n',
            '我稍微出去散步一下哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080463V#393F#5P啊，好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0101, 0x01, 0x00, 0x000F)
    SetChrSubChip(0x0107, 1)
    Sleep(500)

    ChrTalk(
        0x0107,
        (
            '#0070080464V#393F#3P啊，对了……\n',
            '艾丝蒂尔姐姐，露天澡堂是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080465V#394F#3P男女混浴……的啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0000)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1E2B',
    )

    SetChrStatus(0x0000, 0xFB, 0)

    def _loc_1E2B(): pass

    label('loc_1E2B')

    If(
        (
            (Expr.Eval, "OP_42(0x0001)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1E3E',
    )

    SetChrStatus(0x0001, 0xFB, 0)

    def _loc_1E3E(): pass

    label('loc_1E3E')

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1E51',
    )

    SetChrStatus(0x0002, 0xFB, 0)

    def _loc_1E51(): pass

    label('loc_1E51')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1E64',
    )

    SetChrStatus(0x0003, 0xFB, 0)

    def _loc_1E64(): pass

    label('loc_1E64')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1E77',
    )

    SetChrStatus(0x0005, 0xFB, 0)

    def _loc_1E77(): pass

    label('loc_1E77')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1E8A',
    )

    SetChrStatus(0x0004, 0xFB, 0)

    def _loc_1E8A(): pass

    label('loc_1E8A')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1E9D',
    )

    SetChrStatus(0x0006, 0xFB, 0)

    def _loc_1E9D(): pass

    label('loc_1E9D')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1EB0',
    )

    SetChrStatus(0x0007, 0xFB, 0)

    def _loc_1EB0(): pass

    label('loc_1EB0')

    FadeOut(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x10000000)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T3201._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1ECC(): pass

    label('loc_1ECC')

    Return()

# id: 0x000F offset: 0x1ECD
@scena.Code('func_0F_1ECD')
def func_0F_1ECD():
    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ClearChrFlags(0x0101, 0x0020)
    ClearChrFlags(0x0101, 0x0002)
    ClearChrFlags(0x0101, 0x0004)
    SetChrFlags(0x0101, 0x1000)
    SetChrChipByIndex(0x0101, 0)
    SetChrSubChip(0x0101, 0)
    ChrJumpTo(0x00FE, -63690, 0, 27770, 1200, 6000)
    ChrWalkTo(0x00FE, -65920, 250, 28980, 5000, 0x00)
    SetChrDirection(0x00FE, 270, 800)
    OP_70(0x0006, 60)
    Sleep(60)

    ChrWalkTo(0x0101, -67680, 0, 29390, 5000, 0x00)
    Sleep(500)

    OP_72(0x0006, 0x0800)
    PlaySE(7, 0x00, 0x64)
    OP_6F(0x0006, 60)
    OP_70(0x0006, 0)

    Return()

# id: 0x0010 offset: 0x1F6D
@scena.Code('func_10_1F6D')
def func_10_1F6D():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1F8B',
    )

    OP_99(0x00FE, 0x0E, 0x10, 1300)
    OP_99(0x00FE, 0x10, 0x0F, 1300)

    Jump('func_10_1F6D')

    def _loc_1F8B(): pass

    label('loc_1F8B')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
