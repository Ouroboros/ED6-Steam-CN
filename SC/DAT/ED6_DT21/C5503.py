import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5503_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5503   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '克鲁茨'),
    TXT(0x02, '魔兽'),
    TXT(0x03, '魔兽'),
    TXT(0x04, '魔兽'),
    TXT(0x05, '魔兽'),
    TXT(0x06, '目标用照相机'),
    TXT(0x07, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5503.x'
    header.mapIndex       = 1
    header.bgm            = 31
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x3BE6
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
        ('ED6_DT07/CH01620._CH', 'ED6_DT07/CH01620P._CP'),
        ('ED6_DT29/CH12220._CH', 'ED6_DT29/CH12220P._CP'),
        ('ED6_DT07/CH00410._CH', 'ED6_DT07/CH00410P._CP'),
        ('ED6_DT07/CH00414._CH', 'ED6_DT07/CH00414P._CP'),
        ('ED6_DT07/CH00411._CH', 'ED6_DT07/CH00411P._CP'),
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00420._CH', 'ED6_DT07/CH00420P._CP'),
        ('ED6_DT29/CH12210._CH', 'ED6_DT29/CH12210P._CP'),
    ]

# id: 0x10002 offset: 0xEA
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
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            x                   = -13940,
            z                   = 0,
            y                   = 19260,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -27580,
            z                   = 0,
            y                   = 27680,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -36160,
            z                   = 0,
            y                   = 35380,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -36190,
            z                   = 0,
            y                   = 46820,
            direction           = 170,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
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
            npcIndex            = 0x00C0,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x1AA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x1AA
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 7400,
            y           = 2500,
            z           = 3900,
            range       = 9700,
            dword_10    = 0x00001A90,
            dword_14    = 0x00002008,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000006,
        ),
        ScenaEventData(
            x           = -7750,
            y           = 0,
            z           = 199430,
            range       = -4280,
            dword_10    = 0x000007D0,
            dword_14    = 0x00031ECA,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000007,
        ),
        ScenaEventData(
            x           = -16720,
            y           = -1000,
            z           = 19250,
            range       = -11910,
            dword_10    = 0x000007D0,
            dword_14    = 0x00003B92,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000A,
        ),
        ScenaEventData(
            x           = -24000,
            y           = -1000,
            z           = 30610,
            range       = -25500,
            dword_10    = 0x000007D0,
            dword_14    = 0x0000634C,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000C,
        ),
        ScenaEventData(
            x           = -38590,
            y           = -1000,
            z           = 33670,
            range       = -33820,
            dword_10    = 0x000007D0,
            dword_14    = 0x00007B0C,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000E,
        ),
        ScenaEventData(
            x           = -38410,
            y           = -1000,
            z           = 46310,
            range       = -33920,
            dword_10    = 0x000007D0,
            dword_14    = 0x0000A21C,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000010,
        ),
    )

