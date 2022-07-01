import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4111_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4111   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '赫穆特'),
    TXT(0x02, '诺琪'),
    TXT(0x03, '马丁'),
    TXT(0x04, '玛丽安'),
    TXT(0x05, '海伦娜'),
    TXT(0x06, '卡特莉娜夫人'),
    TXT(0x07, '达丽娅'),
    TXT(0x08, '莉安妮'),
    TXT(0x09, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4111.x'
    header.mapIndex       = 1
    header.bgm            = 14
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T4111_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1C3A
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
        ('ED6_DT07/CH01220._CH', 'ED6_DT07/CH01220P._CP'),
        ('ED6_DT07/CH01230._CH', 'ED6_DT07/CH01230P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH02490._CH', 'ED6_DT07/CH02490P._CP'),
        ('ED6_DT07/CH01180._CH', 'ED6_DT07/CH01180P._CP'),
        ('ED6_DT07/CH01350._CH', 'ED6_DT07/CH01350P._CP'),
        ('ED6_DT07/CH01480._CH', 'ED6_DT07/CH01480P._CP'),
        ('ED6_DT27/CH03005._CH', 'ED6_DT27/CH03005P._CP'),
    ]

# id: 0x10002 offset: 0xF2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 60000,
            z                   = 0,
            y                   = 2950,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 60530,
            z                   = 0,
            y                   = 62340,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = 115690,
            z                   = 0,
            y                   = 60750,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 125180,
            z                   = 0,
            y                   = 63830,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = 114980,
            z                   = 0,
            y                   = -55400,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = -1040,
            z                   = 0,
            y                   = -56350,
            direction           = 3,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = 6600,
            z                   = 0,
            y                   = -56390,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = -2470,
            z                   = 0,
            y                   = 61010,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
    )

# id: 0x10003 offset: 0x1F2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x1F2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x1F2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 1520,
            triggerZ            = 0,
            triggerY            = 64780,
            triggerRange        = 1000,
            actorX              = 1520,
            actorZ              = 2000,
            actorY              = 64780,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0000,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x216
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_28B',
    )

    SetChrPos(0x0008, 59640, 0, 1740, 90)
    SetChrPos(0x0009, 60760, 0, 1740, 270)
    SetChrFlags(0x0008, 0x0010)
    SetChrFlags(0x0009, 0x0010)
    SetChrPos(0x000A, 123980, 0, 1080, 90)
    SetChrPos(0x000B, 126360, 0, 1830, 270)
    SetChrPos(0x000C, 126360, 0, 740, 270)
    SetChrFlags(0x000A, 0x0010)
    CreateThread(0x000A, 0x00, 0x06, 0x0002)

    Jump('loc_41A')

    def _loc_28B(): pass

    label('loc_28B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_2B7',
    )

    SetChrPos(0x0008, 59640, 0, 1740, 90)
    SetChrPos(0x0009, 60760, 0, 1740, 270)

    Jump('loc_41A')

    def _loc_2B7(): pass

    label('loc_2B7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_327',
    )

    SetChrPos(0x0008, 55510, 0, 62080, 270)
    SetChrPos(0x000A, 115170, 0, 60900, 90)
    SetChrPos(0x000B, 116170, 0, 60910, 270)
    SetChrPos(0x000C, 120270, 0, 68790, 0)
    CreateThread(0x000A, 0x00, 0x06, 0x0002)
    SetChrFlags(0x000A, 0x0010)
    SetChrFlags(0x000B, 0x0010)
    SetChrPos(0x000D, -2640, 0, 64080, 179)

    Jump('loc_41A')

    def _loc_327(): pass

    label('loc_327')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_397',
    )

    SetChrPos(0x0008, 55510, 0, 62080, 270)
    SetChrPos(0x000B, 114980, 0, -55400, 0)
    SetChrPos(0x000C, 120270, 0, 68790, 0)
    SetChrPos(0x000D, -1600, 0, 64260, 90)
    SetChrPos(0x000E, -2180, 0, 63520, 90)
    SetChrPos(0x000F, -1460, 0, 64920, 180)

    Jump('loc_41A')

    def _loc_397(): pass

    label('loc_397')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3E9',
    )

    SetChrPos(0x0008, 55510, 0, 62080, 270)
    SetChrPos(0x000B, 114980, 0, -55400, 0)
    SetChrPos(0x000C, 120270, 0, 68790, 0)
    SetChrPos(0x000D, -2640, 0, 64080, 179)

    Jump('loc_41A')

    def _loc_3E9(): pass

    label('loc_3E9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_41A',
    )

    SetChrFlags(0x0008, 0x0080)
    SetChrPos(0x000B, 114980, 0, -55400, 0)
    SetChrPos(0x000C, 120270, 0, 68790, 0)

    Jump('loc_41A')

    def _loc_41A(): pass

    label('loc_41A')

    Return()

