import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3201_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3201   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '朵洛希'),
    TXT(0x02, '毛婆婆'),
    TXT(0x03, '拜舍尔'),
    TXT(0x04, '艾德'),
    TXT(0x05, '林'),
    TXT(0x06, '莉西亚'),
    TXT(0x07, '希利尔'),
    TXT(0x08, '艾缇'),
    TXT(0x09, '拉克'),
    TXT(0x0A, '希玛'),
    TXT(0x0B, '库安'),
    TXT(0x0C, '西加罗'),
    TXT(0x0D, '艾德尔'),
    TXT(0x0E, '托兰特平原道方向'),
    TXT(0x0F, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3201.x'
    header.mapIndex       = 1
    header.bgm            = 84
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x32F1
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
        ('ED6_DT07/CH02070._CH', 'ED6_DT07/CH02070P._CP'),
        ('ED6_DT07/CH02430._CH', 'ED6_DT07/CH02430P._CP'),
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
    ]

# id: 0x10002 offset: 0x12A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            x                   = 2590,
            z                   = 250,
            y                   = 5360,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
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
            dword_10            = 6,
            chipIndex           = 6,
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
            dword_10            = 7,
            chipIndex           = 7,
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
            dword_10            = 8,
            chipIndex           = 8,
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
            dword_10            = 9,
            chipIndex           = 9,
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
            dword_10            = 10,
            chipIndex           = 10,
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
            dword_10            = 11,
            chipIndex           = 11,
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
            dword_10            = 12,
            chipIndex           = 12,
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
            dword_10            = 13,
            chipIndex           = 13,
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
            dword_10            = 14,
            chipIndex           = 14,
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
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            x                   = -30790,
            z                   = -2000,
            y                   = 15330,
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

# id: 0x10003 offset: 0x2EA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x2EA
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 28950,
            y           = 1000,
            z           = 4030,
            range       = 2500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000013,
        ),
        ScenaEventData(
            x           = 980,
            y           = -250,
            z           = 18420,
            range       = 1250,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000014,
        ),
        ScenaEventData(
            x           = 42330,
            y           = 5750,
            z           = 36020,
            range       = 1250,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000015,
        ),
    )

# id: 0x10005 offset: 0x34A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 40000,
            triggerZ            = 6000,
            triggerY            = 49730,
            triggerRange        = 800,
            actorX              = 40000,
            actorZ              = 7000,
            actorY              = 49730,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0010,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 42130,
            triggerZ            = 0,
            triggerY            = -860,
            triggerRange        = 1250,
            actorX              = 44880,
            actorZ              = 3000,
            actorY              = 1020,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0012,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x392
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_3A0',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x000F)

    def _loc_3A0(): pass

    label('loc_3A0')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000069, 'loc_3AC'),
        (-1, 'loc_3C2'),
    )

    def _loc_3AC(): pass

    label('loc_3AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 7, 0x527)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3BF',
    )

    SetScenaFlags(ScenaFlag(0x00A4, 7, 0x527))
    Event(0, 0x000E)

    def _loc_3BF(): pass

    label('loc_3BF')

    Jump('loc_3C2')

    def _loc_3C2(): pass

    label('loc_3C2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_40E',
    )

    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, 30590, 4500, 35260, 249)
    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x0010, 28630, 4000, 36530, 176)
    ClearChrFlags(0x0012, 0x0080)
    SetChrPos(0x0012, 28800, 4000, 33220, 0)

    Jump('loc_613')

    def _loc_40E(): pass

    label('loc_40E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_45A',
    )

    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, 41610, 6000, 48020, 219)
    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x0010, 9750, 2000, 15450, 181)
    ClearChrFlags(0x0012, 0x0080)
    SetChrPos(0x0012, 9820, 2000, 13580, 351)

    Jump('loc_613')

    def _loc_45A(): pass

    label('loc_45A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_4A6',
    )

    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x0010, 39080, 6000, 47390, 7)
    ClearChrFlags(0x0012, 0x0080)
    SetChrPos(0x0012, 40560, 6000, 47840, 342)
    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, 39640, 6000, 44670, 353)

    Jump('loc_613')

    def _loc_4A6(): pass

    label('loc_4A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_4B0',
    )

    Jump('loc_613')

    def _loc_4B0(): pass

    label('loc_4B0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_4E6',
    )

    ClearChrFlags(0x0014, 0x0080)
    SetChrPos(0x0014, 47620, 0, 7310, 180)
    ClearChrFlags(0x0013, 0x0080)
    SetChrPos(0x0013, 48380, 0, 7130, 180)

    Jump('loc_613')

    def _loc_4E6(): pass

    label('loc_4E6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_51C',
    )

    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x000A, 16830, 2500, 13990, 11)
    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x0010, 39080, 6000, 47390, 7)

    Jump('loc_613')

    def _loc_51C(): pass

    label('loc_51C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Return,
        ),
        'loc_568',
    )

    ClearChrFlags(0x0013, 0x0080)
    SetChrPos(0x0013, 13770, 2500, 18660, 90)
    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x0010, 17190, 2500, 13960, 351)
    ClearChrFlags(0x0012, 0x0080)
    SetChrPos(0x0012, 15890, 2500, 13840, 32)

    Jump('loc_613')

    def _loc_568(): pass

    label('loc_568')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_5CA',
    )

    ClearChrFlags(0x0013, 0x0080)
    SetChrPos(0x0013, 13770, 2500, 18660, 90)
    ClearChrFlags(0x0014, 0x0080)
    SetChrPos(0x0014, 13780, 2500, 19720, 153)
    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x0010, 17190, 2500, 13960, 351)
    ClearChrFlags(0x0012, 0x0080)
    SetChrPos(0x0012, 15890, 2500, 13840, 32)

    Jump('loc_613')

    def _loc_5CA(): pass

    label('loc_5CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_613',
    )

    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, 13400, 2500, 18050, 224)
    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x0010, 14390, 2500, 16520, 263)
    ClearChrFlags(0x0012, 0x0080)
    SetChrPos(0x0012, 12490, 2000, 16460, 41)

    def _loc_613(): pass

    label('loc_613')

    Return()

