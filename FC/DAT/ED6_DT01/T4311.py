import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4311_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4311   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '管家雷蒙德'),
    TXT(0x02, '特务兵'),
    TXT(0x03, '特务兵'),
    TXT(0x04, '特务兵'),
    TXT(0x05, '特务兵'),
    TXT(0x06, '特务兵'),
    TXT(0x07, '科洛丝'),
    TXT(0x08, '奥利维尔'),
    TXT(0x09, '雪拉'),
    TXT(0x0A, '尤莉亚中尉'),
    TXT(0x0B, '基库'),
    TXT(0x0C, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4311.x'
    header.mapIndex       = 1
    header.bgm            = 89
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x2AF3
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
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00101._CH', 'ED6_DT07/CH00101P._CP'),
        ('ED6_DT07/CH00110._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT07/CH00111._CH', 'ED6_DT07/CH00111P._CP'),
        ('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP'),
        ('ED6_DT07/CH00171._CH', 'ED6_DT07/CH00171P._CP'),
        ('ED6_DT07/CH01570._CH', 'ED6_DT07/CH01570P._CP'),
        ('ED6_DT07/CH01330._CH', 'ED6_DT07/CH01330P._CP'),
        ('ED6_DT06/CH20143._CH', 'ED6_DT06/CH20143P._CP'),
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT07/CH02090._CH', 'ED6_DT07/CH02090P._CP'),
        ('ED6_DT07/CH02320._CH', 'ED6_DT07/CH02320P._CP'),
        ('ED6_DT06/CH20042._CH', 'ED6_DT06/CH20042P._CP'),
        ('ED6_DT06/CH20113._CH', 'ED6_DT06/CH20113P._CP'),
    ]

# id: 0x10002 offset: 0x122
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -11850,
            z                   = 0,
            y                   = 20220,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
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
            dword_10            = 7,
            chipIndex           = 7,
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
            dword_10            = 7,
            chipIndex           = 7,
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
            dword_10            = 7,
            chipIndex           = 7,
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
            dword_10            = 7,
            chipIndex           = 7,
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
            dword_10            = 7,
            chipIndex           = 7,
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
            dword_10            = 8,
            chipIndex           = 8,
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
            dword_10            = 9,
            chipIndex           = 9,
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
            dword_10            = 10,
            chipIndex           = 10,
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
            dword_10            = 11,
            chipIndex           = 11,
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
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x282
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x282
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x282
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 25980,
            triggerZ            = 0,
            triggerY            = 50580,
            triggerRange        = 800,
            actorX              = 25690,
            actorZ              = 1500,
            actorY              = 51500,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 22140,
            triggerZ            = 0,
            triggerY            = 50600,
            triggerRange        = 800,
            actorX              = 21830,
            actorZ              = 890,
            actorY              = 51760,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 18200,
            triggerZ            = 0,
            triggerY            = 51350,
            triggerRange        = 800,
            actorX              = 18200,
            actorZ              = 1800,
            actorY              = 51350,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 14200,
            triggerZ            = 0,
            triggerY            = 51310,
            triggerRange        = 800,
            actorX              = 14200,
            actorZ              = 2000,
            actorY              = 51310,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 10220,
            triggerZ            = 0,
            triggerY            = 51150,
            triggerRange        = 800,
            actorX              = 10220,
            actorZ              = 1200,
            actorY              = 51150,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 24340,
            triggerZ            = 0,
            triggerY            = 45480,
            triggerRange        = 800,
            actorX              = 24340,
            actorZ              = 500,
            actorY              = 45480,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000C,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -13210,
            triggerZ            = 0,
            triggerY            = 18820,
            triggerRange        = 800,
            actorX              = -11850,
            actorZ              = 1500,
            actorY              = 20220,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x37E
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_395',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x000B)

    def _loc_395(): pass

    label('loc_395')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000066, 'loc_3A1'),
        (-1, 'loc_3B4'),
    )

    def _loc_3A1(): pass

    label('loc_3A1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 6, 0x656)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 3, 0x653)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3B1',
    )

    Event(0, 0x0005)

    def _loc_3B1(): pass

    label('loc_3B1')

    Jump('loc_3B4')

    def _loc_3B4(): pass

    label('loc_3B4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 6, 0x656)),
            Expr.Return,
        ),
        'loc_44F',
    )

    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x0009, 0x0001)
    ClearChrFlags(0x000A, 0x0001)
    ClearChrFlags(0x000B, 0x0001)
    ClearChrFlags(0x000C, 0x0001)
    SetChrFlags(0x0009, 0x0800)
    SetChrFlags(0x000A, 0x0800)
    SetChrFlags(0x000B, 0x0800)
    SetChrFlags(0x000C, 0x0800)
    SetChrPos(0x0009, -11150, 0, 15510, 315)
    SetChrPos(0x000A, -11000, 0, 17300, 0)
    SetChrPos(0x000B, -12500, 0, 17280, 270)
    SetChrPos(0x000C, -13000, 0, 16040, 225)
    SetChrChipByIndex(0x0009, 13)
    SetChrChipByIndex(0x000A, 13)
    SetChrChipByIndex(0x000B, 13)
    SetChrChipByIndex(0x000C, 13)

    def _loc_44F(): pass

    label('loc_44F')

    Return()

