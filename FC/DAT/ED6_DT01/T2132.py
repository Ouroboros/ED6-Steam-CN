import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2132_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2132   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '亚内斯特'),
    TXT(0x02, '奈尔'),
    TXT(0x03, '杜南公爵'),
    TXT(0x04, '管家菲利普'),
    TXT(0x05, '鲁特尔'),
    TXT(0x06, '兰达老人'),
    TXT(0x07, '米优'),
    TXT(0x08, '西加罗'),
    TXT(0x09, '艾德尔'),
    TXT(0x0A, '西蒙'),
    TXT(0x0B, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2132.x'
    header.mapIndex       = 1
    header.bgm            = 12
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x42EB
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
        ('ED6_DT07/CH02470._CH', 'ED6_DT07/CH02470P._CP'),
        ('ED6_DT07/CH01570._CH', 'ED6_DT07/CH01570P._CP'),
        ('ED6_DT07/CH02140._CH', 'ED6_DT07/CH02140P._CP'),
        ('ED6_DT07/CH02060._CH', 'ED6_DT07/CH02060P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT06/CH20086._CH', 'ED6_DT06/CH20086P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        (None, 'ED6_DT07/CH01140P._CP'),
    ]

# id: 0x10002 offset: 0x106
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -1900,
            z                   = 0,
            y                   = 11500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 24500,
            z                   = 0,
            y                   = 6100,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = 24500,
            z                   = 0,
            y                   = 6100,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 24500,
            z                   = 0,
            y                   = 6100,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = -42540,
            z                   = 0,
            y                   = 1360,
            direction           = 286,
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
            x                   = -47700,
            z                   = 0,
            y                   = 1570,
            direction           = 265,
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
            x                   = -45810,
            z                   = 0,
            y                   = 3660,
            direction           = 275,
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
            x                   = -43270,
            z                   = 0,
            y                   = 28470,
            direction           = 79,
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
            x                   = -45290,
            z                   = 0,
            y                   = 26250,
            direction           = 269,
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
            x                   = 27950,
            z                   = 0,
            y                   = 49500,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
    )

# id: 0x10003 offset: 0x246
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x246
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x246
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -2020,
            triggerZ            = 0,
            triggerY            = 10280,
            triggerRange        = 400,
            actorX              = -1900,
            actorZ              = 1500,
            actorY              = 11500,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x26A
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_274',
    )

    Jump('loc_2DE')

    def _loc_274(): pass

    label('loc_274')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_283',
    )

    ClearChrFlags(0x0011, 0x0080)

    Jump('loc_2DE')

    def _loc_283(): pass

    label('loc_283')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_28D',
    )

    Jump('loc_2DE')

    def _loc_28D(): pass

    label('loc_28D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 2, 0x41A)),
            Expr.Return,
        ),
        'loc_2DE',
    )

    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x000A, -5790, 0, 84500, 0)
    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, -8410, 0, 83450, 0)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x0011, 0x0080)

    def _loc_2DE(): pass

    label('loc_2DE')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x76),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2FB',
    )

    SetChrPos(0x0000, -8880, 0, 930, 45)

    def _loc_2FB(): pass

    label('loc_2FB')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x77),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_318',
    )

    SetChrPos(0x0000, -12970, 0, 4970, 45)

    def _loc_318(): pass

    label('loc_318')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x78),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_335',
    )

    SetChrPos(0x0000, -11310, 0, 41790, 45)

    def _loc_335(): pass

    label('loc_335')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_351',
    )

    SetMapFlags(0x10000000)
    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x10),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, 0x0010)

    def _loc_351(): pass

    label('loc_351')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000070, 'loc_361'),
        (0x00000073, 'loc_377'),
        (-1, 'loc_38D'),
    )

    def _loc_361(): pass

    label('loc_361')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 2, 0x41A)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 1, 0x419)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_374',
    )

    SetScenaFlags(ScenaFlag(0x0083, 2, 0x41A))
    Event(0, 0x000E)

    def _loc_374(): pass

    label('loc_374')

    Jump('loc_38D')

    def _loc_377(): pass

    label('loc_377')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 2, 0x41A)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_38A',
    )

    SetScenaFlags(ScenaFlag(0x0083, 3, 0x41B))
    Event(0, 0x0011)

    def _loc_38A(): pass

    label('loc_38A')

    Jump('loc_38D')

    def _loc_38D(): pass

    label('loc_38D')

    Return()

# id: 0x0001 offset: 0x38E
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Or,
            Expr.Return,
        ),
        'loc_3AF',
    )

    OP_B1('t2132_y')

    Jump('loc_3B8')

    def _loc_3AF(): pass

    label('loc_3AF')

    OP_B1('t2132_n')

    def _loc_3B8(): pass

    label('loc_3B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 2, 0x41A)),
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3C9',
    )

    OP_1B(0x00, 0x00, 0x0012)

    def _loc_3C9(): pass

    label('loc_3C9')

    Return()

# id: 0x0002 offset: 0x3CA
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3DF',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_3DF(): pass

    label('loc_3DF')

    Return()

# id: 0x0003 offset: 0x3E0
@scena.Code('func_03_3E0')
def func_03_3E0():
    Call(0, 0x0004)

    Return()