# id: 0x0001 offset: 0x614
@scena.Code('Init')
def Init():
    OP_16(0x02, 4000, -98000, -107000, 196692)
    OP_72(0x000B, 0x0010)
    OP_1B(0x00, 0x00, 0x0011)

    If(
        (
            (Expr.GetChrWork, 0x101, 0x1E),
            (Expr.PushLong, 0x11C),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_644',
    )

    OP_28(0x002A, 0x01, 0x0800)

    def _loc_644(): pass

    label('loc_644')

    OP_64(0x01, 0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x002E, 0x00, 0x04)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x002E, 0x01, 0x0010)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_664',
    )

    OP_65(0x01, 0x0001)

    def _loc_664(): pass

    label('loc_664')

    Return()

# id: 0x0002 offset: 0x665
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_67A',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_67A(): pass

    label('loc_67A')

    Return()

# id: 0x0003 offset: 0x67B
@scena.Code('func_03_67B')
def func_03_67B():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_688',
    )

    Jump('loc_871')

    def _loc_688(): pass

    label('loc_688')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_692',
    )

    Jump('loc_871')

    def _loc_692(): pass

    label('loc_692')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_69C',
    )

    Jump('loc_871')

    def _loc_69C(): pass

    label('loc_69C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_6A6',
    )

    Jump('loc_871')

    def _loc_6A6(): pass

    label('loc_6A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_6F5',
    )

    ChrTalk(
        0x00FE,
        (
            '月光映照下的\n',
            '东方风格的庭园……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，简直就像梦幻一样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_871')

    def _loc_6F5(): pass

    label('loc_6F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_7A1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_74D',
    )

    ChrTalk(
        0x00FE,
        (
            '唔～我想去后山看看啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '村子里都已经\n',
            '没有可以去探险的地方了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_79E')

    def _loc_74D(): pass

    label('loc_74D')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '这里面的后山\n',
            '好像有温泉的源头。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我很想去看看，\n',
            '但是村民不允许进去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_79E(): pass

    label('loc_79E')

    Jump('loc_871')

    def _loc_7A1(): pass

    label('loc_7A1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Return,
        ),
        'loc_7AB',
    )

    Jump('loc_871')

    def _loc_7AB(): pass

    label('loc_7AB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_86A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_80E',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，\n',
            '那个好像是特产店啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，虽然我有点心急，\n',
            '不过现在就想去看一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_867')

    def _loc_80E(): pass

    label('loc_80E')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '如我所料，\n',
            '这是个恬静的温泉胜地啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到处都是东方的风格，\n',
            '也让人感到很新鲜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_867(): pass

    label('loc_867')

    Jump('loc_871')

    def _loc_86A(): pass

    label('loc_86A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_871',
    )

    def _loc_871(): pass

    label('loc_871')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x875
@scena.Code('func_04_875')
def func_04_875():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_882',
    )

    Jump('loc_A47')

    def _loc_882(): pass

    label('loc_882')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_88C',
    )

    Jump('loc_A47')

    def _loc_88C(): pass

    label('loc_88C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_896',
    )

    Jump('loc_A47')

    def _loc_896(): pass

    label('loc_896')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_8A0',
    )

    Jump('loc_A47')

    def _loc_8A0(): pass

    label('loc_8A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_948',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_8E6',
    )

    ChrTalk(
        0x00FE,
        (
            '在温泉里泡得有点晕，\n',
            '吹吹夜晚的冷气真是舒服啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_945')

    def _loc_8E6(): pass

    label('loc_8E6')

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

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
            '能把讨厌的事都抛在脑后。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_945(): pass

    label('loc_945')

    Jump('loc_A47')

    def _loc_948(): pass

    label('loc_948')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_952',
    )

    Jump('loc_A47')

    def _loc_952(): pass

    label('loc_952')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Return,
        ),
        'loc_95C',
    )

    Jump('loc_A47')

    def _loc_95C(): pass

    label('loc_95C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_995',
    )

    ChrTalk(
        0x00FE,
        (
            '哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '艾德尔那家伙\n',
            '到底跑到哪儿去了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A47')

    def _loc_995(): pass

    label('loc_995')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_A47',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_9DB',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，能来这里真是好啊。\n',
            '这个温泉好像能治病呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A47')

    def _loc_9DB(): pass

    label('loc_9DB')

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '啊，是因为温泉吧。\n',
            '觉得空气也很潮湿呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要在这里，\n',
            '妻子就会忘掉购物欲，\n',
            '能好好地放松一下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A47(): pass

    label('loc_A47')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0xA4B
