import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import R0302_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R0302   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'rolent'
    header.mapModel       = 'R0302.x'
    header.mapIndex       = 21
    header.bgm            = 22
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
        ('ED6_DT09/CH11050._CH', 'ED6_DT09/CH11050P._CP'),
        ('ED6_DT09/CH11051._CH', 'ED6_DT09/CH11051P._CP'),
        ('ED6_DT09/CH10100._CH', 'ED6_DT09/CH10100P._CP'),
        ('ED6_DT09/CH10101._CH', 'ED6_DT09/CH10101P._CP'),
    ]

# id: 0x10001 offset: 0xCA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '雾调整',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0189,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '洛连特方向',
            x                   = -146110,
            z                   = 10,
            y                   = -9950,
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
        ScenaNpcData(
            name                = '玛鲁加矿山方向',
            x                   = -163040,
            z                   = 3920,
            y                   = 102800,
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

# id: 0x10002 offset: 0x12A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = -156000,
            z           = 2000,
            y           = 18000,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0066,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -146000,
            z           = 2100,
            y           = 27000,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0068,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -130000,
            z           = 4100,
            y           = 26000,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0064,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -117000,
            z           = 4100,
            y           = 31000,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0067,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -154000,
            z           = 2000,
            y           = 47000,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0069,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -156000,
            z           = 4000,
            y           = 68000,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0065,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x1D2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x1D2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -109910,
            triggerZ            = 5850,
            triggerY            = 62020,
            triggerRange        = 1000,
            actorX              = -109910,
            actorZ              = 7350,
            actorY              = 62020,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1F6
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 0, 0x1810)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_226',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 6, 0x180E)),
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 7, 0x180F)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_210',
    )

    Event(0, func_06_FDA)

    Jump('loc_226')

    def _loc_210(): pass

    label('loc_210')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 6, 0x180E)),
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 7, 0x180F)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_222',
    )

    Event(0, func_05_B4A)

    Jump('loc_226')

    def _loc_222(): pass

    label('loc_222')

    Event(0, func_04_4BD)

    def _loc_226(): pass

    label('loc_226')

    Return()

# id: 0x0001 offset: 0x227
@scena.Code('func_01_227')
def func_01_227():
    OP_16(0x02, 4000, -266000, -86000, 2293776)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0326, 2, 0x1932)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_24B',
    )

    OP_6F(0x0000, 0)

    Jump('loc_252')

    def _loc_24B(): pass

    label('loc_24B')

    OP_6F(0x0000, 60)

    def _loc_252(): pass

    label('loc_252')

    StopEffect(0x80, 0x00)
    StopEffect(0x81, 0x00)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_30A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_289',
    )

    MapSetFlags(0x00000010)
    OP_11(0xE6, 0xF0, 0xFF, 0, 60000, 0)
    OP_C4(0x00, 0x00000004)

    Jump('loc_30A')

    def _loc_289(): pass

    label('loc_289')

    OP_11(0xE6, 0xF0, 0xFF, 0, 80000, 0)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    CreateThread(0x0008, 0x00, 0x00, func_02_30B)

    def _loc_30A(): pass

    label('loc_30A')

    Return()

