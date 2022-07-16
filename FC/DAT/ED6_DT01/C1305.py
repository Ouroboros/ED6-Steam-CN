import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C1305_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1305   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '空贼莱尔'),
    TXT(0x02, '空贼罗尔'),
    TXT(0x03, '空贼'),
    TXT(0x04, '空贼'),
    TXT(0x05, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'C1305.x'
    header.mapIndex       = 52
    header.bgm            = 31
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xE2D
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
            word_3A         = 52,
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
        ('ED6_DT07/CH00360._CH', 'ED6_DT07/CH00360P._CP'),
        ('ED6_DT07/CH00364._CH', 'ED6_DT07/CH00364P._CP'),
        ('ED6_DT07/CH00361._CH', 'ED6_DT07/CH00361P._CP'),
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00110._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP'),
        ('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP'),
        ('ED6_DT09/CH10380._CH', 'ED6_DT09/CH10380P._CP'),
        ('ED6_DT09/CH10381._CH', 'ED6_DT09/CH10381P._CP'),
        ('ED6_DT09/CH10390._CH', 'ED6_DT09/CH10390P._CP'),
        ('ED6_DT09/CH10391._CH', 'ED6_DT09/CH10391P._CP'),
        ('ED6_DT09/CH10250._CH', 'ED6_DT09/CH10250P._CP'),
        ('ED6_DT09/CH10251._CH', 'ED6_DT09/CH10251P._CP'),
        ('ED6_DT06/CH20074._CH', 'ED6_DT06/CH20074P._CP'),
    ]

# id: 0x10002 offset: 0x11A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -2300,
            z                   = 500,
            y                   = -2700,
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
            x                   = 1000,
            z                   = 500,
            y                   = -1900,
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
            x                   = -500,
            z                   = 500,
            y                   = 900,
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
            x                   = -3200,
            z                   = 500,
            y                   = -700,
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
    )

# id: 0x10003 offset: 0x19A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -5080,
            z           = 0,
            y           = 890,
            word_0C     = 0x0085,
            word_0E     = 0x0009,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00A4,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 1060,
            z           = 0,
            y           = -138590,
            word_0C     = 0x010B,
            word_0E     = 0x000B,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00AB,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 65660,
            z           = 0,
            y           = -21310,
            word_0C     = 0x00A7,
            word_0E     = 0x000B,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00AB,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x1EE
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x1EE
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -51050,
            triggerZ            = 0,
            triggerY            = -136010,
            triggerRange        = 800,
            actorX              = -51050,
            actorZ              = 1000,
            actorY              = -136010,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -164160,
            triggerZ            = 0,
            triggerY            = -193160,
            triggerRange        = 1000,
            actorX              = -164160,
            actorZ              = 1500,
            actorY              = -193160,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -54870,
            triggerZ            = 0,
            triggerY            = 46490,
            triggerRange        = 1000,
            actorX              = -54740,
            actorZ              = 1500,
            actorY              = 47090,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -206690,
            triggerZ            = 0,
            triggerY            = -155420,
            triggerRange        = 1000,
            actorX              = -206660,
            actorZ              = 1500,
            actorY              = -154670,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x27E
@scena.Code('PreInit')
def PreInit():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000075, 'loc_28A'),
        (-1, 'loc_29D'),
    )

    def _loc_28A(): pass

    label('loc_28A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 0, 0x358)),
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 3, 0x35B)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_29A',
    )

    Event(0, 0x0005)

    def _loc_29A(): pass

    label('loc_29A')

    Jump('loc_29D')

    def _loc_29D(): pass

    label('loc_29D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 3, 0x35B)),
            Expr.Return,
        ),
        'loc_34C',
    )

    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, -116480, 0, 2830, 80)
    SetChrPos(0x0009, -117700, 0, 3160, 360)
    SetChrPos(0x000A, -119190, 0, 2820, 125)
    SetChrPos(0x000B, -119490, 0, 1060, 200)
    SetChrChipByIndex(0x000A, 13)
    SetChrChipByIndex(0x000B, 13)
    SetChrChipByIndex(0x0008, 13)
    SetChrChipByIndex(0x0009, 13)

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)

    def _loc_34C(): pass

    label('loc_34C')

    Return()