# id: 0x0001 offset: 0x450
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0x451
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_466',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_466(): pass

    label('loc_466')

    Return()

# id: 0x0003 offset: 0x467
@scena.Code('func_03_467')
def func_03_467():
    Call(0, 0x0004)

    Return()

# id: 0x0004 offset: 0x46C
@scena.Code('func_04_46C')
def func_04_46C():
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_50D',
    )

    OP_20(0x00000BB8)
    FadeOut(1000, 0, -1)
    Sleep(700)

    PlaySE(13, 0x00, 0x64)
    OP_0D()
    SetChrStatus(0x0000, 0xFE, 0)
    SetChrStatus(0x0001, 0xFE, 0)
    SetChrStatus(0x0002, 0xFE, 0)
    SetChrStatus(0x0003, 0xFE, 0)
    SetChrStatus(0x0004, 0xFE, 0)
    SetChrStatus(0x0005, 0xFE, 0)
    SetChrStatus(0x0006, 0xFE, 0)
    SetChrStatus(0x0007, 0xFE, 0)
    Sleep(3500)

    OP_1E()
    FadeIn(1000, 0)
    OP_56(0x00)
    TalkEnd(0x0008)

    Return()

    def _loc_50D(): pass

    label('loc_50D')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_527',
    )

    FadeIn(300, 0)
    TalkEnd(0x0008)

    Return()

    def _loc_527(): pass

    label('loc_527')

    FadeIn(300, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 7, 0x657)),
            Expr.Return,
        ),
        'loc_591',
    )

    ChrTalk(
        0x0008,
        (
            '#2330130684V对对，就是那个钥匙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330130685V如果有了那个，\n',
            '就可以进入『纹章之间』了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8B8')

    def _loc_591(): pass

    label('loc_591')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CF, 1, 0x679)),
            Expr.Return,
        ),
        'loc_5F3',
    )

    ChrTalk(
        0x0008,
        (
            '还有一把备用钥匙\n',
            '是保管在某个地方的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我记得……\n',
            '应该是藏匿在展示室里面的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8B8')

    def _loc_5F3(): pass

    label('loc_5F3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 5, 0x655)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CF, 1, 0x679)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_83E',
    )

    SetScenaFlags(ScenaFlag(0x00CF, 1, 0x679))
    OP_28(0x004C, 0x01, 0x0010)
    EventBegin(0x00)
    OP_69(0x0008, 1000)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '众人向管家说明了深处的门被锁上了的事情。',
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
            '#2330130671V是啊，\n',
            '那里是被锁上了的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330130672V开那扇门的钥匙\n',
            '是由情报部的中队长保管的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330130673V因为出现了恐怖分子，\n',
            '中队长好像出动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130663V#580F哎……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130664V#013F也就是说，\n',
            '是到尤莉亚中尉他们埋伏的地方去了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130665V#074F嗯，这可就麻烦了，\n',
            '没时间回去了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330130677V等等……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330130678V还有一把备用钥匙\n',
            '是保管在某个地方的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330130679V我想应该是\n',
            '藏匿在展示室里面……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130669V#005F展示室！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130670V#012F立刻去调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)

    Jump('loc_8B8')

    def _loc_83E(): pass

    label('loc_83E')

    ChrTalk(
        0x0008,
        (
            '#2330130686V谢谢你们救了我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330130687V#5P对了，如果感到疲劳，\n',
            '就回到这里休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330130688V#5P我给你们准备饮料。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8B8(): pass

    label('loc_8B8')

    TalkEnd(0x0008)

    Return()

# id: 0x0005 offset: 0x8BC
@scena.Code('func_05_8BC')
def func_05_8BC():
    EventBegin(0x00)
    CameraMove(-11300, 0, 20870, 0)
    OP_67(0, 6220, -10000, 0)
    CameraSetDistance(1820, 0)
    OP_6C(45000, 0)
    OP_6E(487, 0)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    CreateThread(0x0009, 0x00, 0x00, 0x0002)
    CreateThread(0x000A, 0x00, 0x00, 0x0002)
    CreateThread(0x000B, 0x00, 0x00, 0x0002)
    CreateThread(0x000C, 0x00, 0x00, 0x0002)
    SetChrPos(0x0008, -11780, 0, 20150, 225)
    SetChrChipByIndex(0x0101, 0)
    SetChrChipByIndex(0x0102, 2)
    SetChrChipByIndex(0x0108, 4)
    SetChrPos(0x0101, -16850, 0, 13660, 45)
    SetChrPos(0x0108, -18160, 0, 13760, 45)
    SetChrPos(0x0102, -16690, 0, 12820, 45)
    SetChrPos(0x0009, -10960, 0, 18200, 0)
    SetChrPos(0x000A, -12000, 0, 18190, 0)
    SetChrPos(0x000B, -14950, 0, 18980, 90)
    SetChrPos(0x000C, -13770, 0, 18980, 270)
    FadeIn(1000, 0)
    CameraMove(-14900, 0, 16920, 2000)
    OP_4A(0x0008, 255)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#2330130620V你、你们几个是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130621V#004F哇……\n',
            '聚集了不少人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000C, 0xFF)

    @scena.Lambda('lambda_0A5F')
    def lambda_0A5F():
        ChrTurnDirection(0x00FE, 0x0101, 250)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0A5F)

    @scena.Lambda('lambda_0A6D')
    def lambda_0A6D():
        ChrTurnDirection(0x00FE, 0x0101, 200)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0A6D)

    @scena.Lambda('lambda_0A7B')
    def lambda_0A7B():
        ChrTurnDirection(0x00FE, 0x0101, 150)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0A7B)

    ChrTurnDirection(0x000B, 0x0101, 200)

    ChrTalk(
        0x000B,
        (
            '#2660130622V#5P嗯～……\n',
            '什么，你们是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2630130623V#5P唔～……\n',
            '怎么我们不认识你们啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130624V#019F晚上好，\n',
            '我们是游击士协会的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2670130625V#5P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130626V#070F你们就在这里好好睡一觉吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0B5E')
    def lambda_0B5E():
        OP_92(0x00FE, 0x0008, 1000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0B5E)

    Sleep(50)

    @scena.Lambda('lambda_0B78')
    def lambda_0B78():
        OP_92(0x00FE, 0x000A, 1000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0B78)

    Sleep(50)

    @scena.Lambda('lambda_0B92')
    def lambda_0B92():
        OP_92(0x00FE, 0x000C, 1000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_0B92)

    CameraMove(-13120, 0, 18720, 500)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0108, 0xFF)
    TerminateThread(0x0102, 0xFF)
    Battle(0x000003AF, 0x00000000, 0x02, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_BD7'),
        (-1, 'loc_BDA'),
    )

    def _loc_BD7(): pass

    label('loc_BD7')

    OP_B4(0x00)

    Return()

    def _loc_BDA(): pass

    label('loc_BDA')

    EventBegin(0x00)
    CameraMove(-13760, 0, 18120, 0)
    SetChrFlags(0x0009, 0x0800)
    SetChrFlags(0x000A, 0x0800)
    SetChrFlags(0x000B, 0x0800)
    SetChrFlags(0x000C, 0x0800)
    ClearChrFlags(0x0009, 0x0001)
    ClearChrFlags(0x000A, 0x0001)
    ClearChrFlags(0x000B, 0x0001)
    ClearChrFlags(0x000C, 0x0001)
    SetChrPos(0x0009, -11150, 0, 15510, 315)
    SetChrPos(0x000A, -11000, 0, 17300, 0)
    SetChrPos(0x000B, -12500, 0, 17280, 270)
    SetChrPos(0x000C, -13000, 0, 16040, 225)
    SetChrChipByIndex(0x0009, 13)
    SetChrChipByIndex(0x000A, 13)
    SetChrChipByIndex(0x000B, 13)
    SetChrChipByIndex(0x000C, 13)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0108, 65535)
    SetChrPos(0x0101, -15250, 0, 17530, 90)
    SetChrPos(0x0108, -15870, 0, 15890, 90)
    SetChrPos(0x0102, -14310, 0, 16540, 90)
    SetChrFlags(0x0008, 0x0004)
    SetChrPos(0x0008, -12050, -600, 20370, 225)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010130627V#006F呵呵，一个不留。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130628V#071F几下就打晕了，\n',
            '真是没有挑战性。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130629V#010F这里和王城里面一样，\n',
            '也是个类似小酒吧的谈话室呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330130630V留、留我一条小命……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0D8C')
    def lambda_0D8C():
        CameraMove(-12770, 0, 19310, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0D8C)

    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0108, 65535)

    @scena.Lambda('lambda_0DB3')
    def lambda_0DB3():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0DB3)

    Sleep(200)

    @scena.Lambda('lambda_0DC6')
    def lambda_0DC6():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0DC6)

    Sleep(200)

    @scena.Lambda('lambda_0DD9')
    def lambda_0DD9():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_0DD9)

    WaitForThreadExit(0x0101, 0x0002)
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_0DFE')
    def lambda_0DFE():
        ChrMoveTo(0x00FE, -12050, 0, 20370, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0DFE)

    @scena.Lambda('lambda_0E19')
    def lambda_0E19():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0E19')

    DispatchAsync2(0x0108, 0x0001, lambda_0E19)

    @scena.Lambda('lambda_0E2A')
    def lambda_0E2A():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0E2A')

    DispatchAsync2(0x0101, 0x0001, lambda_0E2A)

    @scena.Lambda('lambda_0E3B')
    def lambda_0E3B():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0E3B')

    DispatchAsync2(0x0102, 0x0001, lambda_0E3B)

    WaitForThreadExit(0x0008, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#2330130631V我、我、我\n',
            '不是他们的同伙！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130632V#007F我们知道了，\n',
            '你是离宫的工作人员对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130633V#010F我们是接受女王陛下的委托\n',
            '前来解救被囚禁的人质的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330130634V咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330130635V真、真的吗？\n',
            '真的是来救我们的吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130636V#006F嗯，因此你可以放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0F5E')
    def lambda_0F5E():
        CameraMove(-15830, 0, 17600, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0F5E)

    ChrWalkTo(0x0008, -12930, 0, 21390, 3000, 0x00)
    ChrWalkTo(0x0008, -15830, 0, 20970, 3000, 0x00)
    ChrWalkTo(0x0008, -16300, 0, 18110, 3000, 0x00)
    TerminateThread(0x0101, 0x01)
    SetChrDirection(0x0101, 270, 0)

    ChrTalk(
        0x0008,
        (
            '#2330130637V#5P哈……太好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330130638V#5P我那个记者朋友被抓了之后，\n',
            '我以为我已经活不成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330130639V#5P他应该没事吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130640V#505F记者朋友……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130641V#004F啊，奈尔的朋友难道就是你？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330130642V#5P啊……',
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
            '众人告诉管家雷蒙德奈尔失踪事件的经过。',
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
            '#2330130643V#5P是啊，\n',
            '那时联络奈尔的确实是我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330130644V#5P他想对保护在这里的公主\n',
            '进行一次采访……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330130645V#5P看到他那么热心，我不忍心拒绝，\n',
            '于是我就把他悄悄带了进来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130646V#070F结果事情暴露而被捕了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330130647V#5P是啊，说来惭愧，\n',
            '那时我还没有觉察到真相。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330130648V#5P只是听说公主被恐怖分子列为目标，\n',
            '然后就被送到这里保护起来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330130649V#5P没想到公主原来是被\n',
            '情报部的那伙人给软禁了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330130650V#5P公主要来的事情让我们很高兴，\n',
            '所以根本就没有注意到实情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330130651V#5P我真是个不称职的管家……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130652V#506F算了算了，\n',
            '不要灰心丧气嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130653V#012F您知道那些人质被关在哪里吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330130654V#5P啊，他们集中在这个建筑最深处的\n',
            '『纹章之间』里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330130655V#5P那房间是用来签署条约的，\n',
            '是离宫里一个具有光辉历史的大厅。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x004C, 0x01, 0x0002)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 5, 0x655)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1444',
    )

    ChrTalk(
        0x0101,
        (
            '#0010130656V#006F最深处的『纹章之间』吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130657V#070F好，赶快去看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x004C, 0x01, 0x0004)

    Jump('loc_169A')

    def _loc_1444(): pass

    label('loc_1444')

    SetScenaFlags(ScenaFlag(0x00CF, 1, 0x679))
    OP_28(0x004C, 0x01, 0x0010)

    ChrTalk(
        0x0101,
        (
            '#0010130658V#004F最深处的大厅……\n',
            '不就是在刚才那边吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130659V#072F啊，不过里面有一扇上了锁的门。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330130660V#5P是啊，\n',
            '那里是被锁上了的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330130661V#5P开那扇门的钥匙\n',
            '是由情报部的中队长保管的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330130662V#5P因为出现了恐怖分子，\n',
            '中队长好像出动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130663V#580F哎……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130664V#013F也就是说，\n',
            '是到尤莉亚中尉他们埋伏的地方去了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130665V#074F嗯，这可就麻烦了，\n',
            '没时间回去了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330130666V#5P等等……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330130667V#5P还有一把备用钥匙\n',
            '是保管在某个地方的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330130668V#5P我想应该是\n',
            '藏匿在展示室里面……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130669V#005F展示室！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130670V#012F立刻去调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_169A(): pass

    label('loc_169A')

    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x0001, 0xFF)
    TerminateThread(0x0002, 0xFF)
    FadeOut(1000, 0, -1)
    OP_0D()
    CreateThread(0x0008, 0x00, 0x00, 0x0002)
    SetChrPos(0x0008, -11850, 0, 20220, 225)
    SetChrPos(0x0101, -16149, 0, 17150, 180)
    SetChrPos(0x0102, -16149, 0, 17150, 180)
    SetChrPos(0x0108, -16149, 0, 17150, 180)
    CameraMove(-16149, 0, 17150, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    SetScenaFlags(ScenaFlag(0x00CA, 6, 0x656))
    EventEnd(0x00)

    Return()

# id: 0x0006 offset: 0x1748
@scena.Code('func_06_1748')
def func_06_1748():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 7, 0x657)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00CF, 1, 0x679)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_185C',
    )

    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x00CA, 7, 0x657))
    OP_28(0x004C, 0x01, 0x0020)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '有个巨大的深红色花瓶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔他们调查了一下，\n',
            '看到在其底部粘有什么东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Sleep(400)

    SetMessageWindowPos(-1, -1, -1, -1)
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '备用钥匙',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    AddItem(0x036F, 1)

    ChrTalk(
        0x0101,
        (
            '#0010130689V#006F啊，就是它！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130690V#010F这样就可以打开里面那扇门了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)

    Jump('loc_18A4')

    def _loc_185C(): pass

    label('loc_185C')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '有个巨大的深红色花瓶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    def _loc_18A4(): pass

    label('loc_18A4')

    Return()

# id: 0x0007 offset: 0x18A5
@scena.Code('func_07_18A5')
def func_07_18A5():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 7, 0x657)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00CF, 1, 0x679)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_192E',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '漂亮的器皿作为装饰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔他们调查了一下，\n',
            '没有找到什么特别的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    Jump('loc_1971')

    def _loc_192E(): pass

    label('loc_192E')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '漂亮的器皿作为装饰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    def _loc_1971(): pass

    label('loc_1971')

    TalkEnd(0x00FF)

    Return()