# id: 0x10005 offset: 0x26A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 31770,
            triggerZ            = 200,
            triggerY            = 202040,
            triggerRange        = 800,
            actorX              = 31770,
            actorZ              = 1200,
            actorY              = 202040,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -5000,
            triggerZ            = 0,
            triggerY            = 6610,
            triggerRange        = 1600,
            actorX              = -5000,
            actorZ              = 1000,
            actorY              = 6730,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0013,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2B2
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0201, 1, 0x1009)),
            Expr.Return,
        ),
        'loc_2DE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0201, 3, 0x100B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2DE',
    )

    SetChrPos(0x0008, -770, 0, 7450, 170)
    ClearChrFlags(0x0008, 0x0080)
    CreateThread(0x0008, 0x00, 0x00, 0x0002)

    def _loc_2DE(): pass

    label('loc_2DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0201, 0, 0x1008)),
            (Expr.TestScenaFlags, ScenaFlag(0x0201, 1, 0x1009)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2EE',
    )

    Event(0, 0x0004)

    def _loc_2EE(): pass

    label('loc_2EE')

    Return()

# id: 0x0001 offset: 0x2EF
@scena.Code('Init')
def Init():
    OP_22(0x01C7, 0x00, 0x64)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x022C, 0, 0x1160)),
            Expr.Return,
        ),
        'loc_300',
    )

    SetChrFlags(0x0009, 0x0080)

    def _loc_300(): pass

    label('loc_300')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x022C, 1, 0x1161)),
            Expr.Return,
        ),
        'loc_30C',
    )

    SetChrFlags(0x000A, 0x0080)

    def _loc_30C(): pass

    label('loc_30C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x022C, 2, 0x1162)),
            Expr.Return,
        ),
        'loc_318',
    )

    SetChrFlags(0x000B, 0x0080)

    def _loc_318(): pass

    label('loc_318')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x022C, 3, 0x1163)),
            Expr.Return,
        ),
        'loc_324',
    )

    SetChrFlags(0x000C, 0x0080)

    def _loc_324(): pass

    label('loc_324')

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x11),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3A7',
    )

    EventBegin(0x00)

    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x2),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_378',
    )

    OP_A2(0x1160)
    SetChrFlags(0x0009, 0x0080)
    Call(0, 0x0008)
    SetChrPos(0x0101, -13420, 0, 18940, 0)
    SetChrPos(0x010A, -14920, 0, 18970, 0)
    OP_30(0x00)
    OP_69(0x0101, 0x00000000)

    Jump('loc_3A7')

    def _loc_378(): pass

    label('loc_378')

    Call(0, 0x0008)
    SetChrPos(0x0000, -13990, 50, 12500, 0)
    SetChrPos(0x0001, -13990, 50, 12500, 0)
    OP_30(0x00)
    OP_69(0x0101, 0x00000000)

    def _loc_3A7(): pass

    label('loc_3A7')

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x12),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3F8',
    )

    EventBegin(0x02)
    Call(0, 0x0008)
    SetChrPos(0x0000, -23500, 0, 28000, 270)
    SetChrPos(0x0001, -23500, 0, 28000, 270)
    OP_30(0x00)
    OP_69(0x0101, 0x00000000)

    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x2),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3F8',
    )

    OP_A2(0x1161)
    SetChrFlags(0x000A, 0x0080)

    def _loc_3F8(): pass

    label('loc_3F8')

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x13),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_449',
    )

    EventBegin(0x02)
    Call(0, 0x0008)
    SetChrPos(0x0000, -36130, 0, 28500, 0)
    SetChrPos(0x0001, -36130, 0, 28500, 0)
    OP_30(0x00)
    OP_69(0x0101, 0x00000000)

    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x2),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_449',
    )

    OP_A2(0x1162)
    SetChrFlags(0x000B, 0x0080)

    def _loc_449(): pass

    label('loc_449')

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x10),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4CC',
    )

    EventBegin(0x00)

    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x2),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_49D',
    )

    OP_A2(0x1163)
    SetChrFlags(0x000C, 0x0080)
    Call(0, 0x0008)
    SetChrPos(0x0000, -36010, 0, 40500, 0)
    SetChrPos(0x0001, -36010, 0, 40500, 0)
    OP_30(0x00)
    OP_69(0x0101, 0x00000000)

    Jump('loc_4CC')

    def _loc_49D(): pass

    label('loc_49D')

    Call(0, 0x0008)
    SetChrPos(0x0000, -36010, 0, 40500, 0)
    SetChrPos(0x0001, -36010, 0, 40500, 0)
    OP_30(0x00)
    OP_69(0x0101, 0x00000000)

    def _loc_4CC(): pass

    label('loc_4CC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0201, 1, 0x1009)),
            Expr.Return,
        ),
        'loc_4D6',
    )

    OP_10(0x00, 0x00)

    def _loc_4D6(): pass

    label('loc_4D6')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_541',
    )

    LoadEffect(0x00, 'map\\\\mp027_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, -5000, 1000, 6730, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    OP_72(0x0002, 0x0020)
    OP_6F(0x0002, 0)
    OP_70(0x0002, 0x00000000)

    Jump('loc_554')

    def _loc_541(): pass

    label('loc_541')

    OP_72(0x0002, 0x0020)
    OP_6F(0x0002, 0)
    OP_70(0x0002, 0x00000000)

    def _loc_554(): pass

    label('loc_554')

    Return()

# id: 0x0002 offset: 0x555
@scena.Code('ReInit')
def ReInit():
    ExecExpressionWithReg(
        0x0001,
        (
            Expr.Rand,
            (Expr.PushLong, 0x8),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Switch(
        (
            (Expr.PushReg, 0x1),
            Expr.Return,
        ),
        (0x00000000, 'loc_586'),
        (0x00000001, 'loc_592'),
        (0x00000002, 'loc_59E'),
        (0x00000003, 'loc_5AA'),
        (0x00000004, 'loc_5B6'),
        (0x00000005, 'loc_5C2'),
        (0x00000006, 'loc_5CE'),
        (-1, 'loc_5DA'),
    )

    def _loc_586(): pass

    label('loc_586')

    OP_99(0x00FE, 0x00, 0x07, 0x000005AA)

    Jump('loc_5E6')

    def _loc_592(): pass

    label('loc_592')

    OP_99(0x00FE, 0x00, 0x07, 0x0000060E)

    Jump('loc_5E6')

    def _loc_59E(): pass

    label('loc_59E')

    OP_99(0x00FE, 0x00, 0x07, 0x00000640)

    Jump('loc_5E6')

    def _loc_5AA(): pass

    label('loc_5AA')

    OP_99(0x00FE, 0x00, 0x07, 0x00000578)

    Jump('loc_5E6')

    def _loc_5B6(): pass

    label('loc_5B6')

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_5E6')

    def _loc_5C2(): pass

    label('loc_5C2')

    OP_99(0x00FE, 0x00, 0x07, 0x00000546)

    Jump('loc_5E6')

    def _loc_5CE(): pass

    label('loc_5CE')

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_5E6')

    def _loc_5DA(): pass

    label('loc_5DA')

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_5E6')

    def _loc_5E6(): pass

    label('loc_5E6')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5FB',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_5E6')

    def _loc_5FB(): pass

    label('loc_5FB')

    Return()

# id: 0x0003 offset: 0x5FC
@scena.Code('func_03_5FC')
def func_03_5FC():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_66D',
    )

    ChrTalk(
        0x0008,
        (
            '#0330190841V#840F你们两个怎么了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190842V想恢复体力的时候，\n',
            '就利用那里的回复装置吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    Jump('loc_694')

    def _loc_66D(): pass

    label('loc_66D')

    ChrTalk(
        0x0008,
        (
            '#0330190843V#840F那么，祝你好运。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_694(): pass

    label('loc_694')

    TalkEnd(0x0008)

    Return()

# id: 0x0004 offset: 0x698
@scena.Code('func_04_698')
def func_04_698():
    EventBegin(0x00)
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x010A, 0x0080)
    OP_6D(-13420, 0, 6250, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    @scena.Lambda('lambda_06E7')
    def lambda_06E7():
        OP_6D(150, 0, 5990, 5000)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_06E7)

    OP_C8(0x0200, 0x0046, 'C_PLAC02._CH', 0x00, 0x03E8)
    FadeIn(1000, 0)
    Sleep(300)

    SetChrPos(0x0008, 7310, 3250, 6000, 270)
    ClearChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0008, 0x0040)

    @scena.Lambda('lambda_073D')
    def lambda_073D():
        OP_8E(0x0008, -800, 0, 6000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_073D)

    ClearChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000D, 0x0008)
    SetChrPos(0x000D, 7310, 3250, 6000, 270)
    Sleep(500)

    @scena.Lambda('lambda_0778')
    def lambda_0778():
        OP_8E(0x000D, 140, 0, 6000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_0778)

    @scena.Lambda('lambda_0793')
    def lambda_0793():
        OP_69(0x000D, 0x00000000)
        Yield()

        Jump('lambda_0793')

    DispatchAsync2(0x000D, 0x0003, lambda_0793)

    Sleep(1000)

    SetChrPos(0x0101, 7230, 3000, 5320, 270)
    SetChrPos(0x010A, 7230, 3250, 6550, 270)
    ClearChrFlags(0x0101, 0x0080)
    ClearChrFlags(0x010A, 0x0080)

    @scena.Lambda('lambda_07D5')
    def lambda_07D5():
        OP_8E(0x010A, 1080, 0, 6550, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_07D5)

    Sleep(500)

    @scena.Lambda('lambda_07F5')
    def lambda_07F5():
        OP_8E(0x0101, 1100, 0, 5320, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_07F5)

    WaitForThreadExit(0x0008, 0x0001)
    TerminateThread(0x000D, 0x03)
    OP_8C(0x0008, 90, 1000)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010190809V#4P#1002F这里就是『巴斯塔尔水道』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120190810V#5P#812F看来是相当大的\n',
            '地下水道呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0330190811V#6P#843F虽然比不上王都的地下水道，\n',
            '但还是十分宽敞呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190812V#840F今天的演习，就是回收存放在\n',
            '水道最深处的机密文件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190813V#4P#1004F机、机密文件？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0330190814V#6P#840F哈哈，这纯粹是\n',
            '演习的预定内容。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190815V总之到达水路的最深处\n',
            '应该就能够找到目标文件。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190816V将它回收之后，演习就结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120190817V#5P#816F嗯～听起来\n',
            '倒是相当简单……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190818V#4P#1006F既然说是演习的话，\n',
            '一定准备了各式各样的东西吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0330190819V#6P#843F嗯，这就任凭各位想象了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190820V#842F顺带一提，四处游荡的魔兽\n',
            '确实是相当难对付。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190821V也许会使用到\n',
            '『连锁战技』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190822V#4P#1004F说到『连锁战技』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120190823V#5P#812F就是来到这里后特训的绝招，\n',
            '和同伴们一起进行的协力攻击吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0330190824V#6P#840F没错，是多位同伴\n',
            '可以同时攻击敌人的战技。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190825V机会难得，\n',
            '就在这次演习中试试看吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190837V为了慎重起见，\n',
            '也准备了导力器的恢复装置。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190836V如果受了伤就不要勉强，\n',
            '尽管去使用吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190826V#4P#1006F嗯、明白了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0330190827V#6P#840F<FIXME>……それと、戦闘に際して\n',
            '君達にこれを渡しておこう。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            '#2C#21I<FIXME>魔獣手帳#0Cを受け取った。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    AddItem(ItemTable['魔兽手册'], 1)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0101,
        (
            '#0010190828V#1011F<FIXME>あ、これって……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120190829V#6P#816F<FIXME>これは……\n',
            '『魔獣手帳』ってヤツですね？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0330190830V#841F<FIXME>ああ、戦った相手の情報を\n',
            '記録しておくための手帳さ。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190831V#840F敵の特性が判り次第、\n',
            'その手帳に書き記すといい。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190832V#1006F<FIXME>敵の情報か……\n',
            '戦いには重要なことよね。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120190833V#810F<FIXME>うん、まず敵を知ることは\n',
            '兵法の基本でもあるからね。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190834V#811F恩にきます、クルツ先輩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0330190835V#840F<FIXME>はは、礼には及ばないよ。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190836V加えて言わせてもらうと、\n',
            '傷を負った場合には\n',
            '無理せず撤退するように。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190837Vオーブメントの回復装置も\n',
            '念のために用意したからね。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190838V#1008F<FIXME>あはは、さすがはクルツさん。\n',
            '何もかも準備万端ってわけね。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120190839V#810F<FIXME>うん、それだけに私たちも\n',
            'ちゃんと期待に応えないと。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190840V#1310Fそれでは行ってきま～す！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0008, 0x01, 0x00, 0x0005)
    OP_10(0x00, 0x00)
    OP_A2(0x1009)
    OP_28(0x007E, 0x04, 0x02)
    OP_28(0x007E, 0x04, 0x08)
    OP_28(0x007E, 0x01, 0x0080)
    ClearChrFlags(0x0008, 0x0040)
    EventEnd(0x00)

    Return()

# id: 0x0005 offset: 0x10BD
@scena.Code('func_05_10BD')
def func_05_10BD():
    OP_8E(0x0008, -770, 0, 7450, 2000, 0x00)
    OP_8C(0x0008, 170, 500)
    CreateThread(0x0008, 0x00, 0x00, 0x0002)

    Return()

# id: 0x0006 offset: 0x10E0
@scena.Code('func_06_10E0')
def func_06_10E0():
    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0204, 2, 0x1022)),
            Expr.Return,
        ),
        'loc_10FE',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_110F')

    def _loc_10FE(): pass

    label('loc_10FE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0202, 2, 0x1012)),
            Expr.Return,
        ),
        'loc_110F',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_110F(): pass

    label('loc_110F')

    SetMapFlags(0x00000080)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_C5(0x00, 0x0000, 0x0000, 0x0280, 0x01E0, 0x0000, 0x0000, 0x0300, 0x0200, 0x0000, 0x0000, 0x0280, 0x01E0, 0x00FFFFFF, 0x00, 'C_VIS137._CH')
    OP_C6(0x00, 0x04, 0, 0, 0)
    OP_C6(0x00, 0x03, -1, 500, 0)
    OP_C7(0x00, 0x00, 0x03)
    OP_77(0x00, 0x00, 0x00, 0x00, 0x00000000)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1180(): pass

    label('loc_1180')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xFF),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_149D',
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Switch(
        (
            (Expr.PushReg, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_11AB'),
        (0x00000001, 'loc_11D7'),
        (0x00000002, 'loc_1214'),
        (-1, 'loc_1266'),
    )

    def _loc_11AB(): pass

    label('loc_11AB')

    Menu(
        0,
        30,
        80,
        0,
        (
            TXT(0x00, '【训练场宿舍】\n'),
            TXT(0x01, '【巴斯塔尔水道】\n'),
        ),
    )

    Jump('loc_1266')

    def _loc_11D7(): pass

    label('loc_11D7')

    Menu(
        0,
        30,
        80,
        0,
        (
            TXT(0x00, '【训练场宿舍】\n'),
            TXT(0x01, '【巴斯塔尔水道】\n'),
            TXT(0x02, '【圣科洛瓦森林】\n'),
        ),
    )

    Jump('loc_1266')

    def _loc_1214(): pass

    label('loc_1214')

    Menu(
        0,
        30,
        80,
        0,
        (
            TXT(0x00, '【训练场宿舍】\n'),
            TXT(0x01, '【巴斯塔尔水道】\n'),
            TXT(0x02, '【圣科洛瓦森林】\n'),
            TXT(0x03, '【格林姆瑟尔小要塞】\n'),
        ),
    )

    Jump('loc_1266')

    def _loc_1266(): pass

    label('loc_1266')

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
    OP_56(0x00)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1290'),
        (0x00000001, 'loc_1310'),
        (0x00000002, 'loc_1392'),
        (0x00000003, 'loc_1414'),
        (-1, 'loc_149A'),
    )

    def _loc_1290(): pass

    label('loc_1290')

    SetChrName('')
    SetMessageWindowPos(-1, 120, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '要移动至【训练场宿舍】吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        1,
        10,
        -1,
        0,
        (
            TXT(0x00, '【是】\n'),
            TXT(0x01, '【否】\n'),
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

    OP_5F(0x0001)
    OP_56(0x00)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_12FD'),
        (0x00000001, 'loc_130A'),
        (-1, 'loc_130D'),
    )

    def _loc_12FD(): pass

    label('loc_12FD')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_130D')

    def _loc_130A(): pass

    label('loc_130A')

    Jump('loc_130D')

    def _loc_130D(): pass

    label('loc_130D')

    Jump('loc_149A')

    def _loc_1310(): pass

    label('loc_1310')

    SetChrName('')
    SetMessageWindowPos(-1, 120, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '要移动至【巴斯塔尔水道】吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        1,
        10,
        -1,
        0,
        (
            TXT(0x00, '【是】\n'),
            TXT(0x01, '【否】\n'),
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

    OP_5F(0x0001)
    OP_56(0x00)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_137F'),
        (0x00000001, 'loc_138C'),
        (-1, 'loc_138F'),
    )

    def _loc_137F(): pass

    label('loc_137F')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_138F')

    def _loc_138C(): pass

    label('loc_138C')

    Jump('loc_138F')

    def _loc_138F(): pass

    label('loc_138F')

    Jump('loc_149A')

    def _loc_1392(): pass

    label('loc_1392')

    SetChrName('')
    SetMessageWindowPos(-1, 120, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '要移动至【圣科洛瓦森林】吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        1,
        10,
        -1,
        0,
        (
            TXT(0x00, '【是】\n'),
            TXT(0x01, '【否】\n'),
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

    OP_5F(0x0001)
    OP_56(0x00)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1401'),
        (0x00000001, 'loc_140E'),
        (-1, 'loc_1411'),
    )

    def _loc_1401(): pass

    label('loc_1401')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1411')

    def _loc_140E(): pass

    label('loc_140E')

    Jump('loc_1411')

    def _loc_1411(): pass

    label('loc_1411')

    Jump('loc_149A')

    def _loc_1414(): pass

    label('loc_1414')

    SetChrName('')
    SetMessageWindowPos(-1, 120, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '要移动至【格林姆瑟尔小要塞】吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        1,
        10,
        -1,
        0,
        (
            TXT(0x00, '【是】\n'),
            TXT(0x01, '【否】\n'),
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

    OP_5F(0x0001)
    OP_56(0x00)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1487'),
        (0x00000001, 'loc_1494'),
        (-1, 'loc_1497'),
    )

    def _loc_1487(): pass

    label('loc_1487')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1497')

    def _loc_1494(): pass

    label('loc_1494')

    Jump('loc_1497')

    def _loc_1497(): pass

    label('loc_1497')

    Jump('loc_149A')

    def _loc_149A(): pass

    label('loc_149A')

    Jump('loc_1180')

    def _loc_149D(): pass

    label('loc_149D')

    Switch(
        (
            (Expr.PushReg, 0x2),
            Expr.Return,
        ),
        (0x00000000, 'loc_14B6'),
        (0x00000001, 'loc_14EA'),
        (0x00000002, 'loc_151E'),
        (0x00000003, 'loc_1552'),
        (-1, 'loc_1586'),
    )

    def _loc_14B6(): pass

    label('loc_14B6')

    OP_C6(0x00, 0x00, -640000, 0, 2000)
    OP_C6(0x00, 0x01, 2000, 2000, 2000)
    OP_C6(0x00, 0x03, 16777215, 2000, 0)
    OP_C7(0x00, 0x00, 0x03)

    Jump('loc_1586')

    def _loc_14EA(): pass

    label('loc_14EA')

    OP_C6(0x00, 0x00, -358000, -37000, 2000)
    OP_C6(0x00, 0x01, 2000, 2000, 2000)
    OP_C6(0x00, 0x03, 16777215, 2000, 0)
    OP_C7(0x00, 0x00, 0x03)

    Jump('loc_1586')

    def _loc_151E(): pass

    label('loc_151E')

    OP_C6(0x00, 0x00, -362000, -266000, 2000)
    OP_C6(0x00, 0x01, 2000, 2000, 2000)
    OP_C6(0x00, 0x03, 16777215, 2000, 0)
    OP_C7(0x00, 0x00, 0x03)

    Jump('loc_1586')

    def _loc_1552(): pass

    label('loc_1552')

    OP_C6(0x00, 0x00, -64000, -340000, 2000)
    OP_C6(0x00, 0x01, 2000, 2000, 2000)
    OP_C6(0x00, 0x03, 16777215, 2000, 0)
    OP_C7(0x00, 0x00, 0x03)

    Jump('loc_1586')

    def _loc_1586(): pass

    label('loc_1586')

    OP_C6(0x00, 0x06, 0, 0, 0)
    OP_77(0xFF, 0xFF, 0xFF, 0x00, 0x00000000)

    Switch(
        (
            (Expr.PushReg, 0x2),
            Expr.Return,
        ),
        (0x00000000, 'loc_15B7'),
        (0x00000001, 'loc_15C3'),
        (0x00000002, 'loc_15CF'),
        (0x00000003, 'loc_15DB'),
        (-1, 'loc_15E7'),
    )

    def _loc_15B7(): pass

    label('loc_15B7')

    NewScene('ED6_DT21/T5100._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_15E7')

    def _loc_15C3(): pass

    label('loc_15C3')

    NewScene('ED6_DT21/C5503._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_15E7')

    def _loc_15CF(): pass

    label('loc_15CF')

    NewScene('ED6_DT21/C5507._SN', 101, 0, 0)
    IdleLoop()

    Jump('loc_15E7')

    def _loc_15DB(): pass

    label('loc_15DB')

    NewScene('ED6_DT21/C5508._SN', 101, 0, 0)
    IdleLoop()

    Jump('loc_15E7')

    def _loc_15E7(): pass

    label('loc_15E7')

    Return()

# id: 0x0007 offset: 0x15E8
@scena.Code('func_07_15E8')
def func_07_15E8():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0201, 3, 0x100B)),
            Expr.Return,
        ),
        'loc_15F0',
    )

    Return()

    def _loc_15F0(): pass

    label('loc_15F0')

    EventBegin(0x00)
    SetChrPos(0x0008, 10060, 0, 201910, 270)
    TerminateThread(0x0008, 0x00)
    SetChrSubChip(0x0008, 0)

    NpcTalk(
        0x0008,
        '男人的声音',
        (
            '#0330190920V呵，总算来了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x010A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0008, 1000)
    ChrTurnDirection(0x010A, 0x0008, 1000)

    @scena.Lambda('lambda_1680')
    def lambda_1680():
        OP_6D(8550, 0, 201870, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1680)

    @scena.Lambda('lambda_1698')
    def lambda_1698():
        OP_67(0, 6500, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1698)

    @scena.Lambda('lambda_16B0')
    def lambda_16B0():
        OP_6C(89000, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_16B0)

    @scena.Lambda('lambda_16C0')
    def lambda_16C0():
        OP_6B(3150, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_16C0)

    Sleep(2000)

    SetChrPos(0x010A, -3580, 0, 200950, 90)
    SetChrPos(0x0101, -3660, 0, 202230, 90)

    @scena.Lambda('lambda_16F7')
    def lambda_16F7():
        OP_8E(0x0101, 6390, 0, 202630, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_16F7)

    Sleep(200)

    @scena.Lambda('lambda_1717')
    def lambda_1717():
        OP_8E(0x010A, 6110, 0, 201200, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_1717)

    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x010A, 0x0001)

    ChrTalk(
        0x010A,
        (
            '#0120190921V#814F#4P克、克鲁茨前辈！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190922V#1004F#6P咦，等一下……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190923V你应该在入口处才对，\n',
            '怎么会先到达这里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0330190924V#841F其实是有其他捷径的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190925V在你们解除装置期间，\n',
            '我就直接来了这里哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190926V#1007F#6P受打击了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190927V#1019F好不容易\n',
            '辛辛苦苦地解除了装置……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120190928V#812F#4P先、先不说这个了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190929V这里确实是\n',
            '地下水路的最深处吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0330190930V#840F嗯嗯，没错？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120190931V#819F#4P那么……\n',
            '要回收的机密文件呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0330190932V#841F呵呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0x00D5, 0x00, 0x64)
    SetChrChipByIndex(0x0008, 2)
    OP_0D()
    Sleep(500)

    OP_62(0x010A, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_1991')
    def lambda_1991():
        OP_91(0x0101, -1000, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1991)

    Sleep(100)

    @scena.Lambda('lambda_19B1')
    def lambda_19B1():
        OP_91(0x010A, -1000, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_19B1)

    WaitForThreadExit(0x010A, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    Sleep(200)

    ChrTalk(
        0x0101,
        (
            '#0010190933V#1020F#6P咦！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120190934V#1316F#4P果、果然……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0330190935V#845F你们就把我当成是来抢夺\n',
            '机密文件的某国武装工作人员吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190936V当然，对于目的相同的人\n',
            '都要以实力加以排除。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190937V#1005F#6P你、你说什么～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120190938V#815F#4P机密文件不过是借口……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190939V真正的演习课题，是在探索中\n',
            '出乎预料的交战吧！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0330190940V#841F呵呵，就是这么回事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190941V#846F那么……\n',
            '我就先下手了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0008, 0x0001)
    Battle(0x00000393, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_1BAF'),
        (-1, 'loc_1BB4'),
    )

    def _loc_1BAF(): pass

    label('loc_1BAF')

    OP_B4(0x00)

    Jump('loc_1BB4')

    def _loc_1BB4(): pass

    label('loc_1BB4')

    EventBegin(0x00)
    FadeOut(0, 0, -1)
    ClearMapFlags(0x00000001)
    TerminateThread(0x0008, 0x00)
    OP_6C(45000, 0)
    SetChrPos(0x0008, 10060, 0, 201910, 270)
    SetChrFlags(0x0008, 0x0800)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 3)
    SetChrSubChip(0x0008, 3)
    SetChrPos(0x0101, 6350, 0, 202970, 92)
    SetChrChipByIndex(0x0101, 5)
    SetChrPos(0x010A, 6350, 0, 200970, 92)
    SetChrChipByIndex(0x010A, 6)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0330190942V#843F哎呀哎呀……\n',
            '本来不打算手下留情的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190943V看来是我输了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190944V#1003F呼呼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190945V我们……赢了……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120190946V#813F#6P嗯，嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190947V不愧是『方术使』……\n',
            '两个人联手好不容易才能赢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    OP_22(0x00D5, 0x00, 0x64)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0330190948V#841F好了……\n',
            '使得工作人员丧失战斗力后，\n',
            '你们回收了机密文件。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190949V此次的演习到此结束。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0101, 65535)
    Sleep(100)

    SetChrChipByIndex(0x010A, 65535)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010190950V#1011F那、那今天的训练……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120190951V#1310F#6P就到此结束了吗……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0330190952V#840F哈哈，怎么可能。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190953V回到宿舍吃完午餐后，\n',
            '再去南边的『圣科洛瓦森林』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190954V要修正演习中值得反省的地方，\n',
            '必须继续接受充分的训练啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    OP_62(0x010A, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010190955V#1007F哎～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120190956V#1316F#6P克鲁茨前辈……\n',
            '真是一点也不留情面啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000009C4)
    FadeOut(2000, 0, -1)
    OP_0D()
    Sleep(1000)

    NewScene('ED6_DT21/T5101._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0008 offset: 0x1F7E
@scena.Code('func_08_1F7E')
def func_08_1F7E():
    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x0001, 0xFF)

    ExecExpressionWithValue(
        0x0000,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0001,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrSubChip(0x0000, 0)
    SetChrSubChip(0x0001, 0)

    Return()

# id: 0x0009 offset: 0x1FA7
@scena.Code('func_09_1FA7')
def func_09_1FA7():
    OP_22(0x0074, 0x00, 0x64)
    Sleep(300)

    OP_22(0x0074, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上着锁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x000A offset: 0x1FED
@scena.Code('func_0A_1FED')
def func_0A_1FED():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x022C, 0, 0x1160)),
            Expr.Return,
        ),
        'loc_1FF5',
    )

    Return()

    def _loc_1FF5(): pass

    label('loc_1FF5')

    EventBegin(0x00)
    ChrTurnDirection(0x0000, 0x0009, 0)
    ChrTurnDirection(0x0001, 0x0009, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_2013',
    )

    Call(0, 0x000B)

    Jump('loc_2416')

    def _loc_2013(): pass

    label('loc_2013')

    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010190844V#1002F啊，马上就出现了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120190845V#810F嗯，用来小试身手\n',
            '再适合不过了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190846V好久没实战了，想一边确认\n',
            '战斗方法的同时并进行战斗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190847V怎么办？艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190848V从基础开始全部复习一遍？\n',
            '还是只确认连锁战技？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
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
        1,
        10,
        -1,
        0,
        (
            TXT(0x00, '【从基础开始复习】\n'),
            TXT(0x01, '【只确认连锁战技】\n'),
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

    OP_5F(0x0001)
    OP_56(0x00)
    FadeIn(300, 0)
    ChrTurnDirection(0x0101, 0x010A, 400)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_21A1'),
        (0x00000001, 'loc_2281'),
        (-1, 'loc_2357'),
    )

    def _loc_21A1(): pass

    label('loc_21A1')

    ChrTalk(
        0x0101,
        (
            '#0010190849V#1015F嗯～为了保险起见，\n',
            '我还是想从基础开始。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190850V正如亚妮拉丝所说的一样，\n',
            '好久没跟魔兽战斗了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120190851V#816F嗯！明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190852V那么走吧，艾丝蒂尔！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190853V#1018F好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2357')

    def _loc_2281(): pass

    label('loc_2281')

    OP_A2(0x1064)

    ChrTalk(
        0x0101,
        (
            '#0010190854V#1015F我只想确认\n',
            '连锁战技。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190855V毕竟想早点试试\n',
            '练习过的连锁战技……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120190851V#816F嗯！明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190857V那么，就去把这里的魔兽\n',
            '统统都踹飞吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190853V#1018F好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2357')

    def _loc_2357(): pass

    label('loc_2357')

    OP_59()
    OP_A2(0x0000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x020C, 4, 0x1064)),
            Expr.Return,
        ),
        'loc_2412',
    )

    OP_A2(0x1160)
    OP_A2(0x1161)
    OP_A2(0x1162)
    FadeOut(500, 0, -1)

    @scena.Lambda('lambda_237B')
    def lambda_237B():
        OP_69(0x0009, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_237B)

    @scena.Lambda('lambda_2389')
    def lambda_2389():
        OP_8E(0x0000, -13900, 0, 18980, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_2389)

    @scena.Lambda('lambda_23A4')
    def lambda_23A4():
        OP_8E(0x0001, -13900, 0, 18980, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0001, 0x0000, lambda_23A4)

    OP_0D()
    TerminateThread(0x0000, 0x01)
    TerminateThread(0x0000, 0x00)
    TerminateThread(0x0001, 0x00)
    SetChrPos(0x0000, -36020, 0, 38300, 0)
    SetChrPos(0x0001, -36020, 0, 38300, 0)
    OP_69(0x0000, 0x00000000)
    OP_4A(0x0000, 0)
    OP_4A(0x0001, 0)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    Sleep(4000)

    Call(0, 0x0012)

    Jump('loc_2416')

    def _loc_2412(): pass

    label('loc_2412')

    Call(0, 0x000B)

    def _loc_2416(): pass

    label('loc_2416')

    EventEnd(0x00)

    Return()

# id: 0x000B offset: 0x2419
@scena.Code('func_0B_2419')
def func_0B_2419():
    OP_59()

    @scena.Lambda('lambda_2420')
    def lambda_2420():
        OP_69(0x0009, 0x000001F4)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_2420)

    @scena.Lambda('lambda_242E')
    def lambda_242E():
        OP_8E(0x0000, -13900, 0, 18980, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_242E)

    @scena.Lambda('lambda_2449')
    def lambda_2449():
        OP_8E(0x0001, -13900, 0, 18980, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0001, 0x0000, lambda_2449)

    Sleep(300)

    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x0001, 0xFF)
    Battle(0x00000011, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_2484'),
        (-1, 'loc_26D1'),
    )

    def _loc_2484(): pass

    label('loc_2484')

    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x0001, 0xFF)
    EventBegin(0x00)
    SetChrPos(0x0101, -13420, 0, 18940, 0)
    SetChrPos(0x010A, -14920, 0, 18970, 0)
    OP_6D(-14170, 400, 18970, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010190859V#1018F<FIXME>よし、問題なく倒せたわ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x010A, 0x0101, 400)

    ChrTalk(
        0x010A,
        (
            '#0120190860V#810F<FIXME>うん、それじゃエステルちゃん。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190861V今戦った魔獣のこと、\n',
            'さっそく魔獣手帳に記録しよっか。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x010A, 400)

    ChrTalk(
        0x0101,
        (
            '#0010190862V#1006F<FIXME>了解、任せておいて。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190863V#1029Fさらさらさら……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190864V#1006Fうん、これでバッチリね。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '<FIXME>※戦闘で戦った相手の情報は、\n',
            '  自動的に魔獣手帳に記録されます。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '<FIXME>※なお、戦闘に勝利するか\n',
            '  逃走するかによって\n',
            '  記録される内容は変化します。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    Jump('loc_26D1')

    def _loc_26D1(): pass

    label('loc_26D1')

    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x0001, 0xFF)

    Return()

# id: 0x000C offset: 0x26DA
@scena.Code('func_0C_26DA')
def func_0C_26DA():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x022C, 1, 0x1161)),
            Expr.Return,
        ),
        'loc_26E2',
    )

    Return()

    def _loc_26E2(): pass

    label('loc_26E2')

    EventBegin(0x00)
    ChrTurnDirection(0x0000, 0x000A, 0)
    ChrTurnDirection(0x0001, 0x000A, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_28E1',
    )

    If(
        (
            (Expr.Eval, "OP_B9(0x00, 0x000A)"),
            Expr.Ez,
            (Expr.Eval, "OP_B9(0x09, 0x000A)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_B9(0x00, 0x0014)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_B9(0x09, 0x0014)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_B9(0x00, 0x001E)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_B9(0x09, 0x001E)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_B9(0x00, 0x0032)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_B9(0x09, 0x0032)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_B9(0x00, 0x0046)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_B9(0x09, 0x0046)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_B9(0x00, 0x0041)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_B9(0x09, 0x0041)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_284D',
    )

    ChrTalk(
        0x010A,
        (
            '#0120190865V#814F艾丝蒂尔。\n',
            '准备好攻击魔法了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190866V#810F前进之前要先\n',
            '设定好结晶回路哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※结晶回路的设置在[Orbment]画面进行。\n',
            '  要打开[Orbment]画面，\n',
            '  请在整备画面中点选[Orbment]栏。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_59()
    OP_A2(0x0001)
    OP_90(0x0000, 1500, 0, 0, 3000, 0x00)
    EventEnd(0x00)

    Return()

    def _loc_284D(): pass

    label('loc_284D')

    ChrTalk(
        0x010A,
        (
            '#0120190867V#810F对付武器难以伤害的敌人，\n',
            '魔法就很有效了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190868V#1006FＯＫ。\n',
            '用魔法就行了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190869V好，那么上吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x000D)

    Jump('loc_2CF8')

    def _loc_28E1(): pass

    label('loc_28E1')

    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010190870V#1002F来了，是增援啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_B9(0x00, 0x000A)"),
            Expr.Ez,
            (Expr.Eval, "OP_B9(0x09, 0x000A)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_B9(0x00, 0x0014)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_B9(0x09, 0x0014)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_B9(0x00, 0x001E)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_B9(0x09, 0x001E)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_B9(0x00, 0x0032)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_B9(0x09, 0x0032)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_B9(0x00, 0x0046)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_B9(0x09, 0x0046)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_B9(0x00, 0x0041)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_B9(0x09, 0x0041)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2B43',
    )

    ChrTalk(
        0x010A,
        (
            '#0120190871V#1316F这只魔兽软绵绵的，\n',
            '武器应该很难起作用吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190872V#812F基本上这种时候\n',
            '就要使用魔法……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190873V艾丝蒂尔。\n',
            '准备好攻击魔法了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190874V#1015F嗯～这个嘛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190875V还是先确认一下\n',
            '导力器比较好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x010A, 0x0101, 400)

    ChrTalk(
        0x010A,
        (
            '#0120190876V#810F了解，设定好\n',
            '结晶回路后再前进吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※结晶回路的设置在[Orbment]画面进行。\n',
            '  要打开[Orbment]画面，\n',
            '  请在整备画面中点选[Orbment]栏。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_59()
    OP_A2(0x0001)
    OP_90(0x0000, 1500, 0, 0, 3000, 0x00)
    EventEnd(0x00)

    Return()

    def _loc_2B43(): pass

    label('loc_2B43')

    ChrTalk(
        0x010A,
        (
            '#0120190871V#1316F这只魔兽软绵绵的，\n',
            '武器应该很难起作用吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190878V#810F对付这种敌人，\n',
            '魔法的攻击很有效。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190868V#1006FＯＫ。\n',
            '用魔法就行了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190869V好，那么上吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※对于普通攻击无效的敌人，魔法是很有效的。\n',
            '  魔法可以进行长距离攻击，\n',
            '  但发动之前需要花费时间（驱动时间）。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '※使用魔法的话会消耗ＥＰ。\n',
            '  ＥＰ可在酒馆·饭店·回复点等地休息，\n',
            '  或者使用ＥＰ填充剂等道具来回复。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_59()
    OP_A2(0x0001)
    Call(0, 0x000D)
    def _loc_2CF8(): pass

    label('loc_2CF8')

    EventEnd(0x03)

    Return()

# id: 0x000D offset: 0x2CFB
@scena.Code('func_0D_2CFB')
def func_0D_2CFB():
    OP_59()

    @scena.Lambda('lambda_2D02')
    def lambda_2D02():
        OP_69(0x000A, 0x000001F4)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_2D02)

    @scena.Lambda('lambda_2D10')
    def lambda_2D10():
        OP_8E(0x0000, -25900, 0, 27870, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_2D10)

    @scena.Lambda('lambda_2D2B')
    def lambda_2D2B():
        OP_8E(0x0001, -25900, 0, 27870, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0001, 0x0000, lambda_2D2B)

    Sleep(300)

    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x0001, 0xFF)
    Battle(0x00000012, 0x00000000, 0x00, 0x0000, 0xFF)
    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x0001, 0xFF)

    Return()

# id: 0x000E offset: 0x2D63
@scena.Code('func_0E_2D63')
def func_0E_2D63():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x022C, 2, 0x1162)),
            Expr.Return,
        ),
        'loc_2D6B',
    )

    Return()

    def _loc_2D6B(): pass

    label('loc_2D6B')

    EventBegin(0x00)
    ChrTurnDirection(0x0000, 0x000B, 0)
    ChrTurnDirection(0x0001, 0x000B, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_2D89',
    )

    Call(0, 0x000F)

    Jump('loc_305F')

    def _loc_2D89(): pass

    label('loc_2D89')

    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010190881V#1007F呼，又出现了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x010A, 0x0101, 400)

    ChrTalk(
        0x010A,
        (
            '#0120190882V#816F艾丝蒂尔，\n',
            '这次使用战技看看吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190883V战技不仅仅是攻击，\n',
            '还有着各式各样的效果。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190884V如果ＣＰ在１００以上的话，\n',
            '就能使用更强力的Ｓ战技哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x010A, 400)

    ChrTalk(
        0x0101,
        (
            '#0010190885V#1011F原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190886V要扩大战术的幅度，\n',
            '战技是不可或缺的呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120190887V#816FＳ战技可作为\n',
            'Ｓ爆发技来使用，\n',
            '这可是战斗的关键呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190888V关于Ｓ爆发技的使用法，\n',
            '在战斗中复习看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190889V#1006F嗯！\n',
            '拜托你了，亚妮拉丝！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※战技的射程虽有限制，但可以立即发动。\n',
            '  使用战技时所需的ＣＰ，在攻击和受到伤害\n',
            '  的时候会自然积蓄。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '※当ＣＰ超过１００时\n',
            '　就能使用强力的战技：\n',
            '　Ｓ战技和Ｓ爆发技。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_A2(0x0002)
    Call(0, 0x000F)

    def _loc_305F(): pass

    label('loc_305F')

    EventEnd(0x03)

    Return()

# id: 0x000F offset: 0x3062
@scena.Code('func_0F_3062')
def func_0F_3062():
    OP_59()

    @scena.Lambda('lambda_3069')
    def lambda_3069():
        OP_69(0x000B, 0x000001F4)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_3069)

    @scena.Lambda('lambda_3077')
    def lambda_3077():
        OP_8E(0x0000, -36120, 0, 33700, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_3077)

    @scena.Lambda('lambda_3092')
    def lambda_3092():
        OP_8E(0x0001, -36120, 0, 33700, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0001, 0x0000, lambda_3092)

    Sleep(300)

    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x0001, 0xFF)
    Battle(0x00000013, 0x00000000, 0x00, 0x0000, 0xFF)
    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x0001, 0xFF)

    Return()

# id: 0x0010 offset: 0x30CA
@scena.Code('func_10_30CA')
def func_10_30CA():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x022C, 3, 0x1163)),
            Expr.Return,
        ),
        'loc_30D2',
    )

    Return()

    def _loc_30D2(): pass

    label('loc_30D2')

    EventBegin(0x00)
    ChrTurnDirection(0x0000, 0x000C, 0)
    ChrTurnDirection(0x0001, 0x000C, 0)
    AddCraft(ChrTable['艾丝蒂尔'], CraftTable['连锁战技１(２人协力)'])
    AddCraft(ChrTable['亚妮拉丝'], CraftTable['连锁战技１(２人协力)'])

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_3181',
    )

    ChrTalk(
        0x010A,
        (
            '#0120190890V#810F有机会的话\n',
            '就试试连锁战技吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190891V既然是新的攻击，\n',
            '就想早点试试看呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190892V#1006F嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0011)

    Jump('loc_3333')

    def _loc_3181(): pass

    label('loc_3181')

    ChrTalk(
        0x0101,
        (
            '#0010190893V#1011F这条通道到尽头了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120190894V#810F看来是的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190895V……艾丝蒂尔。\n',
            '要不要试试那个？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x010A, 400)

    ChrTalk(
        0x0101,
        (
            '#0010190896V#1011F#3P那个是…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190897V#1018F啊，连锁战技吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x010A, 0x0101, 400)

    ChrTalk(
        0x010A,
        (
            '#0120190898V#1310F嘿嘿，好不容易才特训出的\n',
            '全新联合攻击嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190899V为了要抓住感觉，\n',
            '必须早点在实战中尝试才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190900V#1006F#3P那么，有机会\n',
            '就试试看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120190901V#810F嗯！拜托你了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    OP_A2(0x0003)
    Call(0, 0x0011)

    def _loc_3333(): pass

    label('loc_3333')

    EventEnd(0x00)

    Return()

# id: 0x0011 offset: 0x3336
@scena.Code('func_11_3336')
def func_11_3336():
    OP_59()

    @scena.Lambda('lambda_333D')
    def lambda_333D():
        OP_69(0x000C, 0x000001F4)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_333D)

    @scena.Lambda('lambda_334B')
    def lambda_334B():
        OP_8E(0x0000, -36210, 0, 46770, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_334B)

    @scena.Lambda('lambda_3366')
    def lambda_3366():
        OP_8E(0x0001, -36210, 0, 46770, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0001, 0x0000, lambda_3366)

    Sleep(300)

    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x0001, 0xFF)
    Battle(0x00000010, 0x00000000, 0x00, 0x0000, 0xFF)
    OP_72(0x0001, 0x0800)
    OP_6F(0x0001, 0)
    OP_70(0x0001, 0x00000000)
    OP_73(0x0001)
    OP_71(0x0001, 0x0800)
    OP_72(0x0001, 0x0002)
    OP_71(0x0001, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x020C, 4, 0x1064)),
            Expr.Return,
        ),
        'loc_36BC',
    )

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_33CD'),
        (-1, 'loc_36BC'),
    )

    def _loc_33CD(): pass

    label('loc_33CD')

    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x0001, 0xFF)
    EventBegin(0x00)
    SetChrPos(0x0101, -35600, 0, 44540, 0)
    SetChrPos(0x010A, -37100, 0, 44540, 0)
    OP_6D(-36350, 400, 44540, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010190912V#1018F<FIXME>よし、問題なく倒せたわ。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190913V#1004F……あっと、そうだった。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x010A, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    OP_22(0x0026, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x010A, 0x0101, 400)

    ChrTalk(
        0x010A,
        (
            '#0120190914V#814F<FIXME>どうかした、エステルちゃん？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x010A, 400)

    ChrTalk(
        0x0101,
        (
            '#0010190915V#1016F<FIXME>あ、うん、魔獣手帳のこと。\n',
            'ちゃんと記録しておかなくっちゃ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120190916V#818F<FIXME>あ……そう言えば。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190917V#1006F<FIXME>ちょっと待ってて。\n',
            'すぐに書いちゃうから。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190863V#1029Fさらさらさら……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190864V#1006Fうん、これでバッチリね。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '<FIXME>※戦闘で戦った相手の情報は、\n',
            '  自動的に魔獣手帳に記録されます。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '<FIXME>※なお、戦闘に勝利するか\n',
            '  逃走するかによって\n',
            '  記録される内容は変化します。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    Jump('loc_36BC')

    def _loc_36BC(): pass

    label('loc_36BC')

    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x0001, 0xFF)

    Return()

# id: 0x0012 offset: 0x36C5
@scena.Code('func_12_36C5')
def func_12_36C5():
    EventBegin(0x00)
    OP_6D(-26300, 0, 26230, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(11000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -36520, 0, 36440, 0)
    SetChrPos(0x00F7, -35650, 0, 35240, 0)

    @scena.Lambda('lambda_372C')
    def lambda_372C():
        OP_94(0x01, 0x00FE, 0x0000, 0x00001770, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_372C)

    Sleep(250)

    @scena.Lambda('lambda_3747')
    def lambda_3747():
        OP_94(0x01, 0x00FE, 0x0000, 0x00001770, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_3747)

    @scena.Lambda('lambda_375D')
    def lambda_375D():
        OP_6D(-36080, 0, 43850, 4500)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_375D)

    @scena.Lambda('lambda_3775')
    def lambda_3775():
        OP_6C(45000, 4500)

        ExitThread()

    DispatchAsync(0x0001, 0x0000, lambda_3775)

    FadeIn(1500, 0)
    OP_0D()
    WaitForThreadExit(0x0000, 0x0001)
    WaitForThreadExit(0x0001, 0x0001)
    WaitForThreadExit(0x0000, 0x0000)
    WaitForThreadExit(0x0001, 0x0000)
    Sleep(1000)

    AddCraft(ChrTable['艾丝蒂尔'], CraftTable['连锁战技１(２人协力)'])
    AddCraft(ChrTable['亚妮拉丝'], CraftTable['连锁战技１(２人协力)'])

    ChrTalk(
        0x0101,
        (
            '#0010190902V#1015F#3P呼，总之\n',
            '一路把魔兽打败了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190893V#1011F这条通道也到尽头了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120190904V#810F嗯，似乎是吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190905V……对了，艾丝蒂尔。\n',
            '要不要试试那个？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x010A, 400)

    ChrTalk(
        0x0101,
        (
            '#0010190906V#1011F#3P那个是…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190897V#1018F啊，连锁战技吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x010A, 0x0101, 400)

    ChrTalk(
        0x010A,
        (
            '#0120190898V#1310F嘿嘿，因为是专门特训的\n',
            '全新联合攻击嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190909V为了要抓住感觉，\n',
            '赶快在实战中试试如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190910V#1006F#3P那么，有机会\n',
            '就试试看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120190911V#816F嗯！　拜托你了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()

    @scena.Lambda('lambda_3997')
    def lambda_3997():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_3997)

    OP_8C(0x0101, 0, 400)
    OP_A2(0x0003)
    OP_6A(0x00FF)
    Call(0, 0x0011)

    Return()

# id: 0x0013 offset: 0x39B1
@scena.Code('func_13_39B1')
def func_13_39B1():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3A02',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '导力好像停止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Jump('loc_3BBD')

    def _loc_3A02(): pass

    label('loc_3A02')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '这是一台可供旅行者回复体力的导力器装置。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

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
        32,
        1,
        (
            TXT(0x00, '在这里休息\n'),
            TXT(0x01, '离开\n'),
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
    OP_56(0x00)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3BA2',
    )

    FadeIn(100, 0)
    Sleep(500)

    OP_26(13)
    OP_82(0x00, 0x02)
    PlayEffect(0x00, 0x00, 0x00FF, -5000, 1000, 6730, 0, 0, 0, 700, 700, 700, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0002, 0)
    OP_70(0x0002, 0x00000032)
    OP_73(0x0002)
    OP_20(0x00000BB8)
    OP_22(0x000C, 0x00, 0x64)
    OP_82(0x00, 0x02)
    LoadEffect(0x01, 'map\\\\mp027_01.eff')
    PlayEffect(0x01, 0x01, 0x00FF, -5000, 1000, 6730, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    FadeOut(1000, 0, -1)
    Sleep(700)

    OP_22(0x000D, 0x00, 0x64)
    OP_0D()
    SetChrStatus(0x00FF, 0xFE, 0)
    OP_69(0x0000, 0x00000000)
    OP_30(0x01)
    Sleep(3500)

    OP_82(0x01, 0x02)
    PlayEffect(0x00, 0x00, 0x00FF, -5000, 1000, 6730, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0002, 0)
    OP_1E()
    FadeIn(1000, 0)
    OP_56(0x00)
    TalkEnd(0x00FF)

    Return()

    def _loc_3BA2(): pass

    label('loc_3BA2')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3BBC',
    )

    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

    def _loc_3BBC(): pass

    label('loc_3BBC')

    Return()

    def _loc_3BBD(): pass

    label('loc_3BBD')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
