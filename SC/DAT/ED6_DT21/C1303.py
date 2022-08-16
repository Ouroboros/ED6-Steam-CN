import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C1303_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1303   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'C1303.x'
    header.mapIndex       = 52
    header.bgm            = 89
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
        ('ED6_DT07/CH01600._CH', 'ED6_DT07/CH01600P._CP'),
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT27/CH04010._CH', 'ED6_DT27/CH04010P._CP'),
        ('ED6_DT27/CH04011._CH', 'ED6_DT27/CH04011P._CP'),
        ('ED6_DT07/CH00291._CH', 'ED6_DT07/CH00291P._CP'),
        ('ED6_DT07/CH00301._CH', 'ED6_DT07/CH00301P._CP'),
        ('ED6_DT07/CH00311._CH', 'ED6_DT07/CH00311P._CP'),
        ('ED6_DT26/CH20335._CH', 'ED6_DT26/CH20335P._CP'),
        ('ED6_DT06/CH20043._CH', 'ED6_DT06/CH20043P._CP'),
        ('ED6_DT27/CH03014._CH', 'ED6_DT27/CH03014P._CP'),
        ('ED6_DT07/CH00330._CH', 'ED6_DT07/CH00330P._CP'),
        ('ED6_DT07/CH00320._CH', 'ED6_DT07/CH00320P._CP'),
    ]

# id: 0x10001 offset: 0x10A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '守备队长',
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
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
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
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
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
    )

# id: 0x10002 offset: 0x16A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x16A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x16A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -75460,
            triggerZ            = 0,
            triggerY            = -119560,
            triggerRange        = 1000,
            actorX              = -75450,
            actorZ              = 1500,
            actorY              = -118890,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x18E
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0300, 1, 0x1801)),
            Expr.Return,
        ),
        'loc_213',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x0008, -39500, 0, -87480, 0)
    ChrSetPos(0x0009, -41000, 0, -87420, 0)
    ChrSetPos(0x000A, -40800, 0, -89040, 0)
    ChrSetFlags(0x0008, 0x0002)
    ChrSetFlags(0x0009, 0x0002)
    ChrSetFlags(0x000A, 0x0002)
    ChrClearFlags(0x0008, 0x0001)
    ChrClearFlags(0x0009, 0x0001)
    ChrClearFlags(0x000A, 0x0001)
    ChrSetSubChip(0x0008, 1)
    ChrSetChipByIndex(0x0008, 7)
    ChrSetSubChip(0x0009, 4)
    ChrSetChipByIndex(0x0009, 8)
    ChrSetSubChip(0x000A, 7)
    ChrSetChipByIndex(0x000A, 8)

    def _loc_213(): pass

    label('loc_213')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x69),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_22B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0300, 1, 0x1801)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_22B',
    )

    Event(0, func_03_368)

    def _loc_22B(): pass

    label('loc_22B')

    Return()

# id: 0x0001 offset: 0x22C
@scena.Code('func_01_22C')
def func_01_22C():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0320, 0, 0x1900)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_23E',
    )

    OP_6F(0x0002, 0)

    Jump('loc_245')

    def _loc_23E(): pass

    label('loc_23E')

    OP_6F(0x0002, 60)

    def _loc_245(): pass

    label('loc_245')

    OP_10(0x03, 0x00)
    OP_10(0x08, 0x01)

    Return()

# id: 0x0002 offset: 0x24C
@scena.Code('func_02_24C')
def func_02_24C():
    UnlockAchievement(0x02, 0x0047, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0320, 0, 0x1900)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_329',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['攻击３'], 1)"),
            Expr.Return,
        ),
        'loc_2C0',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['攻击３']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0320, 0, 0x1900))

    Jump('loc_326')

    def _loc_2C0(): pass

    label('loc_2C0')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['攻击３']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['攻击３']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0)

    def _loc_326(): pass

    label('loc_326')

    Jump('loc_35A')

    def _loc_329(): pass

    label('loc_329')

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
    def _loc_35A(): pass

    label('loc_35A')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x368