# id: 0x0008 offset: 0x1975
@scena.Code('func_08_1975')
def func_08_1975():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 7, 0x657)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00CF, 1, 0x679)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1A00',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '放置着东方风格的瓶子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔他们调查了一下，\n',
            '没有找到什么特别的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    Jump('loc_1A45')

    def _loc_1A00(): pass

    label('loc_1A00')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '放置着东方风格的瓶子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    def _loc_1A45(): pass

    label('loc_1A45')

    TalkEnd(0x00FF)

    Return()

# id: 0x0009 offset: 0x1A49
@scena.Code('func_09_1A49')
def func_09_1A49():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 7, 0x657)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00CF, 1, 0x679)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1AD4',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '放置着帝国风格的瓶子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔他们调查了一下，\n',
            '没有找到什么特别的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    Jump('loc_1B19')

    def _loc_1AD4(): pass

    label('loc_1AD4')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '放置着帝国风格的瓶子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    def _loc_1B19(): pass

    label('loc_1B19')

    TalkEnd(0x00FF)

    Return()

# id: 0x000A offset: 0x1B1D
@scena.Code('func_0A_1B1D')
def func_0A_1B1D():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 7, 0x657)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00CF, 1, 0x679)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1BA2',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '美术目录并排着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔他们调查了一下，\n',
            '没有找到什么特别的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    Jump('loc_1BE1')

    def _loc_1BA2(): pass

    label('loc_1BA2')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '美术目录并排着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    def _loc_1BE1(): pass

    label('loc_1BE1')

    TalkEnd(0x00FF)

    Return()