# id: 0x0002 offset: 0x30B
@scena.Code('func_02_30B')
def func_02_30B():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3A0',
    )

    ExecExpressionWithVar(
        0x37,
        (
            (Expr.PushValueByIndex, 0x67),
            (Expr.PushLong, 0x1388),
            Expr.Sub,
            (Expr.PushLong, 0xF),
            Expr.Mul,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushValueByIndex, 0x37),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_33E',
    )

    ExecExpressionWithVar(
        0x37,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_353')

    def _loc_33E(): pass

    label('loc_33E')

    If(
        (
            (Expr.PushValueByIndex, 0x37),
            (Expr.PushLong, 0x7D00),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_353',
    )

    ExecExpressionWithVar(
        0x37,
        (
            (Expr.PushLong, 0x7D00),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_353(): pass

    label('loc_353')

    ExecExpressionWithVar(
        0x38,
        (
            (Expr.PushValueByIndex, 0x67),
            (Expr.PushLong, 0x1388),
            Expr.Sub,
            (Expr.PushLong, 0xF),
            Expr.Mul,
            (Expr.PushLong, 0x13880),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushValueByIndex, 0x38),
            (Expr.PushLong, 0x13880),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_383',
    )

    ExecExpressionWithVar(
        0x38,
        (
            (Expr.PushLong, 0x13880),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_398')

    def _loc_383(): pass

    label('loc_383')

    If(
        (
            (Expr.PushValueByIndex, 0x38),
            (Expr.PushLong, 0x222E0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_398',
    )

    ExecExpressionWithVar(
        0x38,
        (
            (Expr.PushLong, 0x222E0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_398(): pass

    label('loc_398')

    Sleep(10)

    Jump('func_02_30B')

    def _loc_3A0(): pass

    label('loc_3A0')

    Return()

# id: 0x0003 offset: 0x3A1
@scena.Code('func_03_3A1')
def func_03_3A1():
    UnlockAchievement(0x02, 0x01C9, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0326, 2, 0x1932)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_47E',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['中回复药'], 1)"),
            Expr.Return,
        ),
        'loc_415',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['中回复药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0326, 2, 0x1932))

    Jump('loc_47B')

    def _loc_415(): pass

    label('loc_415')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['中回复药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['中回复药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0)

    def _loc_47B(): pass

    label('loc_47B')

    Jump('loc_4AF')

    def _loc_47E(): pass

    label('loc_47E')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_4AF(): pass

    label('loc_4AF')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x4BD
@scena.Code('func_04_4BD')
def func_04_4BD():
    EventBegin(0x00)
    FadeOut(0, 0, -1)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4E7',
    )

    Call(0, 0x0007)
    FadeIn(0, 0)
    Call(0, 0x0008)

    def _loc_4E7(): pass

    label('loc_4E7')

    CameraMove(-145490, -10, 2670, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2980, 0)
    OP_6C(134000, 0)
    OP_6E(243, 0)
    ChrSetPos(0x0101, -145500, -10, -3730, 0)
    ChrSetPos(0x0103, -146500, -10, -3730, 0)
    ChrSetPos(0x00F8, -145250, -10, -4730, 0)
    ChrSetPos(0x00F9, -146750, -10, -4730, 0)

    @scena.Lambda('lambda_056E')
    def lambda_056E():
        ChrMoveToRelative(0x00FE, 0, 0, 7000, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_056E)

    Sleep(100)

    @scena.Lambda('lambda_058E')
    def lambda_058E():
        ChrMoveToRelative(0x00FE, 0, 0, 7000, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_058E)

    Sleep(200)

    @scena.Lambda('lambda_05AE')
    def lambda_05AE():
        ChrMoveToRelative(0x00FE, 0, 0, 7000, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_05AE)

    Sleep(100)

    @scena.Lambda('lambda_05CE')
    def lambda_05CE():
        ChrMoveToRelative(0x00FE, 0, 0, 7000, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_05CE)

    FadeIn(1000, 0)
    WaitForThreadExit(0x00F9, 0x0001)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010281202V#1004F#6P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0619')
    def lambda_0619():
        ChrWalkTo(0x00FE, -145500, 60, 8270, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0619)

    Sleep(100)

    @scena.Lambda('lambda_0639')
    def lambda_0639():
        ChrWalkTo(0x00FE, -146710, 30, 8189, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_0639)

    Sleep(200)

    @scena.Lambda('lambda_0659')
    def lambda_0659():
        ChrWalkTo(0x00FE, -145300, 60, 6820, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_0659)

    Sleep(100)

    @scena.Lambda('lambda_0679')
    def lambda_0679():
        ChrWalkTo(0x00FE, -146730, 30, 6650, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_0679)

    @scena.Lambda('lambda_0694')
    def lambda_0694():
        CameraMove(-145700, 60, 7100, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0694)

    @scena.Lambda('lambda_06AC')
    def lambda_06AC():
        CameraSetDistance(3540, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_06AC)

    ChrSetDirection(0x0101, 45, 400)
    Sleep(50)

    ChrSetDirection(0x0103, 0, 400)
    Sleep(30)

    ChrSetDirection(0x00F8, 0, 400)
    Sleep(50)

    ChrSetDirection(0x00F9, 320, 400)
    Sleep(300)

    ChrSetDirection(0x0101, 0, 400)
    Sleep(50)

    ChrSetDirection(0x0103, 45, 400)
    Sleep(30)

    ChrSetDirection(0x00F8, 320, 400)
    Sleep(50)

    ChrSetDirection(0x00F9, 0, 400)
    Sleep(300)

    ChrSetDirection(0x0101, 320, 400)
    Sleep(50)

    ChrSetDirection(0x0103, 320, 400)
    Sleep(30)

    ChrSetDirection(0x00F8, 0, 400)
    Sleep(50)

    ChrSetDirection(0x00F9, 45, 400)
    Sleep(300)

    ChrSetDirection(0x0101, 0, 400)
    Sleep(50)

    ChrSetDirection(0x0103, 45, 400)
    Sleep(30)

    ChrSetDirection(0x00F8, 45, 400)
    Sleep(50)

    ChrSetDirection(0x00F9, 320, 400)
    Sleep(300)

    ChrSetDirection(0x0101, 180, 400)
    Sleep(50)

    ChrSetDirection(0x0103, 180, 400)
    Sleep(30)

    ChrSetDirection(0x00F8, 0, 400)
    Sleep(50)

    ChrSetDirection(0x00F9, 0, 400)
    Sleep(300)

    WaitForThreadExit(0x00F9, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7F0',
    )

    ChrTalk(
        0x0107,
        (
            '#0070281162V#560F哇……\n',
            '一下子就明朗了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8E9')

    def _loc_7F0(): pass

    label('loc_7F0')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_82E',
    )

    ChrTalk(
        0x0106,
        (
            '#0050281163V#051F嘿……\n',
            '突然就明朗了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8E9')

    def _loc_82E(): pass

    label('loc_82E')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_86E',
    )

    ChrTalk(
        0x0104,
        (
            '#0040281205V#030F哦……\n',
            '一下子就明朗了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8E9')

    def _loc_86E(): pass

    label('loc_86E')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8AE',
    )

    ChrTalk(
        0x0105,
        (
            '#0060281165V#048F呵呵……\n',
            '忽然就明朗了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8E9')

    def _loc_8AE(): pass

    label('loc_8AE')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8E9',
    )

    ChrTalk(
        0x0108,
        (
            '#0080281166V#070F呼……\n',
            '突然就明朗了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8E9(): pass

    label('loc_8E9')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_931',
    )

    ChrTalk(
        0x0107,
        (
            '#0070281167V#061F雾的覆盖范围\n',
            '似乎就到这里为止呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A4E')

    def _loc_931(): pass

    label('loc_931')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_979',
    )

    ChrTalk(
        0x0106,
        (
            '#0050281209V#051F雾的覆盖范围\n',
            '似乎就到这里为止啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A4E')

    def _loc_979(): pass

    label('loc_979')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9C1',
    )

    ChrTalk(
        0x0104,
        (
            '#0040281210V#030F雾的覆盖范围\n',
            '似乎就到这里为止啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A4E')

    def _loc_9C1(): pass

    label('loc_9C1')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A09',
    )

    ChrTalk(
        0x0105,
        (
            '#0060281170V#048F雾的覆盖范围\n',
            '似乎就到这里为止呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A4E')

    def _loc_A09(): pass

    label('loc_A09')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A4E',
    )

    ChrTalk(
        0x0108,
        (
            '#0080281212V#070F雾的覆盖范围\n',
            '似乎就到这里为止啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A4E(): pass

    label('loc_A4E')

    ChrTalk(
        0x0103,
        (
            '#0030281213V#026F玛鲁加山道，距离洛连特市\n',
            '大约１４０塞尔矩的地点……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281214V#022F不但浓雾的范围很广，\n',
            '还有魔兽游荡，非常危险。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281174V#1015F#6P嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281175V调查完其它地方后，\n',
            '必须赶快向爱娜姐报告才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0302, 0, 0x1810))
    OP_28(0x008F, 0x02, 0x0040)
    OP_28(0x008F, 0x01, 0x0080)
    EventEnd(0x00)

    Return()

# id: 0x0005 offset: 0xB4A
@scena.Code('func_05_B4A')
def func_05_B4A():
    EventBegin(0x00)
    FadeOut(0, 0, -1)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_B74',
    )

    Call(0, 0x0007)
    FadeIn(0, 0)
    Call(0, 0x0008)

    def _loc_B74(): pass

    label('loc_B74')

    CameraMove(-145490, -10, 2670, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2980, 0)
    OP_6C(134000, 0)
    OP_6E(243, 0)
    ChrSetPos(0x0101, -145500, -10, -730, 0)
    ChrSetPos(0x0103, -146500, -10, -730, 0)
    ChrSetPos(0x00F8, -145250, -10, -1730, 0)
    ChrSetPos(0x00F9, -146750, -10, -1730, 0)

    @scena.Lambda('lambda_0BFB')
    def lambda_0BFB():
        ChrWalkTo(0x00FE, -145500, 60, 8270, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0BFB)

    Sleep(100)

    @scena.Lambda('lambda_0C1B')
    def lambda_0C1B():
        ChrWalkTo(0x00FE, -146710, 30, 8189, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_0C1B)

    Sleep(200)

    @scena.Lambda('lambda_0C3B')
    def lambda_0C3B():
        ChrWalkTo(0x00FE, -145300, 60, 6820, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_0C3B)

    Sleep(100)

    @scena.Lambda('lambda_0C5B')
    def lambda_0C5B():
        ChrWalkTo(0x00FE, -146730, 30, 6650, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_0C5B)

    @scena.Lambda('lambda_0C76')
    def lambda_0C76():
        CameraMove(-145700, 60, 7100, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0C76)

    @scena.Lambda('lambda_0C8E')
    def lambda_0C8E():
        CameraSetDistance(3540, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0C8E)

    FadeIn(1000, 0)
    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x00F9, 0x0001)
    OP_0D()

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CE3',
    )

    ChrTalk(
        0x0107,
        (
            '#0070281176V#061F嘿嘿，已经晴了⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DCF')

    def _loc_CE3(): pass

    label('loc_CE3')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D1F',
    )

    ChrTalk(
        0x0106,
        (
            '#0050281218V#051F呼……\n',
            '雾终于散了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DCF')

    def _loc_D1F(): pass

    label('loc_D1F')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D5B',
    )

    ChrTalk(
        0x0104,
        (
            '#0040281219V#030F嗯……\n',
            '雾终于散了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DCF')

    def _loc_D5B(): pass

    label('loc_D5B')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D96',
    )

    ChrTalk(
        0x0105,
        (
            '#0060281179V#048F……似乎已经晴了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DCF')

    def _loc_D96(): pass

    label('loc_D96')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_DCF',
    )

    ChrTalk(
        0x0108,
        (
            '#0080281221V#070F嗯……\n',
            '雾终于散了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DCF(): pass

    label('loc_DCF')

    ChrTalk(
        0x0103,
        (
            '#0030281213V#026F玛鲁加山道，距离洛连特市\n',
            '大约１４０塞尔矩的地点……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281214V#022F不但浓雾的范围很广，\n',
            '还有魔兽游荡，非常危险。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_EF5',
    )

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
        0,
        (
            TXT(0x00, '【◇调查过米尔西街道】\n'),
            TXT(0x01, '【◇调查过艾利兹街道】\n'),
            TXT(0x02, '【◇不变更】\n'),
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
        (0x00000000, 'loc_EE3'),
        (0x00000001, 'loc_EEC'),
        (-1, 'loc_EF5'),
    )

    def _loc_EE3(): pass

    label('loc_EE3')

    ClearScenaFlags(ScenaFlag(0x0301, 6, 0x180E))
    SetScenaFlags(ScenaFlag(0x0301, 7, 0x180F))

    Jump('loc_EF5')

    def _loc_EEC(): pass

    label('loc_EEC')

    SetScenaFlags(ScenaFlag(0x0301, 6, 0x180E))
    ClearScenaFlags(ScenaFlag(0x0301, 7, 0x180F))

    Jump('loc_EF5')

    def _loc_EF5(): pass

    label('loc_EF5')

    ChrTurnDirection(0x0101, 0x0103, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 7, 0x180F)),
            Expr.Return,
        ),
        'loc_F67',
    )

    ChrTalk(
        0x0101,
        (
            '#0010281183V#1006F#5P嗯……\n',
            '就向爱娜姐报告吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281184V接下来，只剩下\n',
            '艾利兹街道了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FC8')

    def _loc_F67(): pass

    label('loc_F67')

    ChrTalk(
        0x0101,
        (
            '#0010281183V#1006F#5P嗯……\n',
            '就向爱娜姐报告吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281227V接下来，只剩下\n',
            '米尔西街道了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FC8(): pass

    label('loc_FC8')

    SetScenaFlags(ScenaFlag(0x0302, 0, 0x1810))
    OP_28(0x008F, 0x02, 0x0040)
    OP_28(0x008F, 0x01, 0x0080)
    EventEnd(0x00)

    Return()

# id: 0x0006 offset: 0xFDA
@scena.Code('func_06_FDA')
def func_06_FDA():
    EventBegin(0x00)
    FadeOut(0, 0, -1)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1004',
    )

    Call(0, 0x0007)
    FadeIn(0, 0)
    Call(0, 0x0008)

    def _loc_1004(): pass

    label('loc_1004')

    CameraMove(-145490, -10, 2670, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2980, 0)
    OP_6C(134000, 0)
    OP_6E(243, 0)
    ChrSetPos(0x0101, -145500, -10, -730, 0)
    ChrSetPos(0x0103, -146500, -10, -730, 0)
    ChrSetPos(0x00F8, -145250, -10, -1730, 0)
    ChrSetPos(0x00F9, -146750, -10, -1730, 0)

    @scena.Lambda('lambda_108B')
    def lambda_108B():
        ChrWalkTo(0x00FE, -145500, 60, 8270, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_108B)

    Sleep(100)

    @scena.Lambda('lambda_10AB')
    def lambda_10AB():
        ChrWalkTo(0x00FE, -146710, 30, 8189, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_10AB)

    Sleep(200)

    @scena.Lambda('lambda_10CB')
    def lambda_10CB():
        ChrWalkTo(0x00FE, -145300, 60, 6820, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_10CB)

    Sleep(100)

    @scena.Lambda('lambda_10EB')
    def lambda_10EB():
        ChrWalkTo(0x00FE, -146730, 30, 6650, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_10EB)

    @scena.Lambda('lambda_1106')
    def lambda_1106():
        CameraMove(-145700, 60, 7100, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1106)

    @scena.Lambda('lambda_111E')
    def lambda_111E():
        CameraSetDistance(3540, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_111E)

    FadeIn(1000, 0)
    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x00F9, 0x0001)
    OP_0D()

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1177',
    )

    ChrTalk(
        0x0107,
        (
            '#0070281228V#061F嘿嘿，雾终于散了阿⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_125D')

    def _loc_1177(): pass

    label('loc_1177')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11B3',
    )

    ChrTalk(
        0x0106,
        (
            '#0050281218V#051F呼……\n',
            '雾终于散了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_125D')

    def _loc_11B3(): pass

    label('loc_11B3')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11EF',
    )

    ChrTalk(
        0x0104,
        (
            '#0040281219V#030F嗯……\n',
            '雾终于散了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_125D')

    def _loc_11EF(): pass

    label('loc_11EF')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1224',
    )

    ChrTalk(
        0x0105,
        (
            '#0060281231V#048F雾终于散了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_125D')

    def _loc_1224(): pass

    label('loc_1224')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_125D',
    )

    ChrTalk(
        0x0108,
        (
            '#0080281221V#070F嗯……\n',
            '雾终于散了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_125D(): pass

    label('loc_125D')

    ChrTalk(
        0x0103,
        (
            '#0030281213V#026F玛鲁加山道，距离洛连特市\n',
            '大约１４０塞尔矩的地点……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281214V#022F不但浓雾的范围很广，\n',
            '还有魔兽游荡，非常危险。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281194V#1015F#6P嗯，的确。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281195V这样的话，三个地方\n',
            '都调查过了…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010281196V#1006F#5P我们应该回协会\n',
            '向爱娜姐报告了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_140C',
    )

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
        0,
        (
            TXT(0x00, '【◇没去过布莱特家】\n'),
            TXT(0x01, '【◇去过布莱特家】\n'),
            TXT(0x02, '【◇不变更】\n'),
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
        (0x00000000, 'loc_1400'),
        (0x00000001, 'loc_1406'),
        (-1, 'loc_140C'),
    )

    def _loc_1400(): pass

    label('loc_1400')

    ClearScenaFlags(ScenaFlag(0x0301, 5, 0x180D))

    Jump('loc_140C')

    def _loc_1406(): pass

    label('loc_1406')

    SetScenaFlags(ScenaFlag(0x0301, 5, 0x180D))

    Jump('loc_140C')

    def _loc_140C(): pass

    label('loc_140C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 5, 0x180D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_14E2',
    )

    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030281238V#023F那样也好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281198V不过，好像还没\n',
            '回家看看呢吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281199V#1004F#5P啊……都给忘了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281241V#1008F回协会报告之前\n',
            '先回去看一下吧。',
            TxtCtl.Enter,
        ),
    )

    OP_28(0x008F, 0x02, 0x0040)
    OP_28(0x008F, 0x01, 0x0080)
    OP_28(0x008F, 0x01, 0x0800)
    OP_28(0x008F, 0x01, 0x1000)
    CloseMessageWindow()

    Jump('loc_1529')

    def _loc_14E2(): pass

    label('loc_14E2')

    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030281242V#021F哎哎。\n',
            '那样也好。',
            TxtCtl.Enter,
        ),
    )

    OP_28(0x008F, 0x02, 0x0040)
    OP_28(0x008F, 0x01, 0x0080)
    OP_28(0x008F, 0x01, 0x0200)
    OP_28(0x008F, 0x01, 0x0400)
    CloseMessageWindow()

    def _loc_1529(): pass

    label('loc_1529')

    SetScenaFlags(ScenaFlag(0x0302, 0, 0x1810))
    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0x152F
@scena.Code('func_07_152F')
def func_07_152F():
    FadeOut(0, 0, -1)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x09, 0xFF)

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
        0,
        (
            TXT(0x00, '【◇选择雪拉扎德为队友】\n'),
            TXT(0x01, '【◇选择阿加特为队友】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_15AC'),
        (0x00000001, 'loc_15B2'),
        (-1, 'loc_15B8'),
    )

    def _loc_15AC(): pass

    label('loc_15AC')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_15B8')

    def _loc_15B2(): pass

    label('loc_15B2')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_15B8')

    def _loc_15B8(): pass

    label('loc_15B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_15C6',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_15CA')

    def _loc_15C6(): pass

    label('loc_15C6')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_15CA(): pass

    label('loc_15CA')

    Return()

# id: 0x0008 offset: 0x15CB
@scena.Code('func_08_15CB')
def func_08_15CB():
    MapClearFlags(0x00000001)
    CameraMove(106730, -1920, 53920, 0)
    Sleep(100)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['雪拉扎德'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            ChrTable['提妲'],
            ChrTable['金'],
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0)
    Sleep(1000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