# id: 0x0001 offset: 0x34D
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0071, 1, 0x389)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_35F',
    )

    OP_6F(0x0001, 0)

    Jump('loc_366')

    def _loc_35F(): pass

    label('loc_35F')

    OP_6F(0x0001, 60)

    def _loc_366(): pass

    label('loc_366')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006D, 6, 0x36E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_378',
    )

    OP_6F(0x0002, 0)

    Jump('loc_37F')

    def _loc_378(): pass

    label('loc_378')

    OP_6F(0x0002, 60)

    def _loc_37F(): pass

    label('loc_37F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006D, 7, 0x36F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_391',
    )

    OP_6F(0x0003, 0)

    Jump('loc_398')

    def _loc_391(): pass

    label('loc_391')

    OP_6F(0x0003, 60)

    def _loc_398(): pass

    label('loc_398')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 4, 0x35C)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 0, 0x358)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3B0',
    )

    OP_10(0x00, 0x00)
    OP_10(0x01, 0x00)
    OP_10(0x02, 0x01)

    Jump('loc_3B9')

    def _loc_3B0(): pass

    label('loc_3B0')

    OP_10(0x00, 0x00)
    OP_10(0x01, 0x01)
    OP_10(0x02, 0x00)

    def _loc_3B9(): pass

    label('loc_3B9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006A, 5, 0x355)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3D5',
    )

    OP_1B(0x22, 0x00, 0x0003)
    OP_6F(0x0000, 0)
    OP_72(0x0000, 0x0010)

    Jump('loc_3D9')

    def _loc_3D5(): pass

    label('loc_3D5')

    OP_64(0x00, 0x0001)

    def _loc_3D9(): pass

    label('loc_3D9')

    Return()

# id: 0x0002 offset: 0x3DA
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3EF',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_3EF(): pass

    label('loc_3EF')

    Return()

# id: 0x0003 offset: 0x3F0
@scena.Code('func_03_3F0')
def func_03_3F0():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006A, 5, 0x355)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5B6',
    )

    ClearMapFlags(0x00000001)
    EventBegin(0x00)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_4DD',
    )

    @scena.Lambda('lambda_041A')
    def lambda_041A():
        CameraMove(-46410, 0, -137150, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_041A)

    Sleep(600)

    SetChrDirection(0x0102, 270, 400)

    ChrTalk(
        0x0102,
        (
            '#0020031406V#012F等一下……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031407V从那道门可以听到说话的声音。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0482')
    def lambda_0482():
        SetChrDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_0482)

    @scena.Lambda('lambda_0490')
    def lambda_0490():
        SetChrDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0490)

    SetChrDirection(0x0103, 270, 400)

    ChrTalk(
        0x0103,
        (
            '#0030031408V#022F看起来空贼就在这里呢。\n',
            '先把他们解决掉吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_59B')

    def _loc_4DD(): pass

    label('loc_4DD')

    @scena.Lambda('lambda_04E3')
    def lambda_04E3():
        CameraMove(-46410, 0, -137150, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_04E3)

    Sleep(600)

    SetChrDirection(0x0104, 270, 400)

    ChrTalk(
        0x0104,
        (
            '#0040031409V#033F哎呀……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040031410V从那道门可以听到说话的声音呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_054B')
    def lambda_054B():
        SetChrDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_054B)

    @scena.Lambda('lambda_0559')
    def lambda_0559():
        SetChrDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0559)

    SetChrDirection(0x0101, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010031411V#002F难道是空贼？\n',
            '那先把这里解决掉吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_59B(): pass

    label('loc_59B')

    ChrMoveToRelative(0x0000, -1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_5B6(): pass

    label('loc_5B6')

    Return()

# id: 0x0004 offset: 0x5B7
@scena.Code('func_04_5B7')
def func_04_5B7():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006A, 5, 0x355)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6BC',
    )

    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '有男人说话的声音传出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0102,
        (
            '#0020031405V#012F好像有空贼的成员在里面，\n',
            '……要闯进去吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
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
        10,
        0,
        (
            TXT(0x00, '【闯进去】\n'),
            TXT(0x01, '【还是算了】\n'),
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
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000001, 'loc_6A8'),
        (0x00000000, 'loc_6AD'),
        (-1, 'loc_6BC'),
    )

    def _loc_6A8(): pass

    label('loc_6A8')

    EventEnd(0x01)

    Jump('loc_6BC')

    def _loc_6AD(): pass

    label('loc_6AD')

    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/C1304._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_6BC')

    def _loc_6BC(): pass

    label('loc_6BC')

    Return()