# id: 0x0001 offset: 0x41B
@scena.Code('Init')
def Init():
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
        'loc_437',
    )

    OP_B1('t4111_y')

    Jump('loc_440')

    def _loc_437(): pass

    label('loc_437')

    OP_B1('t4111_n')

    def _loc_440(): pass

    label('loc_440')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_44E',
    )

    CreateThread(0x000F, 0x00, 0x06, 0x0002)

    def _loc_44E(): pass

    label('loc_44E')

    OP_64(0x00, 0x0001)

    If(
        (
            (Expr.Eval, "OP_29(0x00C4, 0x00, 0x04)"),
            (Expr.Eval, "OP_29(0x00C4, 0x01, 0x0004)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x00C4, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_471',
    )

    OP_65(0x00, 0x0001)

    def _loc_471(): pass

    label('loc_471')

    Return()

# id: 0x0002 offset: 0x472
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_495',
    )

    OP_8D(0x00FE, 113830, 62500, 117900, 58880, 2000)

    Jump('ReInit')

    def _loc_495(): pass

    label('loc_495')

    Return()

# id: 0x0003 offset: 0x496
@scena.Code('func_03_496')
def func_03_496():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4B9',
    )

    OP_8D(0x00FE, -1150, 59690, -3770, 62520, 3000)

    Jump('func_03_496')

    def _loc_4B9(): pass

    label('loc_4B9')

    Return()