@scena.Code('func_03_368')
def func_03_368():
    EventBegin(0x00)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    CameraMove(-34720, 0, -86660, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2230, 0)
    OP_6C(45000, 0)
    OP_6E(355, 0)
    OP_0D()
    CreateThread(0x0129, 0x01, 0x00, func_05_117F)
    Sleep(700)

    CreateThread(0x012A, 0x01, 0x00, func_07_1266)
    Sleep(500)

    CreateThread(0x0146, 0x01, 0x00, func_06_11EF)
    Sleep(800)

    CreateThread(0x0102, 0x01, 0x00, func_08_12DD)

    @scena.Lambda('lambda_03ED')
    def lambda_03ED():
        CameraMove(-36060, 0, -82580, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_03ED)

    WaitForThreadExit(0x0146, 0x0001)
    WaitForThreadExit(0x0146, 0x0000)

    ChrTalk(
        0x0129,
        (
            '#0300280144V#197F#5P这里是……\n',
            '我们之前用过的房间呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x012A, 0, 400)

    ChrTalk(
        0x012A,
        (
            '#0290280145V#200F#2P哦……\n',
            '装设了通信器啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0146,
        (
            '#0090280146V#210F#6P里面没人……\n',
            '有点太粗心大意了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020280147V#1030F看来这里似乎是\n',
            '守备队长的房间。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020280148V只要埋伏在这里的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020280149V#1035F……回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetSubChip(0x0102, 0)
    ChrSetChipByIndex(0x0102, 2)
    OP_0D()
    Sleep(300)

    ChrSetDirection(0x0102, 180, 600)

    ChrTalk(
        0x0102,
        (
            '#0020280150V#1030F#5P趁他们进来时一次解决。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0146,
        (
            '#0090280151V#213F#6P啊啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_05CC')
    def lambda_05CC():
        ChrSetDirection(0x0146, 180, 400)

        ExitThread()

    DispatchAsync(0x0146, 0x0001, lambda_05CC)

    @scena.Lambda('lambda_05DA')
    def lambda_05DA():
        CameraMove(-34550, 0, -85660, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_05DA)

    @scena.Lambda('lambda_05F2')
    def lambda_05F2():
        ChrSetDirection(0x0129, 180, 400)

        ExitThread()

    DispatchAsync(0x0129, 0x0001, lambda_05F2)

    PlaySE(6, 0x00, 0x64)
    Sleep(300)

    @scena.Lambda('lambda_060A')
    def lambda_060A():
        ChrSetDirection(0x012A, 180, 400)

        ExitThread()

    DispatchAsync(0x012A, 0x0001, lambda_060A)

    Sleep(100)

    CreateThread(0x0008, 0x01, 0x00, func_09_1354)
    Sleep(500)

    CreateThread(0x0009, 0x01, 0x00, func_0A_139C)
    Sleep(500)

    CreateThread(0x000A, 0x01, 0x00, func_0B_13EB)
    WaitForThreadExit(0x0008, 0x0001)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    WaitForThreadExit(0x0009, 0x0001)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    WaitForThreadExit(0x000A, 0x0001)
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#3290280152V#5P什…么…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2450280153V#6P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020280154V#1031F#5P……太慢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0102, 0x1000)
    ChrSetFlags(0x0146, 0x1000)
    ChrSetFlags(0x012A, 0x1000)
    ChrSetFlags(0x0129, 0x1000)
    ChrSetChipByIndex(0x0102, 3)

    @scena.Lambda('lambda_070D')
    def lambda_070D():
        ChrMoveTo(0x00FE, -35180, 0, -88280, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_070D)

    Sleep(100)

    PlaySE(216, 0x00, 0x64)
    ChrSetSubChip(0x0146, 0)
    ChrSetChipByIndex(0x0146, 6)

    @scena.Lambda('lambda_073C')
    def lambda_073C():
        ChrMoveTo(0x00FE, -36080, 0, -87570, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0146, 0x0001, lambda_073C)

    Sleep(100)

    ChrSetSubChip(0x012A, 0)
    ChrSetChipByIndex(0x012A, 5)

    @scena.Lambda('lambda_0766')
    def lambda_0766():
        ChrMoveTo(0x00FE, -35340, 0, -86770, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x012A, 0x0001, lambda_0766)

    Sleep(50)

    ChrSetSubChip(0x0129, 0)
    ChrSetChipByIndex(0x0129, 4)

    @scena.Lambda('lambda_0790')
    def lambda_0790():
        ChrMoveTo(0x00FE, -36100, 0, -86510, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0129, 0x0001, lambda_0790)

    @scena.Lambda('lambda_07AB')
    def lambda_07AB():
        CameraMove(-34680, 0, -87920, 300)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_07AB)

    @scena.Lambda('lambda_07C3')
    def lambda_07C3():
        CameraSetDistance(1960, 300)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_07C3)

    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 10)
    ChrSetSubChip(0x0009, 0)
    ChrSetChipByIndex(0x0009, 11)
    ChrSetSubChip(0x000A, 0)
    ChrSetChipByIndex(0x000A, 11)
    Sleep(300)

    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0146, 0xFF)
    TerminateThread(0x012A, 0xFF)
    TerminateThread(0x0129, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    Battle(0x000000A5, 0x00000000, 0x02, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_825'),
        (-1, 'loc_82A'),
    )

    def _loc_825(): pass

    label('loc_825')

    OP_B4(0x00)

    Jump('loc_82A')

    def _loc_82A(): pass

    label('loc_82A')

    Call(0, 0x0004)

    Return()

# id: 0x0004 offset: 0x82F
@scena.Code('func_04_82F')
def func_04_82F():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_0D()
    ChrClearFlags(0x0102, 0x1000)
    ChrClearFlags(0x0146, 0x1000)
    ChrClearFlags(0x012A, 0x1000)
    ChrClearFlags(0x0129, 0x1000)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x0146, 0x01)
    TerminateThread(0x012A, 0x01)
    TerminateThread(0x0129, 0x01)
    ChrSetPos(0x0102, -38290, 0, -86890, 270)
    ChrSetPos(0x0129, -36820, 0, -86670, 270)
    ChrSetPos(0x0146, -37870, 0, -85820, 225)
    ChrSetPos(0x012A, -37800, 0, -87800, 270)
    ChrSetSubChip(0x0102, 0)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetSubChip(0x0129, 0)
    ChrSetChipByIndex(0x0129, 65535)
    ChrSetSubChip(0x012A, 0)
    ChrSetChipByIndex(0x012A, 65535)
    ChrSetSubChip(0x0146, 0)
    ChrSetChipByIndex(0x0146, 65535)
    ChrSetPos(0x0008, -39500, 0, -87480, 0)
    ChrSetPos(0x0009, -41000, 0, -87420, 0)
    ChrSetPos(0x000A, -40800, 0, -89040, 0)
    ChrSetFlags(0x0008, 0x0002)
    ChrSetFlags(0x0009, 0x0002)
    ChrSetFlags(0x000A, 0x0002)
    ChrClearFlags(0x0008, 0x0001)
    ChrClearFlags(0x0009, 0x0001)
    ChrClearFlags(0x000A, 0x0001)
    ChrSetSubChip(0x0008, 1)
    ChrSetChipByIndex(0x0008, 7)
    ChrSetSubChip(0x0009, 4)
    ChrSetChipByIndex(0x0009, 8)
    ChrSetSubChip(0x000A, 7)
    ChrSetChipByIndex(0x000A, 8)
    CameraMove(-37800, 0, -86880, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(1500, 0)
    OP_0D()
    Sleep(500)

    Fade(500)
    ChrSetSubChip(0x0102, 0)
    ChrSetChipByIndex(0x0102, 9)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020280155V#1035F#6P有了……就是这个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['山猫号启动钥匙'], 1)
    Fade(500)
    ChrSetSubChip(0x0102, 0)
    ChrSetChipByIndex(0x0102, 65535)
    OP_0D()

    @scena.Lambda('lambda_0A15')
    def lambda_0A15():
        CameraMove(-37210, 0, -86660, 1000)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_0A15)

    ChrSetDirection(0x0102, 90, 400)
    ChrSetDirection(0x0146, 180, 400)
    ChrSetDirection(0x012A, 0, 400)
    WaitForThreadExit(0x0102, 0x0000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AE3',
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
            TXT(0x00, '【◇没看见确认空贼艇的事件】\n'),
            TXT(0x01, '【◇看见了确认空贼艇的事件】\n'),
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
        (0x00000000, 'loc_AD7'),
        (0x00000001, 'loc_ADD'),
        (-1, 'loc_AE3'),
    )

    def _loc_AD7(): pass

    label('loc_AD7')

    ClearScenaFlags(ScenaFlag(0x0300, 4, 0x1804))

    Jump('loc_AE3')

    def _loc_ADD(): pass

    label('loc_ADD')

    SetScenaFlags(ScenaFlag(0x0300, 4, 0x1804))

    Jump('loc_AE3')

    def _loc_AE3(): pass

    label('loc_AE3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0300, 4, 0x1804)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B20',
    )

    ChrTalk(
        0x0129,
        (
            '#0300280156V#191F#2P哦哦，这么快就找到了啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B4A')

    def _loc_B20(): pass

    label('loc_B20')

    ChrTalk(
        0x0129,
        (
            '#0300280157V#191F#2P好，终于找到了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B4A(): pass

    label('loc_B4A')

    ChrTalk(
        0x012A,
        (
            '#0290280158V#203F真，真是让人\n',
            '吓出一身冷汗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0146, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1000)

    OP_63(0x0146)

    ChrTalk(
        0x0146,
        (
            '#0090280159V#212F#5P……对了，约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090280160V以前和我们对战的时候，\n',
            '难道你手下留情了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020280161V#1034F#6P？什么意思？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0146,
        (
            '#0090280162V#214F#5P因为你实在\n',
            '强得一塌糊涂啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090280163V说实话，那时候\n',
            '和现在根本不能相提并论啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020280164V#1031F#6P我并没有手下留情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020280165V只是当时『开关』\n',
            '还没打开而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0146,
        (
            '#0090280166V#213F#5P开关？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020280167V#1035F#6P详细说明就免了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020280168V总之这个开关打开的话，\n',
            '我就能将合理的思考和行动\n',
            '发挥到极限。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020280169V只有这点差别而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0146,
        (
            '#0090280170V#215F#5P嗯，嗯～……\n',
            '好像听懂了，又好像没懂。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012A,
        (
            '#0290280171V#200F力量并没有改变……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290280172V只是能将这些力量\n',
            '更加彻底有效地发挥出来，对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020280173V#1031F#6P这么理解也没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0129,
        (
            '#0300280174V#490F#2P哦，真不得了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300280175V现在的你，应该和那特务兵\n',
            '队长也不相上下吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012A,
        (
            '#0290280176V#206F说是『结社』手下\n',
            '的那个洛伦斯少尉吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020280177V#1033F#6P不……这点办不到。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020280178V我的能力是针对隐密活动和\n',
            '对集团作战而特别强化过的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020280179V在一对一的战斗中，\n',
            '是不可能胜过『剑帝』的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0129,
        (
            '#0300280180V#192F#2P『剑帝』……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0146,
        (
            '#0090280181V#213F#5P这是说那个少尉？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020280182V#1035F#6P啊啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020280183V#1032F只要有他在，我绝对\n',
            '不会正面向『结社』挑战。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020280184V正如『漆黑之牙』这名号……\n',
            '只会在黑暗中露出利齿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0146,
        (
            '#0090280185V#216F#5P……啊……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0129,
        (
            '#0300280186V#199F#2P你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012A,
        (
            '#0290280187V#206F怎么说呢……\n',
            '好深奥的话啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020280188V#1033F#6P……尽说了些无聊话。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020280189V#1035F没时间了，赶快走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0300, 1, 0x1801))
    EventEnd(0x00)

    Return()

# id: 0x0005 offset: 0x117F
@scena.Code('func_05_117F')
def func_05_117F():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, -35000, 0, -90980, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_11A6')
    def lambda_11A6():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_11A6)

    ChrWalkTo(0x00FE, -34640, 0, -86660, 3000, 0x00)
    ChrWalkTo(0x00FE, -36330, 0, -84850, 3000, 0x00)
    ChrWalkTo(0x00FE, -36460, 0, -82280, 3000, 0x00)

    Return()

# id: 0x0006 offset: 0x11EF
@scena.Code('func_06_11EF')
def func_06_11EF():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, -35000, 0, -90980, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_1216')
    def lambda_1216():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1216)

    ChrWalkTo(0x00FE, -35220, 0, -87620, 3000, 0x00)
    ChrWalkTo(0x00FE, -37450, 0, -85660, 3000, 0x00)
    ChrWalkTo(0x00FE, -37700, 0, -83480, 3000, 0x00)
    ChrSetDirection(0x00FE, 315, 400)

    Return()

# id: 0x0007 offset: 0x1266
@scena.Code('func_07_1266')
def func_07_1266():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, -35000, 0, -90980, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_128D')
    def lambda_128D():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_128D)

    ChrWalkTo(0x00FE, -34860, 0, -86960, 3000, 0x00)
    ChrWalkTo(0x00FE, -35670, 0, -85500, 3000, 0x00)
    ChrWalkTo(0x00FE, -35670, 0, -83000, 3000, 0x00)
    ChrSetDirection(0x00FE, 45, 400)

    Return()

# id: 0x0008 offset: 0x12DD
@scena.Code('func_08_12DD')
def func_08_12DD():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, -35000, 0, -90980, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_1304')
    def lambda_1304():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1304)

    ChrWalkTo(0x00FE, -34920, 0, -87850, 3000, 0x00)
    ChrWalkTo(0x00FE, -36460, 0, -85890, 3000, 0x00)
    ChrWalkTo(0x00FE, -36510, 0, -84440, 3000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0009 offset: 0x1354
@scena.Code('func_09_1354')
def func_09_1354():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, -35000, 0, -90980, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_137B')
    def lambda_137B():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_137B)

    ChrWalkTo(0x00FE, -34900, 0, -88540, 3000, 0x00)

    Return()

# id: 0x000A offset: 0x139C
@scena.Code('func_0A_139C')
def func_0A_139C():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, -35000, 0, -90980, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_13C3')
    def lambda_13C3():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_13C3)

    ChrWalkTo(0x00FE, -35690, 0, -89640, 3000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x000B offset: 0x13EB
@scena.Code('func_0B_13EB')
def func_0B_13EB():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, -35000, 0, -90980, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_1412')
    def lambda_1412():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1412)

    ChrWalkTo(0x00FE, -34370, 0, -89640, 3000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