# id: 0x0004 offset: 0x3E5
@scena.Code('func_04_3E5')
def func_04_3E5():
    TalkBegin(0x0008)
    FadeOut(300, 0, 100)

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
        10,
        100,
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '休息\n'),
            TXT(0x02, '离开\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_441',
    )

    OP_0D()
    OP_A9(0x21)
    OP_56(0x00)
    TalkEnd(0x0008)

    Return()

    def _loc_441(): pass

    label('loc_441')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_452',
    )

    TalkEnd(0x0008)

    Return()

    def _loc_452(): pass

    label('loc_452')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_4B2',
    )

    ChrTalk(
        0x0008,
        (
            '市长被逮捕了，\n',
            '给本市的政务也带来了麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '而且，\n',
            '对旅游业也会造成许多影响。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_116F')

    def _loc_4B2(): pass

    label('loc_4B2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_525',
    )

    ChrTalk(
        0x0008,
        (
            '本酒店的主人\n',
            '名字叫做诺曼，\n',
            '他住在城市的南街区。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '他是一个在观光事业的发展上\n',
            '费尽心思的实业家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_116F')

    def _loc_525(): pass

    label('loc_525')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_5C2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_58C',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '杜南公爵还要在\n',
            '卢安停留一段日子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '他好像非常\n',
            '喜欢这个城市。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5BF')

    def _loc_58C(): pass

    label('loc_58C')

    ChrTalk(
        0x0008,
        (
            '杜南公爵还要在\n',
            '卢安停留一段日子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5BF(): pass

    label('loc_5BF')

    Jump('loc_116F')

    def _loc_5C2(): pass

    label('loc_5C2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_678',
    )

    ChrTalk(
        0x0008,
        (
            '马上就要到王立学院\n',
            '举行学园祭的时候了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '学园祭每年都能吸引\n',
            '很多毕业的学生回来参加。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '毕业生中也有很多知名人士，\n',
            '每到这个时候他们都会\n',
            '过来光顾我们的酒店呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_116F')

    def _loc_678(): pass

    label('loc_678')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 4, 0x42C)),
            Expr.Return,
        ),
        'loc_770',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_704',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '公爵原本准备\n',
            '乘船出去戏水的，\n',
            '却被告知小船正在整修中……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '还是请他先去\n',
            '艾尔·雷登的瀑布观光吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '……呼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_76D')

    def _loc_704(): pass

    label('loc_704')

    ChrTalk(
        0x0008,
        (
            '公爵原本准备\n',
            '乘船出去戏水的，\n',
            '却被告知小船正在整修中……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '还是请他先去\n',
            '艾尔·雷登的瀑布观光吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_76D(): pass

    label('loc_76D')

    Jump('loc_116F')

    def _loc_770(): pass

    label('loc_770')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 2, 0x42A)),
            Expr.Return,
        ),
        'loc_89C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_872',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '怎么了？你们好像很着急的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '出什么事了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#002F对不起，主管先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '有一件事想请问您，\n',
            '酒店提供租船的服务对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '嗯，要租船的话，\n',
            '请从那边的楼梯下去，\n',
            '然后从右边的门口出去就是了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#005F下楼后右拐是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '谢了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_899')

    def _loc_872(): pass

    label('loc_872')

    ChrTalk(
        0x0008,
        (
            '要租船的话\n',
            '请从楼下右边出口出去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_899(): pass

    label('loc_899')

    Jump('loc_116F')

    def _loc_89C(): pass

    label('loc_89C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_984',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_923',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '两位客人，\n',
            '昨天给你们添了非常大的麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '请两位放心，\n',
            '下次绝对不会再发生同样的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '真是非常抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_981')

    def _loc_923(): pass

    label('loc_923')

    ChrTalk(
        0x0008,
        (
            '两位客人，\n',
            '昨天给你们添了非常大的麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '请两位放心，\n',
            '下次绝对不会再发生同样的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_981(): pass

    label('loc_981')

    Jump('loc_116F')

    def _loc_984(): pass

    label('loc_984')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 2, 0x41A)),
            Expr.Return,
        ),
        'loc_B05',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0099, 5, 0x4CD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AB4',
    )

    SetScenaFlags(ScenaFlag(0x0099, 5, 0x4CD))

    ChrTalk(
        0x0008,
        (
            '两位客人，这次由于我们的招待不周\n',
            '而给你们带了诸多不便。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '可以的话，\n',
            '请先在这里喝些饮料吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    AddItem(0x01A2, 1)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '鲜榨果汁',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '至少请接受我们的歉意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我们原想为你们提供优质的服务，\n',
            '但是居然发生了这样的事情，\n',
            '真是十分抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B02')

    def _loc_AB4(): pass

    label('loc_AB4')

    ChrTalk(
        0x0008,
        (
            '我们原想为你们提供优质的服务，\n',
            '但是居然发生了这样的事情，\n',
            '真是十分抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B02(): pass

    label('loc_B02')

    Jump('loc_116F')

    def _loc_B05(): pass

    label('loc_B05')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 1, 0x419)),
            Expr.Return,
        ),
        'loc_B6B',
    )

    ChrTalk(
        0x0008,
        (
            '二位的房间\n',
            '就在本酒店的顶楼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我想你们\n',
            '一定会称心如意的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '请二位好好休息吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_116F')

    def _loc_B6B(): pass

    label('loc_B6B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Return,
        ),
        'loc_108F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 1, 0x419)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1033',
    )

    EventBegin(0x00)
    Fade(1000)
    OP_69(0x0008, 0)
    CameraSetDistance(2800, 0)
    SetChrDirection(0x0008, 180, 0)
    SetChrPos(0x0101, -1830, 0, 9580, 354)
    SetChrPos(0x0102, -2920, 0, 9310, 354)
    SetChrPos(0x0136, -2370, 0, 8090, 354)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#1490041250V欢迎光临。\n',
            '这里是布朗西酒店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1490041251V请问客人是否已经预订了房间？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041252V#000F嗯～\n',
            '还没有呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041253V#010F请问现在还能订吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1490041254V几位来得真凑巧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1490041255V就在刚才，\n',
            '顶楼房间的预订被取消了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1490041256V如果可以的话，\n',
            '我这就带几位过去吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041257V#008F顶楼房间……\n',
            '嗯，听起来不错呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041258V#014F但是……\n',
            '顶楼房间的住宿费会贵很多吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1490041259V因为是取消预订后多出来的，\n',
            '所以只需付普通房间的费用就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1490041260V而且看起来，\n',
            '几位似乎是游击士吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1490041261V平时一直承蒙你们的照顾，\n',
            '这次就请让我为你们打个折吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041262V#001F嘿嘿，既然您这么说，\n',
            '那我们就恭敬不如从命啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041263V#010F那好，\n',
            '我们就要了这房间吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1490041264V我明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060041265V#041F呵呵，太好了。\n',
            '艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0EC1')
    def lambda_0EC1():
        OP_69(0x0101, 1200)

        ExitThread()

    DispatchAsync(0x0136, 0x0002, lambda_0EC1)

    ChrTurnDirection(0x0101, 0x0136, 400)
    ChrTurnDirection(0x0102, 0x0136, 400)
    WaitForThreadExit(0x0136, 0x0002)

    ChrTalk(
        0x0136,
        (
            '#0060041266V#040F那么我也\n',
            '差不多该回学院去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060041267V再不快点回去的话，\n',
            '就赶不上宿舍的门限时间了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041268V#000F#2P啊，对啊。\n',
            '你是说过只能陪我们到傍晚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010041269V#007F嗯……\n',
            '虽然舍不得，不过也没办法了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041270V#010F#1P不介意的话，我们送你回学院吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060041271V#041F呵呵，不用了。\n',
            '这条路我已经走惯了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0083, 1, 0x419))
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T2100._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_108C')

    def _loc_1033(): pass

    label('loc_1033')

    ChrTalk(
        0x0008,
        (
            '这个时期\n',
            '前来旅游的客人很多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '如果要在本酒店住宿，\n',
            '我建议你们\n',
            '尽早预定好房间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_108C(): pass

    label('loc_108C')

    Jump('loc_116F')

    def _loc_108F(): pass

    label('loc_108F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_116F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_111B',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '欢迎光临。\n',
            '这里是布朗西酒店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '本酒店的所有房间\n',
            '都能够望到大海，\n',
            '是个观景的好地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '请务必住在我们这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_116F')

    def _loc_111B(): pass

    label('loc_111B')

    ChrTalk(
        0x0008,
        (
            '本酒店的所有房间\n',
            '都能够望到大海，\n',
            '是个观景的好地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '请务必住在我们这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_116F(): pass

    label('loc_116F')

    TalkEnd(0x0008)

    Return()

# id: 0x0005 offset: 0x1173
@scena.Code('func_05_1173')
def func_05_1173():
    Return()

# id: 0x0006 offset: 0x1174
@scena.Code('func_06_1174')
def func_06_1174():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_125F',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '#0640041453V#221F哈哈哈～真是绝美的风景。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640041454V#220F我非常喜欢！\n',
            '这房间和作为下任国王的我非常相称。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640041455V如果拉旺塔尔赌吧在营业的话，\n',
            '我就没什么好说的了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640041456V#222F竟然在我来视察的时候改建，\n',
            '真是岂有此理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12DB')

    def _loc_125F(): pass

    label('loc_125F')

    ChrTalk(
        0x00FE,
        (
            '#0640041457V#220F如果拉旺塔尔赌吧在营业的话，\n',
            '我就没什么好说的了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640041458V#222F竟然在我来视察的时候改建，\n',
            '真是岂有此理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12DB(): pass

    label('loc_12DB')

    TalkEnd(0x000A)

    Return()

# id: 0x0007 offset: 0x12DF
@scena.Code('func_07_12DF')
def func_07_12DF():
    TalkBegin(0x000B)

    ChrTalk(
        0x000B,
        (
            '#0660041459V#720F给小姐你们添了这么多的麻烦。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660041460V我菲利普绝对不会忘记这份恩情。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000B)

    Return()

# id: 0x0008 offset: 0x1341
@scena.Code('func_08_1341')
def func_08_1341():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '没有让我睡觉的地方啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来只能去请求他们\n',
            '再搬一张床进来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x1391
@scena.Code('func_09_1391')
def func_09_1391():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '哈哈，\n',
            '这下我可有睡意了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x13B7
@scena.Code('func_0A_13B7')
def func_0A_13B7():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '哇，我好高～兴呢㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们可以住在\n',
            '这么棒的地方吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x13F9
@scena.Code('func_0B_13F9')
def func_0B_13F9():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '虽然屋子很漂亮，\n',
            '但反而让我平静不下来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x142D
@scena.Code('func_0C_142D')
def func_0C_142D():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '哎呀，很漂亮的屋子呢。\n',
            '我好喜欢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，\n',
            '从这边很难看到大海的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x1480
@scena.Code('func_0D_1480')
def func_0D_1480():
    TalkBegin(0x0011)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_14FD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_14D3',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '呼，接下来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '差不多该收拾行李，\n',
            '准备回柏斯了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14FA')

    def _loc_14D3(): pass

    label('loc_14D3')

    ChrTalk(
        0x00FE,
        (
            '差不多该收拾行李，\n',
            '准备回柏斯了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14FA(): pass

    label('loc_14FA')

    Jump('loc_1528')

    def _loc_14FD(): pass

    label('loc_14FD')

    ChrTalk(
        0x00FE,
        (
            '不愧是米拉诺小姐的熟人\n',
            '经营的酒店啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1528(): pass

    label('loc_1528')

    TalkEnd(0x0011)

    Return()

# id: 0x000E offset: 0x152C
@scena.Code('func_0E_152C')
def func_0E_152C():
    EventBegin(0x00)
    CameraMove(-2330, 0, 81840, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(261, 0)
    SetChrPos(0x0102, -1600, 0, 75980, 270)
    SetChrPos(0x0101, -1210, 0, 76950, 270)
    FadeIn(1000, 0)
    OP_0D()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010041314V#501F#1P哇～好大啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0101, -2420, 0, 77940, 5000, 0x00)

    @scena.Lambda('lambda_15EE')
    def lambda_15EE():
        ChrWalkTo(0x00FE, -3470, 0, 79710, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_15EE)

    ChrWalkTo(0x0101, -1050, 0, 80940, 5000, 0x00)
    ChrWalkTo(0x0101, 1490, 0, 82720, 5000, 0x00)
    SetChrDirection(0x0101, 90, 400)
    OP_62(0x0101, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    WaitForThreadExit(0x0102, 0x0001)
    SetChrDirection(0x0102, 45, 400)
    Sleep(1000)

    ClearMapFlags(0x00000001)

    @scena.Lambda('lambda_1665')
    def lambda_1665():
        CameraMove(-13470, 0, 74920, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1665)

    @scena.Lambda('lambda_167D')
    def lambda_167D():
        OP_6C(0, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_167D)

    @scena.Lambda('lambda_168D')
    def lambda_168D():
        ChrWalkTo(0x00FE, -6560, 0, 82610, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_168D)

    Sleep(500)

    SetChrDirection(0x0102, 315, 400)
    CreateThread(0x0102, 0x01, 0x00, 0x000F)
    WaitForThreadExit(0x0101, 0x0001)
    ChrWalkTo(0x0101, -12140, 0, 76520, 5000, 0x00)
    OP_62(0x0101, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010041315V#000F哦～这边是卧室啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0102, 0x0001)

    ChrTalk(
        0x0102,
        (
            '#0020041316V#010F而且还是独立套间。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020041317V只需付普通房间的费用，\n',
            '想起来还真是有点不好意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041318V#001F呵呵，难得人家这么提议，\n',
            '我们好好享受一下也无妨啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/T2100._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000F offset: 0x17CE
@scena.Code('func_0F_17CE')
def func_0F_17CE():
    Sleep(1000)

    ChrWalkTo(0x00FE, -6850, 0, 79910, 2000, 0x00)
    ChrWalkTo(0x00FE, -10730, 0, 75970, 2000, 0x00)

    Return()

# id: 0x0010 offset: 0x17FC
@scena.Code('func_10_17FC')
def func_10_17FC():
    EventBegin(0x00)
    CameraMove(-13860, 0, 75700, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x000A, -12490, 0, 76470, 225)
    SetChrPos(0x000B, -11080, 0, 76600, 225)
    SetChrPos(0x0101, -6200, 0, 83040, 225)
    SetChrPos(0x0102, -5190, 0, 82770, 225)
    OP_4A(0x000A, 255)
    OP_4A(0x000B, 255)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    FadeIn(1000, 0)
    OP_0D()

    NpcTalk(
        0x000A,
        '贵族打扮的男子',
        (
            '#0640041328V#220F#1P房间够大，家具也不错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640041329V嗯，我很满意。\n',
            '在卢安逗留期间就住这里好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000B,
        '黑衣老人',
        (
            '#0660041330V#722F#4P公爵大人，请您再稍等一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660041331V这个顶楼房间\n',
            '已经有其他客人住下了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660041332V不如就按照之前的计划，\n',
            '在市长大人的官邸下榻可好？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x000B, 400)

    NpcTalk(
        0x000A,
        '贵族打扮的男子',
        (
            '#0640041333V#224F#1P闭嘴，菲利普！\n',
            '难道住在那里能看见海吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640041334V#225F这间海边酒店风景又好，\n',
            '又能享受到如此清爽的海风。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0102, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    SetChrDirection(0x000A, 45, 400)

    @scena.Lambda('lambda_1A6B')
    def lambda_1A6B():
        ChrTurnDirection(0x00FE, 0x000A, 400)
        Yield()

        Jump('lambda_1A6B')

    DispatchAsync2(0x000B, 0x0001, lambda_1A6B)

    @scena.Lambda('lambda_1A7C')
    def lambda_1A7C():
        CameraMove(-7270, 0, 83010, 2000)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_1A7C)

    ChrWalkTo(0x000A, -7470, 0, 81250, 3000, 0x00)
    WaitForThreadExit(0x000B, 0x0002)

    NpcTalk(
        0x000A,
        '贵族打扮的男子',
        (
            '#0640041335V#221F#3P而且又可以在露台……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x000B, 0x0002)
    TerminateThread(0x000B, 0xFF)
    OP_63(0x0101)
    OP_63(0x0102)
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_62(0x000A, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrJumpToRelative(0x000A, 0, 0, 0, 800, 6000)
    ChrMoveTo(0x000A, -8160, 0, 80750, 5000, 0x00)

    NpcTalk(
        0x000A,
        '贵族打扮的男子',
        (
            '#0640041336V#226F你、你们是什么人！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640041337V强盗吗！？\n',
            '想行刺我的强盗吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041338V#007F#2P你在说些什么\n',
            '乱七八糟的话啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010041339V#009F倒是大叔你们是什么人？\n',
            '为什么擅自闯进我们的房间？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000A,
        '贵族打扮的男子',
        (
            '#0640041340V#224F不、不许叫我大叔！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640041341V#220F哼，算了……\n',
            '你们就是住这个房间的人吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640041342V这里已经成为\n',
            '我在卢安逗留期间的私人房间。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640041343V你们赶快给我出去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041344V#009F#2P啊？我可完全\n',
            '听不懂你在说什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010041345V凭什么要我们\n',
            '把房间让给你啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041346V#012F#2P请给我们一个解释。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000A,
        '贵族打扮的男子',
        (
            '#0640041347V#225F哼，所以我就说嘛，\n',
            '无知愚昧的平民最麻烦了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640041348V你们不知道本公爵是谁吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041349V#007F#2P嗯，完全不知道。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010041350V不过怎么看，\n',
            '都只是个头脑秀逗的大叔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000A,
        '贵族打扮的男子',
        (
            '#0640041351V#226F头、头脑秀逗……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041352V#010F#2P艾丝蒂尔……\n',
            '这样说似乎有点失礼吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020041353V说他很有个性之类的就好了嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041354V#001F#2P就是就是，还是你最会说话⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000A,
        '贵族打扮的男子',
        (
            '#0640041355V#222F呜呜呜呜……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640041356V#225F哼，算了。\n',
            '给我竖起耳朵听好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640041357V#224F……我的名字是\n',
            '杜南·冯·奥赛雷丝！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640041358V利贝尔女王艾莉茜雅Ⅱ世的侄子、\n',
            '王国现任的公爵！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041359V#004F#2P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041360V#014F#2P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0640041361V#225F哼哼哼……\n',
            '吃惊得说不出话了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640041362V总之，现在你们明白\n',
            '将房间让给本公爵的理由了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041363V#008F#2P噗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041364V#019F#2P哈哈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041365V#001F#2P#5S啊哈哈哈哈哈哈！#2S',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041366V#001F#2P大叔，太有趣了！\n',
            '笑得我肚子好痛哦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010041367V你为什么不说其他，\n',
            '偏偏说是女王陛下的侄子～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041368V#011F#2P呵呵，艾丝蒂尔。\n',
            '用不着笑成这个样子吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020041369V人家也许是为了调节气氛，\n',
            '才说些笑话让大家轻松一下哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0640041370V#226F这、这、这两个家伙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x000B, -7830, 0, 79660, 3000, 0x00)

    NpcTalk(
        0x000B,
        '黑衣老人',
        (
            '#0660041371V#722F……虽然十分抱歉，\n',
            '不过公爵大人所说的是事实。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000B, 400)
    ChrTurnDirection(0x0102, 0x000B, 400)

    ChrTalk(
        0x0101,
        (
            '#0010041372V#004F#2P哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000B,
        '黑衣老人',
        (
            '#0660041373V#720F对不起，还没自我介绍。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660041374V我是负责照顾\n',
            '公爵大人起居生活的管家。\n',
            '我叫菲利普……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660041375V自公爵大人出生以来\n',
            '我就一直随侍他的左右。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041376V#008F#2P啊，是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0660041377V#721F我以管家的名誉\n',
            '对此做出万分的保证。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660041378V站在你们面前的这位杜南公爵……\n',
            '的的确确就是艾莉茜雅女王的侄子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    SetChrDirection(0x0101, 135, 400)

    ChrTalk(
        0x0101,
        (
            '#0010041379V#002F#2P（虽、虽然很难让人信服……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010041380V（不过，先不说这个大叔，\n',
            '　那位管家看样子倒是不会假的。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041381V#013F#2P（说起来，\n',
            '　嘉恩先生之前也说过……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020041382V（有王族成员\n',
            '　要来卢安视察……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0640041383V#221F哇哈哈，知道错了吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640041384V把房间让给已被定为下任国王的我，\n',
            '对你们来说，简直是天大的荣誉啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640041385V要知道，\n',
            '这种机会可不是随便就能有的哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    SetChrDirection(0x0101, 225, 400)

    ChrTalk(
        0x0101,
        (
            '#0010041386V#005F#2P开、开什么玩笑！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010041387V就算真的是王族，\n',
            '像大叔你这样傲慢无礼的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrWalkTo(0x000B, -6160, 0, 82000, 4000, 0x00)
    ChrTurnDirection(0x000B, 0x0101, 400)

    ChrTalk(
        0x000B,
        (
            '#0660041388V#723F#3P慢着，小姐！\n',
            '请您等一下可以吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000B, 400)
    ChrTurnDirection(0x0102, 0x000B, 400)

    ChrTalk(
        0x0101,
        (
            '#0010041389V#004F#2P哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0660041390V#720F#3P还请借一步说话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_266A')
    def lambda_266A():
        CameraMove(-5790, 0, 84490, 1000)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_266A)

    @scena.Lambda('lambda_2682')
    def lambda_2682():
        ChrTurnDirection(0x00FE, 0x000B, 400)
        Yield()

        Jump('lambda_2682')

    DispatchAsync2(0x0101, 0x0001, lambda_2682)

    @scena.Lambda('lambda_2693')
    def lambda_2693():
        ChrTurnDirection(0x00FE, 0x000B, 400)
        Yield()

        Jump('lambda_2693')

    DispatchAsync2(0x0102, 0x0001, lambda_2693)

    SetChrFlags(0x0101, 0x0004)

    @scena.Lambda('lambda_26A9')
    def lambda_26A9():
        ChrWalkTo(0x00FE, -5790, 0, 84140, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_26A9)

    @scena.Lambda('lambda_26C4')
    def lambda_26C4():
        ChrWalkTo(0x00FE, -5100, 0, 84260, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_26C4)

    ChrWalkTo(0x000B, -5510, 0, 82990, 2000, 0x00)
    SetChrDirection(0x000B, 0, 400)
    ClearChrFlags(0x0101, 0x0004)

    ChrTalk(
        0x000B,
        (
            '#0660041391V#720F#3P虽然这样说很失礼，\n',
            '但是我有事想请求两位。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660041392V这样能把房间让给我们了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '老管家菲利普\n',
            '从怀里取出一大叠的米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#0010041393V#004F#1P管、管家先生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041394V#014F#2P怎么说也用不着这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0660041395V#722F#3P公爵大人是那种\n',
            '一言既出就绝不收回的人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660041396V这一切都是抚养公爵大人长大的\n',
            '我无德无能所造成的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660041397V求求你们，拜托了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '老管家菲利普低下头，\n',
            '做出一副准备下跪的姿势。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0102, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    OP_63(0x0101)
    OP_63(0x0102)

    ChrTalk(
        0x0101,
        (
            '#0010041398V#007F#1P哎，没办法了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010041399V其实我们\n',
            '也不想让管家太为难。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041400V#010F#2P房间就让给你们吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020041401V不过，这米拉我们不能收。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0660041402V#721F#3P但、但这样的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041403V#006F#1P没关系没关系⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010041404V对我们来说，\n',
            '这房间本来就太豪华了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010041405V#001F您要照看那位大叔一定很辛苦吧，\n',
            '不管怎样，要加油哦㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0660041406V#722F#3P小、小姐您……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660041407V真是太谢谢两位了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x000A, -6830, 0, 82020, 2000, 0x00)

    ChrTalk(
        0x000A,
        (
            '#0640041408V#224F喂喂，你们背着我\n',
            '嘀嘀咕咕地说些什么呀？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2AE9')
    def lambda_2AE9():
        ChrWalkTo(0x00FE, -5090, 0, 82330, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_2AE9)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    ChrTurnDirection(0x0102, 0x000A, 400)
    ChrTurnDirection(0x0101, 0x000A, 400)
    WaitForThreadExit(0x000B, 0x0001)
    ChrTurnDirection(0x000B, 0x000A, 400)

    ChrTalk(
        0x0101,
        (
            '#0010041409V#006F#1P没～什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041410V#010F#2P打扰你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020041411V房间这就让给公爵大人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0640041412V#220F哦哦，是吗！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640041413V#221F哇哈哈， \n',
            '一开始就老老实实这么说不就好了⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640041414V做人一定要谦虚才行，\n',
            '你们这些小的千万别忘记这点哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041415V#007F#1P真是受不了他……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041416V#019F#2P那么我们告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_69(0x0008, 0)
    CameraSetDistance(2600, 0)
    OP_6C(35000, 0)
    SetChrPos(0x0101, -1830, 0, 9580, 354)
    SetChrPos(0x0102, -2920, 0, 9310, 354)
    OP_4A(0x0008, 255)
    Sleep(500)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0xC),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeIn(1000, 0)
    OP_21()
    OP_1E()
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#1490041417V是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1490041418V早知如此，我刚才就该出面\n',
            '向公爵说明情况并断然拒绝他的要求……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1490041419V真是十分抱歉。\n',
            '事情变成现在这个样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041420V#000F没事没事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010041421V全都是那个\n',
            '任性的公爵不好嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041422V#010F对了……\n',
            '请问你们还有其他的房间吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020041423V普通房间就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1490041424V这、这个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1490041425V就在刚才，\n',
            '所有的房间都住满了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041428V#004F哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041426V#013F我们倒是没考虑到这一点……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1490041427V请二位放心。\n',
            '这次的事都是因为我处理不当引起的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1490041429V我会负起全责，\n',
            '为二位在其他地方安排住宿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, -2230, 0, 3110, 0)

    NpcTalk(
        0x0009,
        '男人的声音',
        (
            '#0270041430V#1P哟，是不是碰到麻烦了啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_2F66')
    def lambda_2F66():
        CameraMove(-2200, 0, 9820, 1200)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_2F66)

    @scena.Lambda('lambda_2F7E')
    def lambda_2F7E():
        ChrWalkTo(0x00FE, -2450, 0, 7490, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2F7E)

    SetChrDirection(0x0101, 225, 400)
    SetChrDirection(0x0102, 180, 400)
    WaitForThreadExit(0x0009, 0x0001)
    ChrTurnDirection(0x0009, 0x0008, 0)

    ChrTalk(
        0x0009,
        (
            '#0270041431V#141F#4P艾丝蒂尔、约修亚。\n',
            '空贼基地一别之后好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041432V#004F#2P啊，奈尔！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041433V#010F#1P晚上好。\n',
            '真没想到会在这里见到您。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270041434V#140F#4P这句话该我说才是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270041435V我也没想到\n',
            '你们俩也到卢安来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270041436V先不说这个，怎么了？\n',
            '是不是遇到了什么麻烦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041437V#007F#2P其实是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔说明了刚才发生的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0009,
        (
            '#0270041438V#147F#4P哈哈哈！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270041439V你们还是老样子，\n',
            '又碰到了一些有趣的事情！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041440V#009F#2P我说啊……\n',
            '这没什么好笑的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270041441V#141F#4P这事好办。\n',
            '你们就和我住一个房间吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041442V#004F#2P哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270041443V#141F#4P我房间正好有空着的床位。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270041444V哟，主管先生。\n',
            '我们一起住也没关系吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1490041445V当然了。\n',
            '您可是帮了大忙啊。 ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270041446V#141F#4P好，那就这么定了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270041447V地下一层最里面的房间。\n',
            '不必客气，尽管跟着来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0009, 180, 400)
    ChrWalkTo(0x0009, -1990, 0, 5550, 3000, 0x01)
    ChrWalkTo(0x0009, 2230, 0, 2070, 3000, 0x00)
    SetChrFlags(0x0009, 0x0080)
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010041448V#000F#2P啊，这样好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020041449V#010F#1P难得他这样提议，\n',
            '我们就照他说的办吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020041450V不过，作为收留我们的条件，\n',
            '多半会向我们挖点什么新闻吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041451V#007F#2P嗯……\n',
            '的确很有这种可能。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010041452V#006F不过，这点小事也无所谓啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)
    OP_4B(0x0008, 255)

    Return()

# id: 0x0011 offset: 0x341D
@scena.Code('func_11_341D')
def func_11_341D():
    EventBegin(0x00)
    CameraMove(-43860, 0, 53790, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(1236, 0)
    OP_6C(72000, 0)
    OP_6E(627, 0)
    ClearChrFlags(0x0009, 0x0080)
    SetChrFlags(0x0009, 0x0004)
    TerminateThread(0x0009, 0xFF)
    SetChrChipByIndex(0x0009, 5)
    SetChrSubChip(0x0009, 1)
    SetChrPos(0x0009, -47650, 200, 55350, 197)
    SetChrPos(0x0101, -43080, 0, 53380, 290)
    SetChrPos(0x0102, -42750, -200, 52630, 296)
    OP_6F(0x0007, 30)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0009,
        (
            '#0270041466V#141F哦，来了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270041467V这些空着的床\n',
            '你们就随便用吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_72(0x0007, 0x0800)
    PlaySE(7, 0x00, 0x64)
    OP_70(0x0007, 0)
    OP_66(0x0000)

    @scena.Lambda('lambda_3516')
    def lambda_3516():
        CameraMove(-46290, 0, 55390, 2000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3516)

    @scena.Lambda('lambda_352E')
    def lambda_352E():
        CameraSetDistance(1100, 2000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_352E)

    @scena.Lambda('lambda_353E')
    def lambda_353E():
        ChrWalkTo(0x00FE, -48390, 0, 53770, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_353E)

    Sleep(500)

    @scena.Lambda('lambda_355E')
    def lambda_355E():
        ChrWalkTo(0x00FE, -47390, 0, 53360, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_355E)

    WaitForThreadExit(0x0101, 0x0001)
    SetChrSubChip(0x0009, 0)

    @scena.Lambda('lambda_3583')
    def lambda_3583():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3583)

    WaitForThreadExit(0x0102, 0x0001)

    @scena.Lambda('lambda_3596')
    def lambda_3596():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3596)

    ChrTalk(
        0x0101,
        (
            '#0010041468V#006F虽然很感谢\n',
            '你能收留我们……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010041469V不过这样做好像也\n',
            '服务得太过周到了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270041470V#143F#1P哦？\n',
            '你在瞎猜什么呀？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270041471V先前都是多亏了你们，\n',
            '我才能写出那么爆炸性的报道。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270041472V只是表示一点感谢啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041473V#010F是空贼逮捕的特讯吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020041474V反响如何呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270041475V#141F#1P那还用说，简直卖疯了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270041476V而且，关于理查德上校和\n',
            '情报部活动的新闻尤为反响热烈。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270041477V可以说，上校的新闻\n',
            '简直比空贼事件本身还有看头。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041478V#004F是吗……\n',
            '那个人那么受欢迎吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270041479V#141F#1P据说因为这次事件的解决，\n',
            '他甚至得到了陛下颁发的勋章。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270041480V在王都一带的市民心中，\n',
            '他的人气可是直线上升啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270041481V下次我们也准备刊登\n',
            '理查德上校的独家专访。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041482V#014F那真是厉害啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270041483V#140F#1P无论从他的外表，还是他的举止，\n',
            '都能给人一种沉稳而又可靠的感觉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270041484V之前我也跟他聊了聊，\n',
            '觉得他确实是个很有气质的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270041485V#145F只是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041486V#505F只是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270041487V#142F#1P没什么……\n',
            '算了，无所谓啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270041488V#147F托这次报道的福，奖金也领到了，\n',
            '监护人的工作也总算熬到头了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270041489V多亏了理查德上校啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041490V#501F『监护人的工作熬到头了』，\n',
            '难道你是指朵洛希吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041491V#010F说起来……\n',
            '她没和你在一起吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270041492V#141F#1P本来就是带新人实习的性质，\n',
            '让她在社会上多吸收一下实践经验。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270041493V完成这次特讯之后，\n',
            '当然就是可喜可贺地解除合作关系啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041494V#000F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010041495V#506F不过……\n',
            '她一个人单独行动才更叫人担心呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270041496V#145F#1P别提了……\n',
            '我已经尽量不去多想她的事了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270041497V#141F总之，正因为这样，\n',
            '我现在可以花自己的奖金，\n',
            '逍遥快活地享受属于自己的假期。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041498V#007F说得倒是好听，\n',
            '反正肯定又是在追什么新闻吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010041499V#006F啊，难道说……\n',
            '是在为了那个公爵吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270041500V#140F#1P啊，杜南公爵吗。\n',
            '你们还真是倒霉啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270041501V据我所知，他在王族当中\n',
            '是以胡作非为举止出格而出名的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270041502V听说艾莉茜雅女王\n',
            '也经常为这个公爵大伤脑筋。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041503V#010F这话听起来倒是满有可信度的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020041504V不过，照他本人说，\n',
            '他会是利贝尔的下任国王……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041505V#509F哎～那是真的吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010041506V我可不想叫那种大叔\n',
            '『国王陛下』哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270041507V#140F#1P这个嘛，陛下年事已高了，\n',
            '他的确是继承王位的有力竞争者。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270041508V毕竟陛下的儿子\n',
            '很久以前就已经去世了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270041509V不过，周围的反对呼声也不少啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041510V#010F看来奈尔先生\n',
            '所知道的也不是很多啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020041511V也就是说……\n',
            '你在调查的是其它的事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270041512V#143F#1P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041513V#001F啊，看来被说中了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270041514V#145F#1P真是的……\n',
            '你这小子还是那么敏锐啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270041515V#141F我承认是有别的事。\n',
            '不过只能到此为止，不能再多说什么了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270041516V因为这是条相～当大的新闻哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041517V#501F你这么一说，\n',
            '反而惹得我们更想知道了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010041518V不过算了。\n',
            '反正我们又不是媒体的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041519V#010F那我们就期待着您的报道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270041520V#147F#1P没问题，包在我身上。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270041521V#141F对了，\n',
            '你们还没吃晚饭吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270041522V一块儿去吧，我请客。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041523V#001F哎？真的！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041524V#010F那我们就不客气了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_21()
    Sleep(500)

    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '当晚，由奈尔请客，\n',
            '艾丝蒂尔和约修亚他们\n',
            '在拉旺塔尔赌吧吃了一顿晚餐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '在品尝了各种各样\n',
            '亚瑟利亚湾的海鲜菜肴之后……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔他们将醉倒的\n',
            '奈尔抬回布朗西酒店，\n',
            '然后就各自就寝了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T2403._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0012 offset: 0x4182
@scena.Code('func_12_4182')
def func_12_4182():
    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4247',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_41A5',
    )

    ChrTurnDirection(0x0102, 0x0001, 400)

    Jump('loc_41AC')

    def _loc_41A5(): pass

    label('loc_41A5')

    ChrTurnDirection(0x0102, 0x0000, 400)

    def _loc_41AC(): pass

    label('loc_41AC')

    ChrTalk(
        0x0102,
        (
            '#0020041461V#010F赶快去奈尔先生的房间吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020041462V他这么热情招待我们，\n',
            '再让他等着就太没礼貌了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010041463V#000F他说的房间\n',
            '是在地下一层里面吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_42A9')

    def _loc_4247(): pass

    label('loc_4247')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_425D',
    )

    ChrTurnDirection(0x0102, 0x0001, 400)

    Jump('loc_4264')

    def _loc_425D(): pass

    label('loc_425D')

    ChrTurnDirection(0x0102, 0x0000, 400)

    def _loc_4264(): pass

    label('loc_4264')

    ChrTalk(
        0x0102,
        (
            '#0020041464V#010F赶快去奈尔先生的房间吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020041465V是在地下一层里面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_42A9(): pass

    label('loc_42A9')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