# id: 0x0004 offset: 0x4BA
@scena.Code('func_04_4BA')
def func_04_4BA():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Return,
        ),
        'loc_4C7',
    )

    Jump('loc_7E6')

    def _loc_4C7(): pass

    label('loc_4C7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_4FA',
    )

    ChrTalk(
        0x00FE,
        (
            '这、这局面，也实在是\n',
            '不能钓鱼了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7E6')

    def _loc_4FA(): pass

    label('loc_4FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_60A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5A1',
    )

    ChrTalk(
        0x00FE,
        (
            '怎么说呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为这次的事件，\n',
            '我终于明白了被抛弃是什么感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我准备与妻子一边享受钓鱼\n',
            '一边重新开始人生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然心情有点复杂……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_607')

    def _loc_5A1(): pass

    label('loc_5A1')

    ChrTalk(
        0x00FE,
        (
            '因为这次的事件，\n',
            '我终于明白了被抛弃是什么感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我准备与妻子一边享受钓鱼\n',
            '一边重新开始人生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_607(): pass

    label('loc_607')

    Jump('loc_7E6')

    def _loc_60A(): pass

    label('loc_60A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_649',
    )

    ChrTalk(
        0x00FE,
        (
            '不过我已经决定了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我准备……\n',
            '放弃钓鱼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7E6')

    def _loc_649(): pass

    label('loc_649')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_703',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6D4',
    )

    ChrTalk(
        0x00FE,
        (
            '特级钓师……真令人吃惊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这不是钓公师团中的\n',
            '最高称号吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '想不到我妻子\n',
            '已经进步到如此程度了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_700')

    def _loc_6D4(): pass

    label('loc_6D4')

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
            '………………呼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_700(): pass

    label('loc_700')

    Jump('loc_7E6')

    def _loc_703(): pass

    label('loc_703')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_70D',
    )

    Jump('loc_7E6')

    def _loc_70D(): pass

    label('loc_70D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_7E6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7AB',
    )

    ChrTalk(
        0x00FE,
        (
            '妻子抛开喜爱钓鱼的我\n',
            '加入了钓公师团。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我工作离家期间，\n',
            '她好像频繁前往湖那边……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉哟哟……\n',
            '这样一来水平差距就越来越大了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_7E6')

    def _loc_7AB(): pass

    label('loc_7AB')

    ChrTalk(
        0x00FE,
        (
            '而且我还没有加入\n',
            '钓公师团。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这真是莫大的屈辱……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7E6(): pass

    label('loc_7E6')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x7EA
@scena.Code('func_05_7EA')
def func_05_7EA():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Return,
        ),
        'loc_7F7',
    )

    Jump('loc_E59')

    def _loc_7F7(): pass

    label('loc_7F7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_8FA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_89F',
    )

    ChrTalk(
        0x00FE,
        (
            '你在说什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样下去的话你永远也\n',
            '不能入团了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就是在这种局面下才要\n',
            '才要通过垂钓来使心情平静……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所谓钓鱼的心\n',
            '即是明镜止水！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    Jump('loc_8F7')

    def _loc_89F(): pass

    label('loc_89F')

    ChrTalk(
        0x00FE,
        (
            '就是在这种局面下才要\n',
            '才要通过垂钓来使心情平静……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所谓钓鱼的心\n',
            '即是明镜止水！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8F7(): pass

    label('loc_8F7')

    Jump('loc_E59')

    def _loc_8FA(): pass

    label('loc_8FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02CD, 3, 0x166B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_ACA',
    )

    ChrTalk(
        0x00FE,
        (
            '呵呵，我最近\n',
            '买了新的钓竿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为从开始钓鱼到现在\n',
            '都用着同一根钓竿，\n',
            '我想也该要买新的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么……\n',
            '该怎么处理旧的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我丈夫也只用又新\n',
            '又高级的东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    ChrTurnDirection(0x00FE, 0x0101, 400)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '你……会钓鱼吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x0101,
        (
            '#1004F咦？　嗯，多少会点……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1013F（她、她是怎么知道的？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，这个\n',
            '就送给你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.Item, ItemTable['竹竿']),
            (TxtCtl.SetColor, 0x0),
            '收下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    AddItem(ItemTable['竹竿'], 1)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#1008F谢、谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，拿去尽情地钓吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x166B)

    Jump('loc_E59')

    def _loc_ACA(): pass

    label('loc_ACA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_B51',
    )

    ChrTalk(
        0x00FE,
        (
            '我准备下次休假时\n',
            '教丈夫钓鱼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我丈夫准备请假\n',
            '带我去垂钓旅行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然发生了不少事，\n',
            '不过现在我……感觉挺幸福的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E59')

    def _loc_B51(): pass

    label('loc_B51')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_C1A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BD8',
    )

    ChrTalk(
        0x00FE,
        (
            '从昨天起我丈夫\n',
            '就开始想不开了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就为那点事，真没出息……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以前刚遇见他时，\n',
            '他明明是个充满勇气的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    Jump('loc_C17')

    def _loc_BD8(): pass

    label('loc_BD8')

    ChrTalk(
        0x00FE,
        (
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我可能逼丈夫\n',
            '有点过火了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C17(): pass

    label('loc_C17')

    Jump('loc_E59')

    def _loc_C1A(): pass

    label('loc_C1A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_C77',
    )

    ChrTalk(
        0x00FE,
        (
            '听说我获得了\n',
            '特级钓师的称号\n',
            '丈夫便沉默了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，这次看来\n',
            '很有效果。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E59')

    def _loc_C77(): pass

    label('loc_C77')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_D8E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D28',
    )

    ChrTalk(
        0x00FE,
        (
            '听我说，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次我……\n',
            '获得了『钓公师团』授予的\n',
            '『特级钓师』称号。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在我就和罗伊德老师\n',
            '并驾齐驱了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '等丈夫回来之后\n',
            '我一定要好好炫耀炫耀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    Jump('loc_D8B')

    def _loc_D28(): pass

    label('loc_D28')

    ChrTalk(
        0x00FE,
        (
            '这次我……\n',
            '获得了钓公师团授予的\n',
            '『特级钓师』称号。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '等丈夫回来之后\n',
            '我一定要好好炫耀炫耀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D8B(): pass

    label('loc_D8B')

    Jump('loc_E59')

    def _loc_D8E(): pass

    label('loc_D8E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_E59',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E28',
    )

    ChrTalk(
        0x00FE,
        (
            '丈夫以前只顾工作和钓鱼，\n',
            '对我看都不看一眼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以我决定要在钓鱼\n',
            '上胜过丈夫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这轻蔑家庭的罪……\n',
            '我要他彻彻底底地偿还。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    Jump('loc_E59')

    def _loc_E28(): pass

    label('loc_E28')

    ChrTalk(
        0x00FE,
        (
            '最近我特喜欢送\n',
            '丈夫出门。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哦呵呵呵呵！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E59(): pass

    label('loc_E59')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0xE5D
@scena.Code('func_06_E5D')
def func_06_E5D():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_EA5',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯～那么接下来\n',
            '开始我家的避难训练！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '首先是点名！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1047')

    def _loc_EA5(): pass

    label('loc_EA5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_F13',
    )

    ChrTalk(
        0x00FE,
        (
            '哈哈哈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '果然我们这边的人\n',
            '没有我管着不行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好～努力工作来攒出\n',
            '全体人员的旅行费用～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1047')

    def _loc_F13(): pass

    label('loc_F13')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_F80',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，亚尔摩温泉啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '家庭旅行……这可是有板有眼的\n',
            '节日呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是不是该做个记号呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1047')

    def _loc_F80(): pass

    label('loc_F80')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_FDF',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，饱餐一顿虽然能够提神……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，还是喜好这类……\n',
            '有竞争性的活动啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1047')

    def _loc_FDF(): pass

    label('loc_FDF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_1009',
    )

    ChrTalk(
        0x00FE,
        (
            '哟，好像有股很香的味道……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1047')

    def _loc_1009(): pass

    label('loc_1009')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_1047',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，真和平……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和平真无聊……\n',
            '也没心情工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1047(): pass

    label('loc_1047')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x104B
@scena.Code('func_07_104B')
def func_07_104B():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_107D',
    )

    ChrTalk(
        0x00FE,
        (
            '呵呵，在这种时候\n',
            '感觉他真可靠。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11FA')

    def _loc_107D(): pass

    label('loc_107D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_10AB',
    )

    ChrTalk(
        0x00FE,
        (
            '呵呵，他看来有精神了，太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11FA')

    def _loc_10AB(): pass

    label('loc_10AB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_10F5',
    )

    ChrTalk(
        0x00FE,
        (
            '拜托，带我去\n',
            '亚尔摩温泉吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '当然旅游全部\n',
            '由你来策划。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11FA')

    def _loc_10F5(): pass

    label('loc_10F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1167',
    )

    ChrTalk(
        0x00FE,
        (
            '就算给他做好吃的，\n',
            '也只能让他精神一小会儿，\n',
            '家里的经济也要被压迫……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，到底是怎么了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11FA')

    def _loc_1167(): pass

    label('loc_1167')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_11BE',
    )

    ChrTalk(
        0x00FE,
        (
            '看来果然只有用美味\n',
            '才能让那个人打起精神来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只能尝试各种方式了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11FA')

    def _loc_11BE(): pass

    label('loc_11BE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_11FA',
    )

    ChrTalk(
        0x00FE,
        (
            '真拿他没办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '得让他有精神\n',
            '好好地工作……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11FA(): pass

    label('loc_11FA')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x11FE
@scena.Code('func_08_11FE')
def func_08_11FE():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_125F',
    )

    ChrTalk(
        0x00FE,
        (
            '因为现在是在紧急情况下，\n',
            '我觉得这是很重要的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '爸爸这么高兴\n',
            '真令人在意～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1442')

    def _loc_125F(): pass

    label('loc_125F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_12B3',
    )

    ChrTalk(
        0x00FE,
        (
            '结论是我家的老大\n',
            '果然是妈妈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '爸爸只能一辈子\n',
            '被操控于鼓掌之间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1442')

    def _loc_12B3(): pass

    label('loc_12B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_1300',
    )

    ChrTalk(
        0x00FE,
        (
            '原来如此……不愧是妈妈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '得做个笔记……\n',
            '将来说不定有用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1442')

    def _loc_1300(): pass

    label('loc_1300')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1341',
    )

    ChrTalk(
        0x00FE,
        (
            '妈妈接下来会怎么做呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我就慢慢\n',
            '观战吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1442')

    def _loc_1341(): pass

    label('loc_1341')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_139D',
    )

    ChrTalk(
        0x00FE,
        (
            '为了给爸爸精神起来，\n',
            '今天准备了上好的煎牛排哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '妈妈是不是\n',
            '太宠爸爸了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1442')

    def _loc_139D(): pass

    label('loc_139D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_1442',
    )

    ChrTalk(
        0x00FE,
        (
            '爸爸如果没像武术大会和诞辰庆典\n',
            '这样的活动就会变得颓废。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为只有在有活动时\n',
            '他才能管这个家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你不觉得这很正常吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为在我家妈妈最有实力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1442(): pass

    label('loc_1442')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x1446
@scena.Code('func_09_1446')
def func_09_1446():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_14B1',
    )

    ChrTalk(
        0x00FE,
        (
            '想不到不能使用导力器\n',
            '这么令人不安……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不知他是否平安……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '至少能来个信\n',
            '也好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_176F')

    def _loc_14B1(): pass

    label('loc_14B1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1538',
    )

    ChrTalk(
        0x00FE,
        (
            '虽说是在港口，\n',
            '可也离这儿不远啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '丈夫不在家的时候\n',
            '我一定要好好保护莉安妮……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我不想让她再受政变时\n',
            '那样的罪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_176F')

    def _loc_1538(): pass

    label('loc_1538')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_15D0',
    )

    ChrTalk(
        0x00FE,
        (
            '政变结束之后\n',
            '我丈夫好象一直很忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算去格兰赛尔，\n',
            '也没什么时间过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '至少能让莉安妮\n',
            '见上一面也好啊，\n',
            '不过现在可能也没办法……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_176F')

    def _loc_15D0(): pass

    label('loc_15D0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_161E',
    )

    ChrTalk(
        0x00FE,
        (
            '真没想到会有那种人\n',
            '潜入我家……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '莉安妮没事真是\n',
            '谢天谢地。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_176F')

    def _loc_161E(): pass

    label('loc_161E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_16A3',
    )

    ChrTalk(
        0x00FE,
        (
            '前不久希德中校\n',
            '来这里玩过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我孙女也很喜欢\n',
            '亲近中校……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，中校非常喜欢小孩子，\n',
            '孩子们也能明白这点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_176F')

    def _loc_16A3(): pass

    label('loc_16A3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_1713',
    )

    ChrTalk(
        0x00FE,
        (
            '我那讨厌游击士的丈夫，\n',
            '最近也常提到协会两个字呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可能是受卡西乌斯的影响。\n',
            '我真有点惊讶……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_176F')

    def _loc_1713(): pass

    label('loc_1713')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_176F',
    )

    ChrTalk(
        0x00FE,
        (
            '听到卡西乌斯准将要复出的时候\n',
            '我丈夫那股子高兴劲儿啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真想让你们也看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_176F(): pass

    label('loc_176F')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x1773
@scena.Code('func_0A_1773')
def func_0A_1773():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_17D6',
    )

    ChrTalk(
        0x00FE,
        (
            '这种时候家里只有女人\n',
            '真叫人不安～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '至少我要代替老爷来\n',
            '保护夫人和莉安妮小姐！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19F0')

    def _loc_17D6(): pass

    label('loc_17D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1851',
    )

    ChrTalk(
        0x00FE,
        (
            '哇，港口那边好像有\n',
            '坦克大闹过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听说那坦克是冲着\n',
            '市区去的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……也就是说本来\n',
            '有可能经过这里～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19F0')

    def _loc_1851(): pass

    label('loc_1851')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_18B3',
    )

    ChrTalk(
        0x00FE,
        (
            '我倒是更担心那挂念着\n',
            '老爷的太太自身的健康。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '她多少应该吃点好吃的\n',
            '来补充体力～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19F0')

    def _loc_18B3(): pass

    label('loc_18B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_18FF',
    )

    ChrTalk(
        0x00FE,
        (
            '晚上我会\n',
            '好好地锁门！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一定不能再让那种\n',
            '可疑的人进来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19F0')

    def _loc_18FF(): pass

    label('loc_18FF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1938',
    )

    ChrTalk(
        0x00FE,
        (
            '莉安妮小姐还饿着肚子，\n',
            '我得抓紧了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19F0')

    def _loc_1938(): pass

    label('loc_1938')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_198F',
    )

    ChrTalk(
        0x00FE,
        (
            '老爷最近似乎有点变化……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不知是不是我多心，他好像\n',
            '比以前更爱笑了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19F0')

    def _loc_198F(): pass

    label('loc_198F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_19F0',
    )

    ChrTalk(
        0x00FE,
        (
            '老爷……摩尔根将军他\n',
            '是个非常可怕的人～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，呵呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1S他拿夫人最没辙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19F0(): pass

    label('loc_19F0')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x19F4
@scena.Code('func_0B_19F4')
def func_0B_19F4():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1A41',
    )

    ChrTalk(
        0x00FE,
        (
            '太阳落山后\n',
            '房间里变得漆黑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '太阳一直\n',
            '不落山就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C1E')

    def _loc_1A41(): pass

    label('loc_1A41')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1A93',
    )

    ChrTalk(
        0x00FE,
        (
            '今天奶奶也\n',
            '不让我出去……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近理查德哥哥也\n',
            '不来玩，真没劲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C1E')

    def _loc_1A93(): pass

    label('loc_1A93')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_1AFB',
    )

    ChrTalk(
        0x00FE,
        (
            '下次要让爷爷带我去\n',
            '离宫～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以前虽然在离宫发生了可怕的事，\n',
            '不过和爷爷在一起我就不怕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C1E')

    def _loc_1AFB(): pass

    label('loc_1AFB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1B41',
    )

    ChrTalk(
        0x00FE,
        (
            '我说我说，\n',
            '怪盗是个怎样的人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '莉安妮\n',
            '好想见见他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C1E')

    def _loc_1B41(): pass

    label('loc_1B41')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1B82',
    )

    ChrTalk(
        0x00FE,
        (
            '今天玩了很久，\n',
            '肚子饿了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '晚饭还没好吗～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C1E')

    def _loc_1B82(): pass

    label('loc_1B82')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_1BD5',
    )

    ChrTalk(
        0x00FE,
        (
            '不久前我在大圣堂\n',
            '碰到了穿白色衣服的女孩子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真想和那孩子玩玩～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C1E')

    def _loc_1BD5(): pass

    label('loc_1BD5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_1C1E',
    )

    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '啊，你是救过莉安妮的\n',
            '艾丝蒂尔！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是来找我玩的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C1E(): pass

    label('loc_1C1E')

    TalkEnd(0x00FE)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