# id: 0x000B offset: 0x1BE5
@scena.Code('func_0B_1BE5')
def func_0B_1BE5():
    SetMapFlags(0x02000000)
    EventBegin(0x00)
    CameraMove(17870, 0, -11650, 0)
    OP_67(0, 4740, -10000, 0)
    CameraSetDistance(3019, 0)
    OP_6C(315000, 0)
    OP_6E(261, 0)
    SetChrPos(0x000E, 11330, 0, -10500, 135)
    SetChrPos(0x0012, 12980, 0, -9840, 225)
    SetChrPos(0x0011, 12980, 0, -9840, 270)
    SetChrPos(0x0010, 12140, 0, -12950, 0)
    SetChrPos(0x000F, 10420, 0, -12050, 90)
    SetChrPos(0x0108, 11130, 0, -13550, 0)
    SetChrPos(0x0101, 13440, 0, -12780, 315)
    SetChrPos(0x0102, 14010, 0, -11910, 315)
    ChrTurnDirection(0x000E, 0x0011, 0)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0101, 0x0080)
    ClearChrFlags(0x0102, 0x0080)
    ClearChrFlags(0x0108, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    SetChrFlags(0x0011, 0x0020)
    SetChrChipByIndex(0x0011, 14)
    SetChrSubChip(0x0011, 0)
    SetChrFlags(0x0012, 0x0080)
    CameraMove(11600, 0, -10880, 3000)

    ChrTalk(
        0x0011,
        (
            '#0100130858V#175F我真的……\n',
            '感到非常抱歉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100130859V由于不成器的我，\n',
            '而让大家受了这么多苦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100130860V如果不能救出大家，办事不周的我\n',
            '必定用自己双手将身体撕裂来以谢此罪……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000E,
        '科洛蒂娅公主',
        (
            '#0060130861V#401F我不允许你这样说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060130862V能够这样和大家再次相会，\n',
            '我已经觉得非常心满意足了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060130863V你们能够来救我……\n',
            '我感激都还来不及呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0100130864V#171F殿下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0012, 400)

    ChrTalk(
        0x0101,
        (
            '#0010130865V#506F哎……不好意思，\n',
            '在你们感动的时候打断一下……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130866V#505F为什么基库也在这里呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0440130867V#310F啾？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0011, 0x0101, 400)

    ChrTalk(
        0x0011,
        (
            '#0100130868V#170F呵呵，基库在作为殿下的护卫的同时，\n',
            '也是亲卫队的传令员哦。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100130869V你们忘了在旅馆收到的那封信吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130870V#004F啊……是那天晚上！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130871V#010F果然是这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130872V这么说来，让尤莉亚中尉\n',
            '得知女王陛下委托的也是它了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0100130873V#176F嗯，没错。\n',
            '是女王陛下直接通过基库告知我的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100130874V#175F不过殿下所在的这个大房间\n',
            '没有基库可以进入的窗户。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100130875V不能及时取得联系真让我很担心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130876V#007F真是的……\n',
            '我完全没有想到呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130877V#509F喂，基库。\n',
            '悄悄的把信放下后就离开了，\n',
            '是不是有些不太礼貌呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0440130878V#310F啾～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000E, 0x0101, 400)

    NpcTalk(
        0x000E,
        '科洛蒂娅公主',
        (
            '#0060130879V#408F嘻嘻……\n',
            '它说『对不起』呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130880V#001F哎呀，没关系的啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130881V#006F对了，\n',
            '那些特务兵已经全部解决了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_21B5')
    def lambda_21B5():
        SetChrDirection(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_21B5)

    ChrTalk(
        0x0011,
        (
            '#0100130882V#178F在离宫这里值勤的特务部队\n',
            '基本上都被我们控制了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100130883V但是在格兰赛尔城内\n',
            '应该还有相当一部分的残党。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0030130884V#026F各地的王国军，\n',
            '至今还处于情报部的掌控之下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030130885V#022F最糟糕的是，他们很有可能会\n',
            '以镇压叛军的名义对这里展开进攻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0101, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010130886V#580F啊……\n',
            '我还没有想到这一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0102, 270, 400)

    ChrTalk(
        0x0102,
        (
            '#0020130887V#012F是呀……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130888V我想，至少也要让科洛丝\n',
            '先去安全的地方躲避一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000E,
        '科洛蒂娅公主',
        (
            '#0060130889V#404F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0040130890V#030F如果可以的话，\n',
            '去寻求帝国或共和国大使馆的保护如何？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040130891V#035F在大使馆里有治外法权保护……\n',
            '我想敌人是不会随便轻举妄动的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130892V#070F可以用刚才作战所缴获的\n',
            '特务飞艇作为逃跑的工具。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130893V虽然不能从根本上解决问题，\n',
            '但可以拖延一些时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0100130894V#176F说的是啊……\n',
            '也只有选择逃亡了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000E,
        '科洛蒂娅公主',
        (
            '#0060130895V#406F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060130896V#402F大家……听我说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0102, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0108, 0x00000000, 2300, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0010, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x000F, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0011, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    @scena.Lambda('lambda_257E')
    def lambda_257E():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_257E)

    @scena.Lambda('lambda_258C')
    def lambda_258C():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_258C)

    @scena.Lambda('lambda_259A')
    def lambda_259A():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_259A)

    @scena.Lambda('lambda_25A8')
    def lambda_25A8():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_25A8)

    @scena.Lambda('lambda_25B6')
    def lambda_25B6():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_25B6)

    @scena.Lambda('lambda_25C4')
    def lambda_25C4():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_25C4)

    NpcTalk(
        0x000E,
        '科洛蒂娅公主',
        (
            '#0060130897V#402F在这种状况下，\n',
            '我可以通过你们向游击士协会委托任务吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130898V#004F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130899V#010F人质营救任务已经完成了，\n',
            '所以应该可以接受其他的委托。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130900V当然，要视委托的内容而定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000E,
        '科洛蒂娅公主',
        (
            '#0060130901V#406F如果可以……\n',
            '请接受我无理的请求。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060130902V#403F可以帮助我解放王城并救出陛下吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0100130903V#173F殿、殿下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130904V#006F对啊……还有女王陛下呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130905V我们一定要把她也救出来啊！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130906V#074F说实话，\n',
            '我就知道有可能会变成这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130907V#072F不过，公主殿下……\n',
            '这个委托相当棘手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0030130908V#025F是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030130909V以我们现在的战斗力，就算全员齐聚，\n',
            '也不可能从正面攻入王城的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130910V#013F如果利用那艘特务飞艇的话，\n',
            '也不是没有可能……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130911V然而……\n',
            '充足的准备是行动的必要条件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000E,
        '科洛蒂娅公主',
        (
            '#0060130912V#406F……这些我已经考虑过了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060130913V#402F各位，你们看这个可以吗？',
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
            '科洛蒂娅公主取出了一幅古老的地图。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    AddItem(0x0357, 1)
    OP_AD('ED6_DT04/C_VIS019._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(1500)

    SetMessageWindowPos(150, 300, -1, -1)
    SetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010130914V#004F这张是……哪里的地图？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(300, 300, -1, -1)
    SetChrName('科洛蒂娅公主')

    Talk(
        (
            '#0060130915V#402F这张古地图是记载着王都地下水路\n',
            '内部结构的古代文献。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060130916V这上面标记有通往王城地下的隐藏水路。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeOut(0, 0, -1)
    OP_AE(0x000001F4)
    OP_20(0x000005DC)
    OP_21()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T4260._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000C offset: 0x2A65
@scena.Code('func_0C_2A65')
def func_0C_2A65():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '『先王的御座』\n',
            '　先王埃德佳Ⅲ世\n',
            '　下榻艾尔贝离宫时\n',
            '　爱用的椅子。',
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