# id: 0x0005 offset: 0x6BD
@scena.Code('func_05_6BD')
def func_05_6BD():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(-114820, 0, -1080, 0)
    CameraSetDistance(2800, 0)
    SetChrPos(0x0008, -113140, 0, -920, 225)
    SetChrPos(0x0009, -113210, 0, 90, 225)
    SetChrPos(0x000A, -112860, 0, 1370, 225)
    SetChrPos(0x000B, -112680, 0, -2000, 270)
    SetChrPos(0x0101, -116790, 0, -2600, 90)
    SetChrPos(0x0102, -118090, 0, -3150, 90)
    SetChrPos(0x0103, -117660, 0, -1530, 90)
    SetChrPos(0x0104, -117180, 0, -4120, 45)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x0008, 0x0080)
    SetChrChipByIndex(0x0101, 3)
    SetChrChipByIndex(0x0102, 4)
    SetChrChipByIndex(0x0103, 5)
    SetChrChipByIndex(0x0104, 6)

    ChrTalk(
        0x0008,
        (
            '#0990031698V#2P嘁，果然来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1270031699V我们根本没想过要赢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1270031700V只要争取到能让\n',
            '大哥他们逃跑的时间就够了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040031701V#030F呵呵，为了保护首领\n',
            '而情愿将自身当作盾牌吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040031702V虽说有点愚蠢，\n',
            '但却是值得敬佩的气概嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030031703V#026F那我们全力作战\n',
            '也算是对他们的尊重吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031704V#024F来吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    SetChrChipByIndex(0x000A, 2)
    SetChrChipByIndex(0x000B, 2)
    SetChrChipByIndex(0x0008, 2)
    SetChrChipByIndex(0x0009, 2)

    @scena.Lambda('lambda_08EB')
    def lambda_08EB():
        OP_92(0x00FE, 0x0102, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_08EB)

    @scena.Lambda('lambda_0900')
    def lambda_0900():
        OP_92(0x00FE, 0x0102, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0900)

    @scena.Lambda('lambda_0915')
    def lambda_0915():
        OP_92(0x00FE, 0x0102, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0915)

    @scena.Lambda('lambda_092A')
    def lambda_092A():
        OP_92(0x00FE, 0x0102, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_092A)

    Sleep(400)

    Battle(0x0000038C, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_957'),
        (-1, 'loc_95A'),
    )

    def _loc_957(): pass

    label('loc_957')

    OP_B4(0x00)

    Return()

    def _loc_95A(): pass

    label('loc_95A')

    SetChrPos(0x0008, -116480, 0, 2830, 80)
    SetChrPos(0x0009, -117700, 0, 3160, 360)
    SetChrPos(0x000A, -119190, 0, 2820, 125)
    SetChrPos(0x000B, -119490, 0, 1060, 200)
    SetChrChipByIndex(0x000A, 13)
    SetChrChipByIndex(0x000B, 13)
    SetChrChipByIndex(0x0008, 13)
    SetChrChipByIndex(0x0009, 13)

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    SetChrPos(0x0101, -115860, 0, 30, 270)
    SetChrPos(0x0102, -115860, 0, 30, 270)
    SetChrPos(0x0103, -115860, 0, 30, 270)
    SetChrPos(0x0104, -115860, 0, 30, 270)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0103, 0xFF)
    TerminateThread(0x0104, 0xFF)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0103, 65535)
    SetChrChipByIndex(0x0104, 65535)
    CameraMove(-115860, 0, 30, 0)
    CameraSetDistance(2600, 0)
    FadeIn(1000, 0)
    SetScenaFlags(ScenaFlag(0x006B, 3, 0x35B))
    EventEnd(0x00)

    Return()

# id: 0x0006 offset: 0xA7F
@scena.Code('func_06_A7F')
def func_06_A7F():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0071, 1, 0x389)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B6F',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x014E, 1)"),
            Expr.Return,
        ),
        'loc_AF5',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '宝石戒指',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0071, 1, 0x389))

    Jump('loc_B6C')

    def _loc_AF5(): pass

    label('loc_AF5')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '宝石戒指',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '宝石戒指',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0)

    def _loc_B6C(): pass

    label('loc_B6C')

    Jump('loc_BA5')

    def _loc_B6F(): pass

    label('loc_B6F')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱里什么东西都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    WaitEffect(0x0F, 0x10)
    def _loc_BA5(): pass

    label('loc_BA5')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0xBB3
@scena.Code('func_07_BB3')
def func_07_BB3():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006D, 6, 0x36E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C9D',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x003F, 1)"),
            Expr.Return,
        ),
        'loc_C27',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '毒蝎鞭',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x006D, 6, 0x36E))

    Jump('loc_C9A')

    def _loc_C27(): pass

    label('loc_C27')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '毒蝎鞭',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '毒蝎鞭',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0)

    def _loc_C9A(): pass

    label('loc_C9A')

    Jump('loc_CD3')

    def _loc_C9D(): pass

    label('loc_C9D')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱里什么东西都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    WaitEffect(0x0F, 0x11)
    def _loc_CD3(): pass

    label('loc_CD3')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0xCE1
@scena.Code('func_08_CE1')
def func_08_CE1():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006D, 7, 0x36F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DD7',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0003, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01FE, 1)"),
            Expr.Return,
        ),
        'loc_D59',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            'ＥＰ填充剂',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x006D, 7, 0x36F))

    Jump('loc_DD4')

    def _loc_D59(): pass

    label('loc_D59')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            'ＥＰ填充剂',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            'ＥＰ填充剂',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0003, 60)
    OP_70(0x0003, 0)

    def _loc_DD4(): pass

    label('loc_DD4')

    Jump('loc_E0D')

    def _loc_DD7(): pass

    label('loc_DD7')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱里什么东西都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    WaitEffect(0x0F, 0x12)
    def _loc_E0D(): pass

    label('loc_E0D')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