@scena.Code('func_05_A4B')
def func_05_A4B():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_A58',
    )

    Jump('loc_B58')

    def _loc_A58(): pass

    label('loc_A58')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_A62',
    )

    Jump('loc_B58')

    def _loc_A62(): pass

    label('loc_A62')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_A6C',
    )

    Jump('loc_B58')

    def _loc_A6C(): pass

    label('loc_A6C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_A76',
    )

    Jump('loc_B58')

    def _loc_A76(): pass

    label('loc_A76')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_A80',
    )

    Jump('loc_B58')

    def _loc_A80(): pass

    label('loc_A80')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_B3D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_AE2',
    )

    ChrTalk(
        0x00FE,
        (
            '……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '…………嗯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这口井……\n',
            '大小正好适合做钓鱼池啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B3A')

    def _loc_AE2(): pass

    label('loc_AE2')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '嗯，\n',
            '偶尔把钓鱼的事忘掉，\n',
            '休息一下也不错啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '简直感觉\n',
            '像心灵被清洗了一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B3A(): pass

    label('loc_B3A')

    Jump('loc_B58')

    def _loc_B3D(): pass

    label('loc_B3D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Return,
        ),
        'loc_B47',
    )

    Jump('loc_B58')

    def _loc_B47(): pass

    label('loc_B47')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_B51',
    )

    Jump('loc_B58')

    def _loc_B51(): pass

    label('loc_B51')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_B58',
    )

    def _loc_B58(): pass

    label('loc_B58')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0xB5C
@scena.Code('func_06_B5C')
def func_06_B5C():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0xB63
@scena.Code('func_07_B63')
def func_07_B63():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0xB6A
@scena.Code('func_08_B6A')
def func_08_B6A():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_C49',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_BE7',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，喂，库安。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你在刚才的战斗中\n',
            '一直在用导力魔法，\n',
            '那可不行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '使用魔法\n',
            '需要待机时间啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C46')

    def _loc_BE7(): pass

    label('loc_BE7')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '还在玩武术大会游戏……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且是在大马路上，\n',
            '不觉得害羞吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是个小鬼头。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C46(): pass

    label('loc_C46')

    Jump('loc_EEC')

    def _loc_C49(): pass

    label('loc_C49')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_D2F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_CB9',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，\n',
            '在蔡斯发生大事的同时，\n',
            '这边的水泵也出了故障。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不愧是解乏又温暖的\n',
            '亚尔摩温泉啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D2C')

    def _loc_CB9(): pass

    label('loc_CB9')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '嗯，不愧是蔡斯啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '恐怖事件……\n',
            '真是了不得的大新闻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '《利贝尔通讯》中\n',
            '也会登载这个爆炸性新闻吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D2C(): pass

    label('loc_D2C')

    Jump('loc_EEC')

    def _loc_D2F(): pass

    label('loc_D2F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_DD0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_D86',
    )

    ChrTalk(
        0x00FE,
        (
            '好啦，拉克。\n',
            '不能去栅栏那边啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要不然我又要\n',
            '被毛婆婆骂了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DCD')

    def _loc_D86(): pass

    label('loc_D86')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '只是去后山而已，\n',
            '有什么了不起的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们啊，\n',
            '真是一群小鬼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DCD(): pass

    label('loc_DCD')

    Jump('loc_EEC')

    def _loc_DD0(): pass

    label('loc_DD0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_DDA',
    )

    Jump('loc_EEC')

    def _loc_DDA(): pass

    label('loc_DDA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_DE4',
    )

    Jump('loc_EEC')

    def _loc_DE4(): pass

    label('loc_DE4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_DEE',
    )

    Jump('loc_EEC')

    def _loc_DEE(): pass

    label('loc_DEE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Return,
        ),
        'loc_DF8',
    )

    Jump('loc_EEC')

    def _loc_DF8(): pass

    label('loc_DF8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_E02',
    )

    Jump('loc_EEC')

    def _loc_E02(): pass

    label('loc_E02')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_EEC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_E63',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯～\n',
            '蔡斯的人果然都很酷啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '该怎么说呢，\n',
            '就像这样给人以干练的感觉呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EEC')

    def _loc_E63(): pass

    label('loc_E63')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E8B',
    )

    ChrTalk(
        0x00FE,
        (
            '哇，哥哥真帅呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EAE')

    def _loc_E8B(): pass

    label('loc_E8B')

    ChrTalk(
        0x00FE,
        (
            '哇，\n',
            '那边的哥哥看起来真帅呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EAE(): pass

    label('loc_EAE')

    ChrTalk(
        0x00FE,
        (
            '喂，喂？\n',
            '你们是从蔡斯来的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在那边\n',
            '正流行什么啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EEC(): pass

    label('loc_EEC')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0xEF0
@scena.Code('func_09_EF0')
def func_09_EF0():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0xEF7
@scena.Code('func_0A_EF7')
def func_0A_EF7():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0xEFE
@scena.Code('func_0B_EFE')
def func_0B_EFE():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_F87',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_F41',
    )

    ChrTalk(
        0x00FE,
        (
            '上啊～！\n',
            '看我的导力魔法！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '咚～～啪！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F84')

    def _loc_F41(): pass

    label('loc_F41')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '喂，莉西亚姐姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x000D, 400)

    ChrTalk(
        0x00FE,
        (
            '你是裁判，\n',
            '要好好看着才行哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F84(): pass

    label('loc_F84')

    Jump('loc_1208')

    def _loc_F87(): pass

    label('loc_F87')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_1015',
    )

    ChrTalk(
        0x00FE,
        (
            '嘿，你知道吗？\n',
            '蔡斯出事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像是不得了的大事件。\n',
            '这个村子里\n',
            '也有游击士来调查了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊～\n',
            '好想看看真正的游击士呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1208')

    def _loc_1015(): pass

    label('loc_1015')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_10D3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1066',
    )

    ChrTalk(
        0x00FE,
        (
            '啊啊～\n',
            '真想去后山探险一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '村子里面\n',
            '我都已经玩够了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10D0')

    def _loc_1066(): pass

    label('loc_1066')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '温泉的源头\n',
            '一定非常大吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '温泉水从那里\n',
            '涌出了几十年，\n',
            '也没有见它干涸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊～真想去看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10D0(): pass

    label('loc_10D0')

    Jump('loc_1208')

    def _loc_10D3(): pass

    label('loc_10D3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_10DD',
    )

    Jump('loc_1208')

    def _loc_10DD(): pass

    label('loc_10DD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_10E7',
    )

    Jump('loc_1208')

    def _loc_10E7(): pass

    label('loc_10E7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_10F1',
    )

    Jump('loc_1208')

    def _loc_10F1(): pass

    label('loc_10F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1186',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1143',
    )

    ChrTalk(
        0x00FE,
        (
            '唔～果然很奇怪啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '绝对没错。\n',
            '因为我每天都看着呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1183')

    def _loc_1143(): pass

    label('loc_1143')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '哎～真奇怪啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就在刚才，\n',
            '温泉的水流看起来有点弱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1183(): pass

    label('loc_1183')

    Jump('loc_1208')

    def _loc_1186(): pass

    label('loc_1186')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_1208',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_11CE',
    )

    ChrTalk(
        0x00FE,
        (
            '这么年轻\n',
            '就来泡温泉啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '肯定是相当累了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1208')

    def _loc_11CE(): pass

    label('loc_11CE')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '啊，有客人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎～真少见啊。\n',
            '这么年轻的客人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1208(): pass

    label('loc_1208')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x120C
@scena.Code('func_0C_120C')
def func_0C_120C():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x1213
@scena.Code('func_0D_1213')
def func_0D_1213():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_12A1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_1262',
    )

    ChrTalk(
        0x00FE,
        (
            '可恶！不能认输！\n',
            '我也发动魔法！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿呀呀呀呀～～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_129E')

    def _loc_1262(): pass

    label('loc_1262')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '嘿嘿嘿～说起诞辰庆典，\n',
            '果然还是武术大会最吸引人吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_129E(): pass

    label('loc_129E')

    Jump('loc_152C')

    def _loc_12A1(): pass

    label('loc_12A1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_1323',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_12ED',
    )

    ChrTalk(
        0x00FE,
        (
            '真是件大事啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然好像和我们村子\n',
            '没什么关系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1320')

    def _loc_12ED(): pass

    label('loc_12ED')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '蔡斯出了大事吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '城市里果然可怕啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1320(): pass

    label('loc_1320')

    Jump('loc_152C')

    def _loc_1323(): pass

    label('loc_1323')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_142C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_13A5',
    )

    ChrTalk(
        0x00FE,
        (
            '……但是，\n',
            '莉西亚姐姐也真是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们都已经是大人了，\n',
            '不要管我们那么多嘛。\n',
            '有这时间倒不如去旅馆帮帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1429')

    def _loc_13A5(): pass

    label('loc_13A5')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '后山的温泉源头吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然我经常听说，\n',
            '但是从来没有亲眼见过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，\n',
            '虽说不能越过这个栅栏，\n',
            '但我还是很想去看看啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1429(): pass

    label('loc_1429')

    Jump('loc_152C')

    def _loc_142C(): pass

    label('loc_142C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_1436',
    )

    Jump('loc_152C')

    def _loc_1436(): pass

    label('loc_1436')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_1440',
    )

    Jump('loc_152C')

    def _loc_1440(): pass

    label('loc_1440')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_144A',
    )

    Jump('loc_152C')

    def _loc_144A(): pass

    label('loc_144A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_14A6',
    )

    ChrTalk(
        0x00FE,
        (
            '拉克那家伙\n',
            '说温泉的样子有点奇怪……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是吗？\n',
            '对我来说没感到什么不同。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_152C')

    def _loc_14A6(): pass

    label('loc_14A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_152C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_14FC',
    )

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，拉克真是小鬼啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说到情侣，\n',
            '果然要一起去温泉才浪漫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_152C')

    def _loc_14FC(): pass

    label('loc_14FC')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '嘿嘿嘿，很浪漫啊。\n',
            '情侣一起到温泉旅游。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_152C(): pass

    label('loc_152C')

    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x1530
@scena.Code('func_0E_1530')
def func_0E_1530():
    EventBegin(0x00)
    ClearMapFlags(0x00000001)
    CameraMove(53490, 2500, 9430, 0)
    OP_67(0, 5410, -10000, 0)
    CameraSetDistance(3600, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 52820, 2500, -3040, 270)
    SetChrPos(0x0101, 42000, 2500, -2430, 45)
    SetChrPos(0x0102, 41080, 2500, -1680, 45)
    SetChrPos(0x0107, 40890, 2500, -2710, 45)
    FadeIn(1000, 0)
    CameraMove(40870, 2500, -2620, 5000)

    ChrTalk(
        0x0101,
        (
            '#0010080344V#501F哇～天色已经这么暗了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080345V#010F东方风格的庭院……的确很风雅。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0280080346V#2P啊～！\n',
            '是小艾你们啊～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    CameraMove(46060, 2500, -3350, 0)
    OP_67(0, 5850, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(180000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 41530, 2500, -2520, 90)
    SetChrPos(0x0107, 41120, 2500, -3580, 90)
    SetChrPos(0x0102, 40830, 2500, -1900, 90)
    SetChrFlags(0x0107, 0x0004)
    SetChrFlags(0x0102, 0x0004)

    @scena.Lambda('lambda_16E0')
    def lambda_16E0():
        ChrWalkTo(0x00FE, 47170, 2500, -2920, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_16E0)

    OP_0D()
    WaitForThreadExit(0x0008, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010080347V#501F咦，朵洛希？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_171F')
    def lambda_171F():
        ChrWalkTo(0x00FE, 45160, 2500, -2850, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_171F)

    Sleep(300)

    @scena.Lambda('lambda_173F')
    def lambda_173F():
        ChrWalkTo(0x00FE, 44450, 2500, -3640, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_173F)

    Sleep(300)

    @scena.Lambda('lambda_175F')
    def lambda_175F():
        ChrWalkTo(0x00FE, 44520, 2500, -2310, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_175F)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#0280080348V#151F嘿嘿～～\n',
            '小艾你们也来泡澡吗～？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280080349V这里的澡堂很好哦～\n',
            '又大又舒适。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280080350V不过要是泡过头了，\n',
            '脑袋会晕晕乎乎的哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080351V#004F难道说你回到旅馆之后，\n',
            '就一～直泡到现在？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0280080352V#151F没错。\n',
            '哇～真是好舒服哦～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280080353V#153F咦，这个女孩子是……\n',
            '我们还是第一次见面吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080354V#560F啊，初次见面……\n',
            '我叫提妲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0280080355V#150F哎～初次见面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280080356V我叫朵洛希。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280080357V我在王都的一家杂志社里\n',
            '当一名摄影师的哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080358V#061F摄影师……\n',
            '哇～好棒的职业哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0280080359V#151F嘿嘿，过奖啦～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280080360V#150F啊，对了～\n',
            '小艾你们今天\n',
            '也在这家旅馆过夜吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280080361V可以的话待会儿一起吃饭吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080362V#501F嗯，那也好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080363V#010F在我们泡完温泉之前，\n',
            '可以请你先等一会儿吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0280080364V#151F嗯，没问题～\n',
            '那我就一边喝水果牛奶一边等～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280080365V那么，待会见哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1A98')
    def lambda_1A98():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_1A98')

    DispatchAsync2(0x0101, 0x0001, lambda_1A98)

    @scena.Lambda('lambda_1AA9')
    def lambda_1AA9():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_1AA9')

    DispatchAsync2(0x0102, 0x0001, lambda_1AA9)

    @scena.Lambda('lambda_1ABA')
    def lambda_1ABA():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_1ABA')

    DispatchAsync2(0x0107, 0x0001, lambda_1ABA)

    ChrMoveTo(0x0102, 44260, 2500, -2800, 2000, 0x00)
    SetChrFlags(0x0008, 0x0040)
    ChrWalkTo(0x0008, 45900, 2500, -2310, 3000, 0x00)
    ChrWalkTo(0x0008, 40600, 2500, -2850, 3000, 0x00)
    OP_70(0x0005, 29)
    OP_73(0x0005)
    ChrWalkTo(0x0008, 38950, 2500, -2790, 3000, 0x00)
    SetChrFlags(0x0008, 0x0080)
    Sleep(500)

    OP_72(0x0005, 0x0800)
    PlaySE(7, 0x00, 0x64)
    OP_6F(0x0005, 29)
    OP_70(0x0005, 0)
    OP_73(0x0005)
    OP_71(0x0005, 0x0800)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0107, 0xFF)
    TerminateThread(0x0102, 0xFF)
    ClearChrFlags(0x0107, 0x0004)
    ClearChrFlags(0x0102, 0x0004)
    EventEnd(0x00)

    Return()

# id: 0x000F offset: 0x1B67
@scena.Code('func_0F_1B67')
def func_0F_1B67():
    PlaySE(455, 0x01, 0x64)
    EventBegin(0x00)
    ClearMapFlags(0x00000001)
    OP_11(0xEF, 0xEC, 0xF1, 34100, 39400, 0)
    SetMapFlags(0x00000010)
    CameraMove(67020, 1000, 15120, 0)
    OP_67(0, 9190, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    SetChrChipByIndex(0x0101, 2)
    SetChrFlags(0x0101, 0x1000)
    SetChrChipByIndex(0x0107, 3)
    SetChrFlags(0x0107, 0x1000)
    SetChrChipByIndex(0x0102, 4)
    SetChrFlags(0x0102, 0x1000)
    SetChrFlags(0x0107, 0x0080)
    SetChrPos(0x0101, 68840, 2000, 6530, 0)
    SetChrPos(0x0102, 66060, 1000, 21730, 225)
    FadeIn(1000, 0)
    ChrWalkTo(0x0101, 66710, 2000, 11190, 3000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010080466V#441F（呼～好紧张……\n',
            '　心脏还在咚咚地跳呢……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080467V（我……\n',
            '　刚才到底是怎么了……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080468V（到现在为止，\n',
            '　都没对约修亚有过这样的感觉……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080469V#377F（…………………………）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080470V#376F（啊啊啊，不想了！\n',
            '　一味苦恼根本不是我的性格！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1D2A')
    def lambda_1D2A():
        CameraMove(65160, 1000, 17980, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1D2A)

    @scena.Lambda('lambda_1D42')
    def lambda_1D42():
        OP_6C(11000, 3500)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_1D42)

    ChrWalkTo(0x0101, 63050, 2000, 10940, 2000, 0x00)
    ChrWalkTo(0x0101, 61980, 1000, 15170, 2000, 0x00)
    ChrWalkTo(0x0101, 65090, 1000, 17900, 1000, 0x00)
    SetChrDirection(0x0101, 225, 300)
    ChrTurnDirection(0x0102, 0x0101, 0)

    ChrTalk(
        0x0101,
        (
            '#0010080471V#371F哇～好舒服～！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080472V里面的澡堂也很不错，\n',
            '不过外面的可是更特别呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080473V#370F嗯～\n',
            '又大又舒适……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0102,
        '少年的声音',
        (
            '#0020080474V……话说在前头，\n',
            '这里面可不许游泳的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080475V#444F嘁……\n',
            '我才不会那么做呢！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080476V…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080477V#374F………………哎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1EB8')
    def lambda_1EB8():
        CameraMove(65630, 1000, 20540, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1EB8)

    OP_67(0, 8970, -10000, 1000)
    ChrTurnDirection(0x0101, 0x0102, 400)
    Fade(2500)
    ClearMapFlags(0x00000010)
    Sleep(2500)

    OP_6C(45000, 2500)

    ChrTalk(
        0x0102,
        (
            '#0020080478V#380F哟，艾丝蒂尔，\n',
            '我已经先进来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080479V#389F哈哈……说起来，\n',
            '这幅样子还真是有点难为情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080480V#374F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080481V#389F不、不过温泉\n',
            '真是出乎意料的有效啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080482V伤口似乎好多了，\n',
            '体内的疲劳也都释放出来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080483V对我们游击士来说，\n',
            '这种调节是最合适不过的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080484V#374F……………………………\n',
            '……………………………\n',
            '……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080485V#388F喂，那个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080486V在这种气氛下保持沉默，\n',
            '会让人觉得很不自然的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)

    ChrTalk(
        0x0101,
        (
            '#0010080487V#373F哎……唔，啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0101, 15, 0, 1000, 3000)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010080488V#375F#30A#5S呀啊啊啊啊啊啊啊！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    FadeOut(3000, 0, -1)
    CameraSetDistance(15700, 2000)
    Sleep(2000)

    CameraMove(67030, 2000, 13540, 0)
    CameraSetDistance(2800, 0)
    OP_6C(225000, 0)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, 66930, 2000, 12000, 0)
    ClearChrFlags(0x0107, 0x0080)
    SetChrPos(0x0101, 65690, 1000, 15170, 180)
    SetChrPos(0x0107, 64620, 1000, 15010, 180)
    SetChrPos(0x0102, 65430, 1000, 16430, 180)
    Sleep(500)

    FadeIn(2000, 0)
    OP_1E()
    OP_0D()

    ChrTalk(
        0x0009,
        (
            '#0570080489V#682F发出那么大声的惨叫，\n',
            '我还以为岀了啥事呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080490V真是会添乱的小姑娘呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080491V#377F呜……对不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0570080492V#682F听好了。\n',
            '这个露天温泉是男女混浴的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080493V你刚才没看清楚\n',
            '更衣室外那张大大的告示吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080494V#373F呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080495V#387F……真是的，\n',
            '肯定是连看都没看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0570080496V#681F再说了，裸体被看个一两次，\n',
            '也没啥好慌张的嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080497V女孩子的肌肤就是要\n',
            '保养得漂漂亮亮给人看的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080498V#393F是、是吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080499V#372F提妲，不要相信呀！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080500V而且而且……\n',
            '我根本就没被人看到裸体呀！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0570080501V#680F哎呀，就别管那么多啦。\n',
            '泡个澡而已，亲亲热热地去泡就是啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080502V这里本来就是\n',
            '给一家人开开心心混浴的嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080503V好了，我先走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0009, 180, 400)

    @scena.Lambda('lambda_2490')
    def lambda_2490():
        ChrWalkTo(0x0009, 68760, 2000, 6530, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2490)

    Sleep(1000)

    @scena.Lambda('lambda_24B0')
    def lambda_24B0():
        CameraMove(65269, 1000, 15580, 2000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_24B0)

    WaitForThreadExit(0x0009, 0x0002)
    OP_6F(0x0008, 29)
    OP_70(0x0008, 29)
    Sleep(1000)

    OP_72(0x0008, 0x0800)
    PlaySE(7, 0x00, 0x64)
    OP_70(0x0008, 0)
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010080504V#377F唉～……\n',
            '突然觉得好累……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080505V#444F唔～都怪你，约修亚。\n',
            '搞出那么难为情的事情！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0102, 400)

    ChrTalk(
        0x0102,
        (
            '#0020080506V#387F为什么是我……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080507V#388F根本就是你一个人\n',
            '引起了那么大的骚动。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080508V连更衣室的告示也没看到，\n',
            '这就是平日注意力不够的证明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080509V#379F要、要你多事啦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080510V真是的……\n',
            '一点儿也不可爱！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080511V#382F哦，是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080512V#385F算了，没关系。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080513V反正就算被你觉得可爱，\n',
            '我也没什么好高兴的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080514V#372F你、你说什么～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080515V#383F说到底，刚刚那算什么。\n',
            '看到人家就像见鬼似的发出惨叫……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080516V你竟然会有那样的反应，\n',
            '……我真是做梦都没想到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080517V#441F那……那是……\n',
            '因为时机实在是太……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080518V反正不是因为\n',
            '讨厌见到约修亚你啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080519V#385F没关系，不用勉强。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080520V#380F反正碍事的人已经洗好了，\n',
            '你们俩就继续泡吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080521V#375F什、什么嘛！？\n',
            '碍事什么的，我根本一句也没说过呀！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080522V约修亚是笨蛋！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080523V#382F哼……谁才是笨蛋啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080524V#391F嘻嘻……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0102, 0x0101, 400)
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010080525V#441F你、你看！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080526V都怪你。\n',
            '连提妲都在笑我们了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080527V#388F为什么又怪我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2946')
    def lambda_2946():
        OP_69(0x0107, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2946)

    @scena.Lambda('lambda_2954')
    def lambda_2954():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2954)

    ChrTurnDirection(0x0102, 0x0107, 400)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0102,
        (
            '#0020080528V#389F抱、抱歉。\n',
            '让你看到这么丢人的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080529V#396F啊，没有啦。\n',
            '只是忍不住笑了，真不好意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080530V其实呢……\n',
            '我挺羡慕你们俩的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080531V#374F#3P羡、羡慕？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080532V#384F哎……为什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080533V#390F我没有兄弟姐妹，\n',
            '也没有跟别人吵过架。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080534V爷爷很疼我，\n',
            '也很少很少会责骂我……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080535V还有的是，\n',
            '爸爸妈妈又很少在我身边……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080536V#374F#3P哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080537V#382F那个……\n',
            '提妲的爸爸妈妈是……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080538V#390F我爸爸妈妈是导力技术者，\n',
            '所以需要一直呆在国外。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080539V听说是到导力器还没普及的地方\n',
            '去做技术指导……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080540V而且……\n',
            '他们俩已经好几年没回来过呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080541V#373F#3P是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080542V#383F那会……很寂寞吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080543V#396F也没有啦。\n',
            '因为还有爷爷和我在一起嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080544V而且中央工房的员工对我也很好，\n',
            '大家都是很亲切的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080545V#395F不过……\n',
            '见到艾丝蒂尔姐姐你们之后，\n',
            '我就总觉得有点羡慕……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080546V嘿嘿，也许这就是\n',
            '所谓得不到的东西总是好的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080547V#382F提妲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080548V#440F#3P…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080549V#376F我有个好主意哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080550V#393F咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080551V#384F艾丝蒂尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080552V#371F#3P从现在开始，\n',
            '我就做提妲的姐姐吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080553V而约修亚嘛，就做哥哥好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080554V#394F哎哎！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080555V#387F唉……\n',
            '又说这么唐突的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080556V#379F#3P什么呀，你有意见吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080557V#381F没有……\n',
            '这本来是艾丝蒂尔的风格。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080558V我也没意见。\n',
            '只要提妲觉得合适的话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080559V#396F……啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080560V#395F谢、谢谢……\n',
            '艾丝蒂尔姐姐、约修亚哥哥。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080561V我、我……\n',
            '实在是太高兴了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080562V#371F#3P那好，就这样决定了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080563V#376F啊，对了对了。\n',
            '以后说话可不要那么见外哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080564V嘿嘿～\n',
            '当然我们也会比较随便的啦㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080565V#389F是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080566V以后只要像和博士说话那样，\n',
            '轻松点自然点就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080567V#397F啊，嗯……\n',
            '轻松点自然点说话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080568V…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080569V#396F艾丝蒂尔姐姐，\n',
            '还有约修亚哥哥。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080570V#395F……这、这样行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080571V#371F#3P嗯，非常好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080572V#389F以后我们就是三兄妹了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T3223._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0010 offset: 0x3101
@scena.Code('func_10_3101')
def func_10_3101():
    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上着锁，无法打开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0011 offset: 0x3151
@scena.Code('func_11_3151')
def func_11_3151():
    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_31C7',
    )

    ChrTurnDirection(0x0102, 0x0001, 400)

    ChrTalk(
        0x0102,
        (
            '#0020080368V#010F晚上的平原很危险。\n',
            '我们还是回去吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080369V想散步的话，在村子里走走就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_321C')

    def _loc_31C7(): pass

    label('loc_31C7')

    ChrTurnDirection(0x0102, 0x0000, 400)

    ChrTalk(
        0x0102,
        (
            '#0020080370V#010F晚上的平原很危险。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080371V想散步的话，\n',
            '在村子里走走就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_321C(): pass

    label('loc_321C')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0012 offset: 0x3238
@scena.Code('func_12_3238')
def func_12_3238():
    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '发现了一个油纸包。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '里面放着',
            (TxtCtl.SetColor, 0x2),
            '艾尔贝啄木鸟的生态',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(0x0343, 1)
    OP_64(0x01, 0x0001)
    OP_28(0x002E, 0x01, 0x0010)
    TalkEnd(0x00FF)

    Return()

# id: 0x0013 offset: 0x32B9
@scena.Code('func_13_32B9')
def func_13_32B9():
    OP_13(0x0088)

    Return()

# id: 0x0014 offset: 0x32BD
@scena.Code('func_14_32BD')
def func_14_32BD():
    OP_13(0x0087)

    Return()

# id: 0x0015 offset: 0x32C1
@scena.Code('func_15_32C1')
def func_15_32C1():
    OP_13(0x0089)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
