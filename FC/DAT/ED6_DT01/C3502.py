import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C3502_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C3502   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'C3502.x'
    header.mapIndex       = 1
    header.bgm            = 33
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
        ('ED6_DT07/CH01610._CH', 'ED6_DT07/CH01610P._CP'),
        ('ED6_DT07/CH00440._CH', 'ED6_DT07/CH00440P._CP'),
        ('ED6_DT07/CH00441._CH', 'ED6_DT07/CH00441P._CP'),
        ('ED6_DT07/CH00444._CH', 'ED6_DT07/CH00444P._CP'),
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00101._CH', 'ED6_DT07/CH00101P._CP'),
        ('ED6_DT07/CH00112._CH', 'ED6_DT07/CH00112P._CP'),
        ('ED6_DT07/CH00111._CH', 'ED6_DT07/CH00111P._CP'),
        ('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP'),
        ('ED6_DT07/CH00151._CH', 'ED6_DT07/CH00151P._CP'),
        ('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP'),
        ('ED6_DT07/CH00161._CH', 'ED6_DT07/CH00161P._CP'),
        ('ED6_DT06/CH20110._CH', 'ED6_DT06/CH20110P._CP'),
        ('ED6_DT06/CH20111._CH', 'ED6_DT06/CH20111P._CP'),
        ('ED6_DT06/CH20104._CH', 'ED6_DT06/CH20104P._CP'),
        ('ED6_DT07/CH01330._CH', 'ED6_DT07/CH01330P._CP'),
        ('ED6_DT07/CH00442._CH', 'ED6_DT07/CH00442P._CP'),
        ('ED6_DT07/CH00162._CH', 'ED6_DT07/CH00162P._CP'),
        ('ED6_DT07/CH00050._CH', 'ED6_DT07/CH00050P._CP'),
        ('ED6_DT07/CH00051._CH', 'ED6_DT07/CH00051P._CP'),
        ('ED6_DT07/CH00055._CH', 'ED6_DT07/CH00055P._CP'),
        ('ED6_DT07/CH00164._CH', 'ED6_DT07/CH00164P._CP'),
        ('ED6_DT07/CH00340._CH', 'ED6_DT07/CH00340P._CP'),
        ('ED6_DT07/CH00341._CH', 'ED6_DT07/CH00341P._CP'),
        ('ED6_DT07/CH00344._CH', 'ED6_DT07/CH00344P._CP'),
    ]

# id: 0x10001 offset: 0x172
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '黑衣男子',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '黑衣男子',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '黑衣男子',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '拉赛尔博士',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务艇',
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
            name                = ' ',
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
            name                = '黑衣男子',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x252
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x252
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x252
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x252
@scena.Code('Init')
def Init():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_25E'),
        (-1, 'loc_274'),
    )

    def _loc_25E(): pass

    label('loc_25E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 2, 0x53A)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 1, 0x539)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_271',
    )

    SetScenaFlags(ScenaFlag(0x00A7, 2, 0x53A))
    Event(0, func_02_2BA)

    def _loc_271(): pass

    label('loc_271')

    Jump('loc_274')

    def _loc_274(): pass

    label('loc_274')

    Return()

# id: 0x0001 offset: 0x275
@scena.Code('func_01_275')
def func_01_275():
    OP_71(0x0004, 0x0004)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 2, 0x53A)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 0, 0x558)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_29F',
    )

    OP_71(0x0005, 0x0004)
    OP_7A(0x00, 0x0002)
    OP_7A(0x01, 0x0002)
    OP_7A(0x02, 0x0002)
    OP_7A(0x03, 0x0002)
    OP_7B()

    Jump('loc_2B4')

    def _loc_29F(): pass

    label('loc_29F')

    OP_78(0xFF, 0xFF, 0xFF)
    OP_79(0x00, 0x0002)
    OP_79(0x01, 0x0002)
    OP_79(0x02, 0x0002)
    OP_79(0x03, 0x0002)
    OP_7B()

    def _loc_2B4(): pass

    label('loc_2B4')

    PlaySE(451, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x2BA
@scena.Code('func_02_2BA')
def func_02_2BA():
    EventBegin(0x00)
    CameraMove(940, 250, 31840, 0)
    CameraSetDistance(5000, 0)
    ChrSetPos(0x0106, 300, 0, -2410, 50)
    ChrSetPos(0x0101, 1330, 0, -2710, 50)
    ChrSetPos(0x0102, 60, 0, -3500, 50)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x0008, 11190, 250, 4260, 96)
    ChrSetPos(0x0009, 11310, 250, 5950, 96)
    ChrSetPos(0x000A, 12710, 250, 4560, 96)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 13330, 250, 4520, 180)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_0370')
    def lambda_0370():
        CameraMove(7980, 250, 1980, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0370)

    WaitForThreadExit(0x0101, 0x0002)
    OP_0D()
    Fade(500)
    CameraSetDistance(3000, 0)
    CameraMove(3350, 250, -480, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010081159V#005F找到了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050081160V#051F哼……\n',
            '总算被我们追到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_03FD')
    def lambda_03FD():
        OP_67(0, 4700, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_03FD)

    @scena.Lambda('lambda_0415')
    def lambda_0415():
        CameraMove(9830, 250, 2770, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0415)

    @scena.Lambda('lambda_042D')
    def lambda_042D():
        CameraSetDistance(3700, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_042D)

    ChrSetChipByIndex(0x0101, 4)

    @scena.Lambda('lambda_0442')
    def lambda_0442():
        ChrWalkTo(0x00FE, 7230, 250, -390, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0442)

    Sleep(200)

    ChrSetChipByIndex(0x0106, 8)

    @scena.Lambda('lambda_0467')
    def lambda_0467():
        ChrWalkTo(0x00FE, 6190, 250, 590, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_0467)

    Sleep(200)

    ChrSetChipByIndex(0x0102, 6)

    @scena.Lambda('lambda_048C')
    def lambda_048C():
        ChrWalkTo(0x00FE, 5920, 250, -660, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_048C)

    Sleep(500)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(500)

    @scena.Lambda('lambda_04F6')
    def lambda_04F6():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_04F6)

    @scena.Lambda('lambda_0504')
    def lambda_0504():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0504)

    @scena.Lambda('lambda_0512')
    def lambda_0512():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0512)

    WaitForThreadExit(0x0101, 0x0001)
    ChrTurnDirection(0x0101, 0x0008, 400)
    WaitForThreadExit(0x0106, 0x0001)
    ChrTurnDirection(0x0106, 0x0008, 400)
    WaitForThreadExit(0x0102, 0x0001)
    ChrTurnDirection(0x0102, 0x0008, 400)
    ChrSetSubChip(0x0102, 11)
    WaitForThreadExit(0x0101, 0x0003)
    ChrMoveTo(0x0008, 11670, 250, 4710, 2000, 0x00)
    ChrSetChipByIndex(0x0008, 22)
    Sleep(300)

    ChrSetChipByIndex(0x0009, 22)
    ChrSetChipByIndex(0x000A, 1)

    ChrTalk(
        0x0008,
        (
            '#2620081161V啊……！\n',
            '那帮游击士！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2630081162V真是缠人的家伙。\n',
            '竟追到这里来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081163V#006F你们竟然想到换装逃出城镇，\n',
            '的确也很有一套嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010081164V但是你们最终还是难逃法网。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020081165V#012F你们以为谁都不会来这个遗迹，\n',
            '看来好运再好也会到头的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020081166V请你们还是赶快放下武器投降，\n',
            '然后马上放了拉赛尔博士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620081167V呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050081168V#057F现基于游击士协会规定，\n',
            '我要将你们逮捕并拘留归案。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050081169V虽然不能马上抓到\n',
            '那个装模作样的蒙面混蛋……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050081170V算了，就先拿你们充数好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620081171V口、口出狂言！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2630081172V碍事的家伙就要消灭！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0008, 23)

    @scena.Lambda('lambda_07DB')
    def lambda_07DB():
        ChrMoveToRelative(0x00FE, -3000, 0, -3000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_07DB)

    Sleep(50)

    ChrSetChipByIndex(0x000A, 2)

    @scena.Lambda('lambda_0800')
    def lambda_0800():
        ChrMoveToRelative(0x00FE, -3000, 0, -3000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0800)

    Sleep(50)

    ChrSetChipByIndex(0x0009, 23)

    @scena.Lambda('lambda_0825')
    def lambda_0825():
        ChrMoveToRelative(0x00FE, -3000, 0, -3000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0825)

    @scena.Lambda('lambda_0840')
    def lambda_0840():
        ChrMoveToRelative(0x00FE, 3000, 0, 3000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0840)

    Sleep(50)

    @scena.Lambda('lambda_0860')
    def lambda_0860():
        ChrMoveToRelative(0x00FE, 3000, 0, 3000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_0860)

    Sleep(50)

    @scena.Lambda('lambda_0880')
    def lambda_0880():
        ChrMoveToRelative(0x00FE, 3000, 0, 3000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0880)

    Sleep(200)

    Battle(0x000003A0, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_8B3'),
        (-1, 'loc_8B6'),
    )

    def _loc_8B3(): pass

    label('loc_8B3')

    OP_B4(0x00)

    Return()

    def _loc_8B6(): pass

    label('loc_8B6')

    EventBegin(0x00)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0106, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    CameraMove(11880, 250, 6260, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(3700, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FormationAddMember(0x06, 0xFF)
    ChrSetPos(0x0101, 8730, 250, 6030, 108)
    ChrSetPos(0x0106, 8240, 250, 3640, 87)
    ChrSetPos(0x0102, 7230, 250, 4750, 101)
    ChrSetPos(0x0107, 2860, 250, -2970, 58)
    ChrSetChipByIndex(0x0101, 4)
    ChrSetChipByIndex(0x0102, 6)
    ChrSetSubChip(0x0102, 11)
    ChrSetChipByIndex(0x0106, 8)
    ChrSetChipByIndex(0x0107, 10)

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0008, 24)
    ChrSetChipByIndex(0x0009, 3)
    ChrSetChipByIndex(0x000A, 24)
    ChrSetPos(0x0008, 12260, 250, 4130, 268)
    ChrSetPos(0x0009, 12650, 250, 2620, 288)
    ChrSetPos(0x000A, 13120, 250, 5220, 280)
    ChrSetPos(0x000B, 14750, 250, 2210, 280)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#2620081173V#2P呜……\n',
            '不愧是游击士……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2630081174V#2P不过……\n',
            '别忘了我们手上有人质！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0A51')
    def lambda_0A51():
        OP_99(0x00FE, 0x03, 0x00, 800)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0A51)

    @scena.Lambda('lambda_0A61')
    def lambda_0A61():
        OP_99(0x00FE, 0x03, 0x00, 1000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0A61)

    @scena.Lambda('lambda_0A71')
    def lambda_0A71():
        OP_99(0x00FE, 0x03, 0x00, 700)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0A71)

    WaitForThreadExit(0x0009, 0x0001)
    ChrSetChipByIndex(0x0009, 1)
    ChrJumpTo(0x0009, 14400, 250, 2770, 500, 5000)
    PlaySE(164, 0x00, 0x64)

    @scena.Lambda('lambda_0AA7')
    def lambda_0AA7():
        CameraMove(12670, 250, 5070, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0AA7)

    WaitForThreadExit(0x000A, 0x0001)
    ChrSetChipByIndex(0x000A, 22)

    @scena.Lambda('lambda_0AC9')
    def lambda_0AC9():
        ChrMoveTo(0x00FE, 14590, 250, 4730, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0AC9)

    Sleep(200)

    WaitForThreadExit(0x0008, 0x0001)
    ChrSetChipByIndex(0x0008, 22)

    @scena.Lambda('lambda_0AF3')
    def lambda_0AF3():
        ChrMoveTo(0x00FE, 13520, 250, 3650, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0AF3)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010081175V#005F你们这些家伙！\n',
            '还要做垂死挣扎吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020081176V#012F你们的目的是\n',
            '拉赛尔博士的智慧吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020081177V你们真的敢加害于他吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620081178V#2P少、少啰嗦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2630081179V#2P以为我们不敢伤害他的话，\n',
            '你们大可以试试啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050081180V#054F烦死了……\n',
            '你们闹够没有，投降吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050081181V王国军也要出动了，\n',
            '你们这些家伙已经无处可逃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620081182V#2P……呵呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2630081183V#2P哈哈哈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050081184V#057F……有什么好笑的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620081185V#2P不，没什么。\n',
            '只是觉得你们还真是单纯得可爱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620081186V#2P那么……时间差不多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(121, 0x01, 0x64)
    OP_24(0x0079, 0x46)

    ChrTalk(
        0x0106,
        (
            '#0050081187V#057F什……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050081188V#052F……………什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x000C, 22050, -10000, -11170, 305)
    OP_24(0x0079, 0x50)

    @scena.Lambda('lambda_0DB5')
    def lambda_0DB5():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_0DB5')

    DispatchAsync2(0x0101, 0x0000, lambda_0DB5)

    @scena.Lambda('lambda_0DC6')
    def lambda_0DC6():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_0DC6')

    DispatchAsync2(0x0102, 0x0000, lambda_0DC6)

    @scena.Lambda('lambda_0DD7')
    def lambda_0DD7():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_0DD7')

    DispatchAsync2(0x0106, 0x0000, lambda_0DD7)

    ChrTalk(
        0x0102,
        (
            '#0020081189V#016F艾丝蒂尔，危险！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_72(0x0004, 0x0004)
    ChrSetFlags(0x000C, 0x0040)
    ChrSetFlags(0x000C, 0x0004)
    OP_A1(0x000C, 0x0004)
    OP_B0(0x0004, 0x1E)
    OP_6F(0x0004, 975)

    @scena.Lambda('lambda_0E2E')
    def lambda_0E2E():
        CameraMove(15860, 250, 4980, 5300)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0E2E)

    ChrTalk(
        0x0101,
        (
            '#0010081190V#005F#10A我知道！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    LoadEffect(0x00, 'map\\\\mp003_00.eff')
    OP_24(0x0079, 0x64)
    Yield()
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000E, 0x0004)
    ChrSetBattleFlags(0x000E, 0x0020)
    OP_89(0x000E, 19530, 1810, -9400, 270)

    @scena.Lambda('lambda_0EA2')
    def lambda_0EA2():
        ChrMoveTo(0x00FE, 23110, 250, 1830, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0EA2)

    Sleep(200)

    @scena.Lambda('lambda_0EC2')
    def lambda_0EC2():
        ChrSetDirection(0x00FE, 0, 20)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_0EC2)

    @scena.Lambda('lambda_0ED0')
    def lambda_0ED0():
        ChrMoveTo(0x00FE, 23110, -3000, 1830, 4800, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0ED0)

    Sleep(200)

    @scena.Lambda('lambda_0EF0')
    def lambda_0EF0():
        ChrSetDirection(0x00FE, 0, 19)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_0EF0)

    @scena.Lambda('lambda_0EFE')
    def lambda_0EFE():
        ChrMoveTo(0x00FE, 23110, -3000, 1830, 4800, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0EFE)

    Sleep(200)

    @scena.Lambda('lambda_0F1E')
    def lambda_0F1E():
        ChrSetDirection(0x00FE, 0, 18)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_0F1E)

    @scena.Lambda('lambda_0F2C')
    def lambda_0F2C():
        ChrMoveTo(0x00FE, 23110, -3000, 1830, 4500, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0F2C)

    Sleep(500)

    @scena.Lambda('lambda_0F4C')
    def lambda_0F4C():
        OP_6E(350, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0F4C)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x00FF, 12230, 1000, 1240, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x00FF, 10470, 1000, 1770, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x00FF, 10180, 1000, 3370, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_1014')
    def lambda_1014():
        ChrJumpTo(0x00FE, 7000, 250, 6330, 800, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1014)

    Sleep(100)

    @scena.Lambda('lambda_1037')
    def lambda_1037():
        ChrJumpTo(0x00FE, 5140, 250, 4910, 500, 8000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_1037)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x00FF, 8600, 1000, 3960, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    @scena.Lambda('lambda_1094')
    def lambda_1094():
        ChrJumpTo(0x00FE, 6160, 250, 2800, 700, 8000)

        ExitThread()

    DispatchAsync(0x0106, 0x0003, lambda_1094)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x00FF, 7510, 1000, 4890, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x00FF, 8610, 1000, 4900, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x00FF, 8850, 1000, 4220, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x00FF, 7510, 1000, 4890, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(200)

    Sleep(100)

    @scena.Lambda('lambda_11B3')
    def lambda_11B3():
        ChrSetDirection(0x00FE, 0, 12)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_11B3)

    @scena.Lambda('lambda_11C1')
    def lambda_11C1():
        ChrMoveTo(0x00FE, 23110, -3000, 1830, 4200, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_11C1)

    Sleep(100)

    OP_70(0x0004, 1000)
    Sleep(100)

    @scena.Lambda('lambda_11ED')
    def lambda_11ED():
        ChrSetDirection(0x00FE, 0, 11)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_11ED)

    @scena.Lambda('lambda_11FB')
    def lambda_11FB():
        ChrMoveTo(0x00FE, 23110, -3000, 1830, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_11FB)

    Sleep(100)

    @scena.Lambda('lambda_121B')
    def lambda_121B():
        ChrSetDirection(0x00FE, 0, 10)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_121B)

    @scena.Lambda('lambda_1229')
    def lambda_1229():
        ChrMoveTo(0x00FE, 23110, -3000, 1830, 3500, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1229)

    Sleep(200)

    @scena.Lambda('lambda_1249')
    def lambda_1249():
        ChrSetDirection(0x00FE, 355, 9)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_1249)

    @scena.Lambda('lambda_1257')
    def lambda_1257():
        ChrMoveTo(0x00FE, 23110, -3000, 1830, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1257)

    Sleep(200)

    @scena.Lambda('lambda_1277')
    def lambda_1277():
        ChrSetDirection(0x00FE, 355, 8)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_1277)

    @scena.Lambda('lambda_1285')
    def lambda_1285():
        ChrMoveTo(0x00FE, 23110, -3000, 1830, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1285)

    Sleep(200)

    @scena.Lambda('lambda_12A5')
    def lambda_12A5():
        ChrSetDirection(0x00FE, 355, 6)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_12A5)

    @scena.Lambda('lambda_12B3')
    def lambda_12B3():
        ChrMoveTo(0x00FE, 23110, -3000, 1830, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_12B3)

    Sleep(200)

    @scena.Lambda('lambda_12D3')
    def lambda_12D3():
        ChrSetDirection(0x00FE, 355, 4)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_12D3)

    @scena.Lambda('lambda_12E1')
    def lambda_12E1():
        ChrMoveTo(0x00FE, 23110, -3000, 1830, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_12E1)

    Sleep(200)

    @scena.Lambda('lambda_1301')
    def lambda_1301():
        ChrSetDirection(0x00FE, 355, 3)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_1301)

    @scena.Lambda('lambda_130F')
    def lambda_130F():
        ChrMoveTo(0x00FE, 23110, -3000, 1830, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_130F)

    Sleep(200)

    @scena.Lambda('lambda_132F')
    def lambda_132F():
        ChrSetDirection(0x00FE, 355, 2)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_132F)

    @scena.Lambda('lambda_133D')
    def lambda_133D():
        ChrMoveTo(0x00FE, 23110, -3000, 1830, 500, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_133D)

    OP_71(0x0004, 0x0020)
    OP_6F(0x0004, 830)
    OP_70(0x0004, 850)

    ChrTalk(
        0x0101,
        (
            '#0010081191V#005F#5P果然，是飞艇吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050081192V#054F#5P可恶，\n',
            '居然有如此先进的飞行工具！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_13D2')
    def lambda_13D2():
        ChrMoveTo(0x00FE, 19830, -3500, 7300, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_13D2)

    @scena.Lambda('lambda_13ED')
    def lambda_13ED():
        ChrSetDirection(0x00FE, 5, 2)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_13ED)

    Sleep(300)

    @scena.Lambda('lambda_1400')
    def lambda_1400():
        CameraMove(10930, 650, 4120, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1400)

    @scena.Lambda('lambda_1418')
    def lambda_1418():
        OP_6E(292, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1418)

    @scena.Lambda('lambda_1428')
    def lambda_1428():
        ChrSetDirection(0x00FE, 5, 3)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_1428)

    @scena.Lambda('lambda_1436')
    def lambda_1436():
        ChrMoveTo(0x00FE, 19830, -3500, 7300, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1436)

    Sleep(300)

    @scena.Lambda('lambda_1456')
    def lambda_1456():
        ChrSetDirection(0x00FE, 5, 5)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_1456)

    @scena.Lambda('lambda_1464')
    def lambda_1464():
        ChrMoveTo(0x00FE, 19830, -3500, 7300, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1464)

    Sleep(1000)

    @scena.Lambda('lambda_1484')
    def lambda_1484():
        ChrSetDirection(0x00FE, 5, 4)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_1484)

    @scena.Lambda('lambda_1492')
    def lambda_1492():
        ChrMoveTo(0x00FE, 19830, -3500, 7300, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1492)

    Sleep(400)

    @scena.Lambda('lambda_14B2')
    def lambda_14B2():
        ChrSetDirection(0x00FE, 5, 3)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_14B2)

    @scena.Lambda('lambda_14C0')
    def lambda_14C0():
        ChrMoveTo(0x00FE, 19830, -3500, 7300, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_14C0)

    Sleep(400)

    @scena.Lambda('lambda_14E0')
    def lambda_14E0():
        ChrSetDirection(0x00FE, 5, 2)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_14E0)

    @scena.Lambda('lambda_14EE')
    def lambda_14EE():
        ChrMoveTo(0x00FE, 19830, -3500, 7300, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_14EE)

    Sleep(300)

    @scena.Lambda('lambda_150E')
    def lambda_150E():
        ChrSetDirection(0x00FE, 5, 1)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_150E)

    @scena.Lambda('lambda_151C')
    def lambda_151C():
        ChrMoveTo(0x00FE, 19830, -3500, 7300, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_151C)

    Sleep(200)

    @scena.Lambda('lambda_153C')
    def lambda_153C():
        ChrMoveTo(0x00FE, 19830, -3500, 7300, 500, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_153C)

    WaitForThreadExit(0x000C, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#2620081193V呵呵……形势逆转了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2630081194V虽然可以在这里把你们杀光……\n',
            '但我们还不打算和游击士协会作对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620081195V劝你们呆在一边乖乖看着，\n',
            '也许还能保住自己的小命。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081196V#005F可、可恶～！\n',
            '明明是手下败将还敢说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020081197V#012F（艾丝蒂尔……\n',
            '我们就按他们说的做。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081198V#004F（哎……！？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050081199V#057F（先假装顺从，然后伺机……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050081200V（趁他们把老爷子运进去的瞬间，\n',
            '我们抓住时机一口气冲过去。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081201V#002F（明、明白……！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620081202V……看来你们放弃了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2630081203V呵呵……\n',
            '这才是明智的选择嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620081204V那么，我们就告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_17D3')
    def lambda_17D3():
        CameraMove(13430, 650, 4770, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_17D3)

    ChrSetFlags(0x0008, 0x0004)
    ChrSetFlags(0x0009, 0x0004)
    ChrSetFlags(0x000A, 0x0004)
    ChrSetChipByIndex(0x000A, 15)
    Sleep(250)

    ChrJumpTo(0x000A, 15670, 1100, 4880, 1300, 5000)
    PlaySE(164, 0x00, 0x64)
    ChrJumpTo(0x000A, 17180, -120, 4710, 500, 5000)
    PlaySE(164, 0x00, 0x64)
    ChrClearFlags(0x000A, 0x0004)
    ChrSetBattleFlags(0x000A, 0x0020)
    OP_89(0x000A, 17180, 1000, 4710, 270)
    ChrMoveTo(0x000A, 18650, -150, 5150, 2000, 0x00)
    ChrSetChipByIndex(0x0008, 15)
    Sleep(250)

    ChrMoveTo(0x0008, 14720, 250, 3800, 2000, 0x00)
    Sleep(100)

    ChrJumpTo(0x0008, 15660, 1100, 4070, 1300, 5000)
    PlaySE(164, 0x00, 0x64)
    ChrJumpTo(0x0008, 16830, -150, 3710, 500, 5000)
    PlaySE(164, 0x00, 0x64)
    ChrClearFlags(0x0008, 0x0004)
    ChrSetBattleFlags(0x0008, 0x0020)
    OP_89(0x0008, 16830, 1000, 3710, 270)
    ChrMoveTo(0x0008, 19200, -130, 3740, 1500, 0x00)
    Sleep(500)

    ChrSetChipByIndex(0x0009, 15)
    Sleep(500)

    ChrTurnDirection(0x0009, 0x000B, 400)
    TerminateThread(0x0106, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0101, 0xFF)
    LoadEffect(0x02, 'map\\\\mp019_00.eff')

    ChrTalk(
        0x0106,
        (
            '#0050081205V#057F（就是现在……！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1954')
    def lambda_1954():
        CameraMove(15200, 250, 4740, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1954)

    ChrSetPos(0x0107, 4970, 250, -4350, 45)

    NpcTalk(
        0x0107,
        '小女孩的声音',
        (
            '#0070081206V#18A#2P#3S住、住手～！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    @scena.Lambda('lambda_19B2')
    def lambda_19B2():
        ChrWalkTo(0x00FE, 27140, 250, -840, 4100, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_19B2)

    Sleep(50)

    @scena.Lambda('lambda_19D2')
    def lambda_19D2():
        ChrWalkTo(0x00FE, 27140, 250, -840, 4100, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_19D2)

    Sleep(50)

    @scena.Lambda('lambda_19F2')
    def lambda_19F2():
        ChrWalkTo(0x00FE, 27140, 250, -840, 4100, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_19F2)

    ChrSetPos(0x000D, 17450, 1200, 7800, 0)
    PlaySE(506, 0x00, 0x64)
    PlayEffect(0x02, 0xFF, 0x0107, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x000D, 0, 0, 0, 0)
    Sleep(620)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrSetChipByIndex(0x0009, 0)

    @scena.Lambda('lambda_1AA7')
    def lambda_1AA7():
        ChrTurnDirection(0x00FE, 0x0107, 600)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1AA7)

    @scena.Lambda('lambda_1AB5')
    def lambda_1AB5():
        ChrTurnDirection(0x00FE, 0x0107, 600)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1AB5)

    @scena.Lambda('lambda_1AC3')
    def lambda_1AC3():
        ChrTurnDirection(0x00FE, 0x0107, 600)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1AC3)

    @scena.Lambda('lambda_1AD1')
    def lambda_1AD1():
        OP_94(0x00, 0x00FE, 0x0000, 0x00000190, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_1AD1)

    OP_62(0x0106, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(100)

    @scena.Lambda('lambda_1B03')
    def lambda_1B03():
        OP_94(0x00, 0x00FE, 0x0000, 0x00000190, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1B03)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    @scena.Lambda('lambda_1B35')
    def lambda_1B35():
        OP_94(0x00, 0x00FE, 0x0000, 0x00000190, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1B35)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0106,
        (
            '#0050081207V#052F什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1B86')
    def lambda_1B86():
        CameraMove(12830, 250, 2990, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1B86)

    @scena.Lambda('lambda_1B9E')
    def lambda_1B9E():
        OP_6E(270, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1B9E)

    @scena.Lambda('lambda_1BAE')
    def lambda_1BAE():
        ChrTurnDirection(0x00FE, 0x0107, 600)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_1BAE)

    Sleep(50)

    @scena.Lambda('lambda_1BC1')
    def lambda_1BC1():
        ChrTurnDirection(0x00FE, 0x0107, 600)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1BC1)

    Sleep(50)

    @scena.Lambda('lambda_1BD4')
    def lambda_1BD4():
        ChrTurnDirection(0x00FE, 0x0107, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1BD4)

    Sleep(500)

    @scena.Lambda('lambda_1BE7')
    def lambda_1BE7():
        ChrTurnDirection(0x00FE, 0x0107, 0)
        Yield()

        Jump('lambda_1BE7')

    DispatchAsync2(0x0101, 0x0000, lambda_1BE7)

    @scena.Lambda('lambda_1BF8')
    def lambda_1BF8():
        ChrTurnDirection(0x00FE, 0x0107, 0)
        Yield()

        Jump('lambda_1BF8')

    DispatchAsync2(0x0102, 0x0000, lambda_1BF8)

    @scena.Lambda('lambda_1C09')
    def lambda_1C09():
        ChrTurnDirection(0x00FE, 0x0107, 0)
        Yield()

        Jump('lambda_1C09')

    DispatchAsync2(0x0106, 0x0000, lambda_1C09)

    @scena.Lambda('lambda_1C1A')
    def lambda_1C1A():
        ChrWalkTo(0x00FE, 8580, 250, -2130, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_1C1A)

    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#2620081208V小、小女孩！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081209V#004F#1P提妲！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020081210V#016F#1P糟了！\n',
            '她竟然跟了过来！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0107, 17)

    ChrTalk(
        0x0107,
        (
            '#0070081211V#068F还、还我爷爷！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070081212V不还的话……\n',
            '我、我、我就要开炮了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x000D, 17450, 1200, 7800, 0)
    PlaySE(506, 0x00, 0x64)
    PlayEffect(0x02, 0xFF, 0x0107, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x000D, 0, 0, 0, 0)
    OP_99(0x0107, 0x00, 0x0B, 2000)

    ChrTalk(
        0x0008,
        (
            '#2620081213V呜哇……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2630081214V臭、臭小鬼！\n',
            '不要太得意忘形了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1DA9')
    def lambda_1DA9():
        CameraMove(11750, 250, 1440, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1DA9)

    @scena.Lambda('lambda_1DC1')
    def lambda_1DC1():
        OP_6E(242, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1DC1)

    PlaySE(216, 0x00, 0x64)
    ChrSetChipByIndex(0x0009, 16)
    TerminateThread(0x0106, 0x00)
    TerminateThread(0x0102, 0x00)
    TerminateThread(0x0101, 0x00)

    @scena.Lambda('lambda_1DE7')
    def lambda_1DE7():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1DE7)

    @scena.Lambda('lambda_1DF5')
    def lambda_1DF5():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1DF5)

    @scena.Lambda('lambda_1E03')
    def lambda_1E03():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_1E03)

    WaitForThreadExit(0x0101, 0x0002)
    LoadEffect(0x00, 'map\\\\mp008_00.eff')
    Sleep(500)

    ChrTalk(
        0x0107,
        (
            '#0070081215V#065F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020081216V#016F#1P糟了……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081217V#005F提妲！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1E8D')
    def lambda_1E8D():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_1E8D)

    ChrTalk(
        0x0106,
        (
            '#0050081218V#550F……嘁！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0106, 18)

    @scena.Lambda('lambda_1EBF')
    def lambda_1EBF():
        CameraMove(9360, 250, -2160, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1EBF)

    @scena.Lambda('lambda_1ED7')
    def lambda_1ED7():
        OP_6C(40000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1ED7)

    ChrSetFlags(0x0106, 0x1000)
    ChrSetChipByIndex(0x0106, 19)

    @scena.Lambda('lambda_1EF1')
    def lambda_1EF1():
        ChrWalkTo(0x00FE, 8060, 250, -640, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_1EF1)

    Sleep(200)

    @scena.Lambda('lambda_1F11')
    def lambda_1F11():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1F11)

    @scena.Lambda('lambda_1F1F')
    def lambda_1F1F():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1F1F)

    WaitForThreadExit(0x0106, 0x0001)

    @scena.Lambda('lambda_1F32')
    def lambda_1F32():
        OP_92(0x00FE, 0x0107, 500, 8000, 0x01)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_1F32)

    ChrSetPos(0x000D, 8580, 1000, -2130, 0)
    PlayEffect(0x00, 0xFF, 0x0009, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0x000D, 0, 0, 0, 0)

    @scena.Lambda('lambda_1F8D')
    def lambda_1F8D():
        OP_99(0x00FE, 0x00, 0x07, 2000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1F8D)

    WaitForThreadExit(0x0106, 0x0001)
    ChrSetFlags(0x0107, 0x1000)
    ChrSetFlags(0x0107, 0x0020)

    ExecExpressionWithValue(
        0x0107,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0107, 21)
    ChrTurnDirection(0x0107, 0x0106, 0)

    @scena.Lambda('lambda_1FC3')
    def lambda_1FC3():
        OP_99(0x00FE, 0x00, 0x03, 1500)

        ExitThread()

    DispatchAsync(0x0107, 0x0002, lambda_1FC3)

    @scena.Lambda('lambda_1FD3')
    def lambda_1FD3():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_1FD3)

    WaitForThreadExit(0x0106, 0x0001)
    ChrSetDirection(0x0106, 180, 0)
    ChrSetFlags(0x0106, 0x0020)

    ExecExpressionWithValue(
        0x0106,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0106, 20)

    @scena.Lambda('lambda_200A')
    def lambda_200A():
        ChrJumpTo(0x00FE, 7970, 250, -2730, 600, 6000)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_200A)

    OP_94(0x01, 0x0107, 0x00B4, 0x00000320, 0x00001F40, 0x00)
    OP_94(0x01, 0x0107, 0x00B4, 0x00000258, 0x00001770, 0x00)
    PlaySE(555, 0x00, 0x64)
    OP_94(0x01, 0x0107, 0x00B4, 0x00000190, 0x00001194, 0x00)
    OP_94(0x01, 0x0107, 0x00B4, 0x000000C8, 0x00000BB8, 0x00)
    OP_94(0x01, 0x0107, 0x00B4, 0x00000064, 0x000005DC, 0x00)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0106,
        (
            '#0050081219V#056F呜……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081220V#005F#4P阿加特！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020081221V#012F阿加特兄！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0106, 0x1000)

    @scena.Lambda('lambda_20E6')
    def lambda_20E6():
        CameraSetDistance(3500, 1200)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_20E6)

    @scena.Lambda('lambda_20F6')
    def lambda_20F6():
        CameraMove(12340, 250, 2410, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_20F6)

    @scena.Lambda('lambda_210E')
    def lambda_210E():
        OP_6E(312, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_210E)

    ChrTurnDirection(0x0008, 0x0009, 400)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0008,
        (
            '#2620081222V喂、喂！\n',
            '你怎能对着小孩射击！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620081223V而且那是测试用的……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2630081224V#1P抱、抱歉……\n',
            '我怕飞艇会被她射下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620081225V算了，还是赶快撤退吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0009, 0)
    ChrSetFlags(0x0009, 0x0004)
    ChrSetFlags(0x000B, 0x0004)
    ChrTurnDirection(0x0009, 0x000B, 800)
    ChrTurnDirection(0x000B, 0x0009, 800)

    @scena.Lambda('lambda_21FE')
    def lambda_21FE():
        ChrJumpTo(0x00FE, 17270, -120, 3140, 1300, 5000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_21FE)

    @scena.Lambda('lambda_221C')
    def lambda_221C():
        ChrJumpTo(0x00FE, 17360, -140, 2550, 1300, 5000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_221C)

    @scena.Lambda('lambda_223A')
    def lambda_223A():
        CameraMove(12820, 250, 1370, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_223A)

    WaitForThreadExit(0x0009, 0x0001)
    WaitForThreadExit(0x000B, 0x0001)
    ChrClearFlags(0x0009, 0x0004)
    ChrClearFlags(0x000B, 0x0004)
    ChrSetBattleFlags(0x0009, 0x0020)
    ChrSetBattleFlags(0x000B, 0x0020)
    OP_89(0x0009, 17270, 1000, 3140, 270)
    OP_89(0x000B, 17360, 1000, 2550, 270)
    ChrTurnDirection(0x0009, 0x000B, 0)
    ChrTurnDirection(0x000B, 0x0009, 0)

    ChrTalk(
        0x0101,
        (
            '#0010081226V#004F啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_22BF')
    def lambda_22BF():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_22BF)

    @scena.Lambda('lambda_22CD')
    def lambda_22CD():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_22CD)

    @scena.Lambda('lambda_22DB')
    def lambda_22DB():
        OP_99(0x00FE, 0x03, 0x00, 2000)

        ExitThread()

    DispatchAsync(0x0107, 0x0002, lambda_22DB)

    @scena.Lambda('lambda_22EB')
    def lambda_22EB():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_22EB)

    ChrTalk(
        0x0101,
        (
            '#0010081227V#005F喂，等一下！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070081228V#068F爷、爷爷————————！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_234D')
    def lambda_234D():
        CameraMove(17230, 300, 5990, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_234D)

    @scena.Lambda('lambda_2365')
    def lambda_2365():
        ChrMoveTo(0x00FE, 23110, -3000, 1830, 500, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_2365)

    Sleep(100)

    @scena.Lambda('lambda_2385')
    def lambda_2385():
        ChrMoveTo(0x00FE, 23110, -3000, 1830, 750, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_2385)

    Sleep(100)

    @scena.Lambda('lambda_23A5')
    def lambda_23A5():
        ChrMoveTo(0x00FE, 23110, -3000, 1830, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_23A5)

    Sleep(100)

    @scena.Lambda('lambda_23C5')
    def lambda_23C5():
        ChrMoveTo(0x00FE, 23110, -3000, 1830, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_23C5)

    Sleep(1300)

    @scena.Lambda('lambda_23E5')
    def lambda_23E5():
        ChrMoveTo(0x00FE, 23110, -3000, 1830, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_23E5)

    Sleep(100)

    @scena.Lambda('lambda_2405')
    def lambda_2405():
        ChrMoveTo(0x00FE, 23110, -3000, 1830, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_2405)

    Sleep(100)

    @scena.Lambda('lambda_2425')
    def lambda_2425():
        ChrMoveTo(0x00FE, 23110, -3000, 1830, 750, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_2425)

    Sleep(100)

    @scena.Lambda('lambda_2445')
    def lambda_2445():
        ChrMoveTo(0x00FE, 23110, -3000, 1830, 500, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_2445)

    Sleep(100)

    TerminateThread(0x000C, 0xFF)
    WaitForThreadExit(0x0101, 0x0001)
    Fade(1000)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    OP_71(0x0004, 0x0002)
    OP_66(0x0000)
    ChrSetPos(0x000D, 31230, 250, -250, 355)
    ChrSetPos(0x000C, 31230, 250, -250, 355)
    OP_69(0x000D, 0)
    OP_6A(0x000D)
    OP_67(9050, 60020, -29580, 0)
    CameraSetDistance(1560, 0)
    OP_6C(37000, 0)
    OP_6E(171, 0)
    CreateThread(0x000C, 0x01, 0x00, func_03_367C)
    CreateThread(0x000D, 0x01, 0x00, func_04_39E6)
    Sleep(3500)

    OP_20(0x000007D0)
    FadeOut(2000, 0, -1)
    OP_24(0x0079, 0x5A)
    Sleep(100)

    OP_24(0x0079, 0x50)
    Sleep(100)

    OP_24(0x0079, 0x46)
    Sleep(100)

    OP_24(0x0079, 0x3C)
    Sleep(100)

    OP_24(0x0079, 0x32)
    Sleep(100)

    OP_24(0x0079, 0x28)
    Sleep(100)

    OP_24(0x0079, 0x1E)
    Sleep(100)

    OP_24(0x0079, 0x14)
    Sleep(100)

    OP_24(0x0079, 0x0A)
    Sleep(100)

    OP_23(0x0079)
    OP_0D()
    OP_6A(0x0000)
    MapClearFlags(0x00000001)
    OP_66(0x0001)
    CameraMove(13840, 500, 5330, 0)
    OP_67(0, 4990, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetPos(0x0101, 12850, 250, 6370, 130)
    ChrSetPos(0x0102, 14370, 250, 6810, 192)
    ChrClearFlags(0x0106, 0x0020)
    ChrSetChipByIndex(0x0106, 18)
    ChrSetSubChip(0x0106, 0)
    ChrSetPos(0x0106, 11040, 250, 3390, 45)
    ChrSetPos(0x0107, 14260, 250, 5330, 250)
    ChrSetFlags(0x0107, 0x0002)
    ChrSetChipByIndex(0x0107, 12)
    ChrSetSubChip(0x0107, 0)

    @scena.Lambda('lambda_2617')
    def lambda_2617():
        OP_99(0x00FE, 0x00, 0x04, 1500)
        Yield()

        Jump('lambda_2617')

    DispatchAsync2(0x0107, 0x0001, lambda_2617)

    Sleep(2000)

    PlayBGM(83)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0107,
        (
            '#0070081229V#069F#2P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081230V#003F提妲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020081231V#013F总之……\n',
            '我们先回蔡斯吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020081232V要先回协会向雾香小姐\n',
            '报告那艘飞艇的事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081233V#003F嗯、嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010081234V提妲……\n',
            '我知道你很难过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0107, 0x01)
    OP_99(0x0107, 0x00, 0x06, 1500)

    @scena.Lambda('lambda_2746')
    def lambda_2746():
        OP_99(0x00FE, 0x07, 0x0A, 1500)
        Yield()

        Jump('lambda_2746')

    DispatchAsync2(0x0107, 0x0001, lambda_2746)

    Sleep(1000)

    ChrTalk(
        0x0107,
        (
            '#0070081235V#069F#2P…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070081236V……为什么……\n',
            '为什么要把爷爷……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070081237V太过分了……为什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0106, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    OP_63(0x0106)

    ChrTalk(
        0x0106,
        (
            '#0050081238V#053F喂，小不点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2822')
    def lambda_2822():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2822)

    @scena.Lambda('lambda_2830')
    def lambda_2830():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2830)

    CameraMove(13200, 250, 5060, 1000)
    TerminateThread(0x0107, 0x01)

    ChrTalk(
        0x0107,
        (
            '#0070081239V#069F#2P…………？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2877')
    def lambda_2877():
        ChrTurnDirection(0x00FE, 0x0106, 0)
        Yield()

        Jump('lambda_2877')

    DispatchAsync2(0x0102, 0x0002, lambda_2877)

    @scena.Lambda('lambda_2888')
    def lambda_2888():
        ChrTurnDirection(0x00FE, 0x0106, 0)
        Yield()

        Jump('lambda_2888')

    DispatchAsync2(0x0101, 0x0002, lambda_2888)

    @scena.Lambda('lambda_2899')
    def lambda_2899():
        CameraMove(13840, 500, 5330, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2899)

    @scena.Lambda('lambda_28B1')
    def lambda_28B1():
        CameraSetDistance(2780, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_28B1)

    ChrWalkTo(0x0106, 13410, 250, 5290, 3000, 0x00)
    ChrSetFlags(0x0106, 0x0002)
    ChrSetChipByIndex(0x0106, 13)
    ChrSetSubChip(0x0106, 0)
    WaitForThreadExit(0x0101, 0x0001)
    ChrSetSubChip(0x0106, 0)
    Sleep(60)

    ChrSetSubChip(0x0106, 1)
    Sleep(60)

    ChrSetSubChip(0x0106, 2)
    Sleep(60)

    ChrSetSubChip(0x0106, 3)
    Sleep(100)

    ChrSetSubChip(0x0106, 4)
    Sleep(40)

    ChrSetSubChip(0x0106, 5)
    Sleep(40)

    ChrSetSubChip(0x0106, 6)
    PlaySE(165, 0x00, 0x64)
    ChrSetSubChip(0x0107, 11)
    Sleep(60)

    ChrSetSubChip(0x0106, 7)
    Sleep(80)

    ChrSetSubChip(0x0106, 8)
    Sleep(80)

    ChrSetSubChip(0x0106, 9)
    Sleep(80)

    ChrSetSubChip(0x0106, 10)
    Sleep(200)

    ExecExpressionWithValue(
        0x0106,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0106, 18)
    ChrClearFlags(0x0106, 0x1000)
    ChrClearFlags(0x0106, 0x0020)
    ChrClearFlags(0x0106, 0x0002)
    ChrTurnDirection(0x0106, 0x0107, 0)
    OP_99(0x0107, 0x0C, 0x12, 1000)

    ChrTalk(
        0x0107,
        (
            '#0070081240V#065F……啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    OP_99(0x0107, 0x13, 0x15, 2000)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010081241V#004F#1P等、等一下！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050081242V#050F我不是说过了……\n',
            '叫你不要跟来扯我们的后腿。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050081243V就因为你的出现，\n',
            '我们才错过了救你爷爷的时机。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050081244V这个责任……你打算怎么负？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070081245V#065F我……我……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070081246V我……\n',
            '没、没想到会那样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050081247V#057F而且还要用那么差劲的威胁方式，\n',
            '知不知道你刚才差点没命……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050081248V为什么就是不听大人的话？\n',
            '我啊，在这个世界上最讨厌\n',
            '你这种没本事却又要瞎起劲的小鬼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070081249V#065F……对……对……不……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070081250V#069F……对不……起……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070081251V呜…………\n',
            '……呜呜呜呜…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2C0E')
    def lambda_2C0E():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_2C0E)

    ChrWalkTo(0x0101, 13160, 250, 5740, 4000, 0x00)
    ChrMoveTo(0x0106, 13070, 250, 4930, 4000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010081252V#005F#1P够、够了吧！\n',
            '你怎么能说这么过分的话！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010081253V刚刚被掳走的\n',
            '可是她的亲生爷爷啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050081254V#552F所以我才更要说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050081255V喂……小鬼。\n',
            '就算哭也要给我听好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070081256V#069F……呜……呜……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050081257V#057F你想这样就算了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050081258V还没救出爷爷，\n',
            '就这样打算放弃了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2D8F')
    def lambda_2D8F():
        OP_99(0x00FE, 0x15, 0x1A, 1800)
        Yield()

        Jump('lambda_2D8F')

    DispatchAsync2(0x0107, 0x0001, lambda_2D8F)

    Sleep(200)

    @scena.Lambda('lambda_2DA7')
    def lambda_2DA7():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2DA7)

    ChrTalk(
        0x0107,
        (
            '#0070081259V#069F呜呜呜呜……（摇头摇头）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0107, 0x01)
    OP_99(0x0107, 0x15, 0x1B, 1500)

    ChrTalk(
        0x0106,
        (
            '#0050081260V#057F就是啊……\n',
            '别那么窝囊的，振作点！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050081261V哭也好叫也好，\n',
            '靠自己的双脚站起来！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050081262V连自己都照顾不了，\n',
            '还有什么资格去救别人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070081263V#065F……啊…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050081264V#057F要是做不到的话，\n',
            '就不要来给我们添无谓的麻烦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050081265V像个小孩子该做的，\n',
            '躲在被窝里哼哼唧唧地哭个够吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050081266V#552F……哼，\n',
            '那样的话我才要谢天谢地啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070081267V#561F…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081268V#003F提妲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070081269V#561F…………………………\n',
            '不要紧了……姐姐……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070081270V我……\n',
            '……自己站得起来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveTo(0x0101, 13090, 250, 6180, 1000, 0x00)
    Sleep(100)

    ChrMoveTo(0x0106, 12810, 250, 5110, 1000, 0x00)
    Sleep(400)

    OP_99(0x0107, 0x1C, 0x1F, 800)
    Sleep(500)

    ChrTalk(
        0x0106,
        (
            '#0050081271V#051F哼……\n',
            '只要有心还是做得到嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    ChrSetSubChip(0x0107, 32)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0107,
        (
            '#0070081272V#561F真的……很对不起……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070081273V都、都是因为我，\n',
            '才让那些坏人逃走了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081275V#008F傻瓜……\n',
            '用不着道歉啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020081274V#019F是啊。\n',
            '提妲你没事就好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    ChrSetSubChip(0x0107, 31)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0107,
        (
            '#0070081276V#067F谢谢你们……\n',
            '艾丝蒂尔姐姐、约修亚哥哥……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0107,
        (
            '#0070081277V#065F那、那个……阿加特大哥哥……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050081278V#053F怎么了？\n',
            '有什么怨言直说好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070081279V#562F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070081280V真、真的非常谢谢你。\n',
            '在那么危险的时候救了我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0107, 0x1F, 0x22, 1300)
    Sleep(500)

    OP_99(0x0107, 0x22, 0x1F, 1300)
    Sleep(500)

    ChrTalk(
        0x0107,
        (
            '#0070081281V#560F还有的是……\n',
            '谢谢你鼓励我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0106, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(500)

    ChrTalk(
        0x0106,
        (
            '#0050081282V#054F谁、谁鼓励你了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050081283V我只是想让\n',
            '你这哭哭啼啼的小鬼振作一点！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    ChrSetSubChip(0x0107, 35)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0107,
        (
            '#0070081284V#067F呵呵……是呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050081285V#055F我说你刚刚还在哭个不停，\n',
            '现在怎么突然笑起来了啊……！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050081286V真、真是喜怒无常的小鬼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0106, 400)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010081287V#007F你啊，真是的……\n',
            '坦率接受人家的道谢不好吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010081288V真是个爱闹别扭的家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0106, 400)

    ChrTalk(
        0x0102,
        (
            '#0020081291V#019F呵呵……\n',
            '其实阿加特兄只是不好意思罢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081289V#004F哎呀，原～来是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010081290V#001F你也有可爱的一面嘛㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050081292V#053F那边黑头发的小鬼，给我闭嘴！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000003E8)
    Fade(500)

    ExecExpressionWithValue(
        0x0107,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0107, 65535)
    ChrClearFlags(0x0107, 0x1000)
    ChrClearFlags(0x0107, 0x0020)
    ChrClearFlags(0x0107, 0x0002)
    OP_0D()
    OP_21()
    PlayBGM(33)
    Sleep(500)

    ChrTurnDirection(0x0106, 0x0102, 400)

    ChrTalk(
        0x0106,
        (
            '#0050081293V#552F好了……\n',
            '总之马上回城里吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050081294V看来，那些黑衣人并不简单，\n',
            '一定有相当强大的后台撑着。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050081295V这样下去调查很难有所进展……\n',
            '看来有必要和军队合作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081296V#002F嗯……知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020081297V#012F那我们赶快回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0041, 0x01, 0x0400)
    OP_28(0x0041, 0x01, 0x0800)
    Fade(1000)
    ChrSetChipByIndex(0x0106, 65535)
    EventEnd(0x00)

    Return()

# id: 0x0003 offset: 0x367C
@scena.Code('func_03_367C')
def func_03_367C():
    LoadEffect(0x00, 'map\\\\mp021_04.eff')

    @scena.Lambda('lambda_3696')
    def lambda_3696():
        OP_97(0x000C, 490, 7190, -30000, 500, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_3696)

    Sleep(250)

    @scena.Lambda('lambda_36B7')
    def lambda_36B7():
        OP_97(0x000C, 490, 7190, -30000, 1000, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_36B7)

    Sleep(250)

    @scena.Lambda('lambda_36D8')
    def lambda_36D8():
        OP_97(0x000C, 490, 7190, -30000, 1500, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_36D8)

    Sleep(250)

    @scena.Lambda('lambda_36F9')
    def lambda_36F9():
        OP_97(0x000C, 490, 7190, -30000, 2000, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_36F9)

    Sleep(300)

    @scena.Lambda('lambda_371A')
    def lambda_371A():
        OP_97(0x000C, 490, 7190, -30000, 2500, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_371A)

    Sleep(300)

    @scena.Lambda('lambda_373B')
    def lambda_373B():
        OP_97(0x000C, 490, 7190, -30000, 3000, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_373B)

    Sleep(300)

    @scena.Lambda('lambda_375C')
    def lambda_375C():
        OP_97(0x000C, 490, 7190, -30000, 3500, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_375C)

    Sleep(250)

    @scena.Lambda('lambda_377D')
    def lambda_377D():
        OP_97(0x000C, 490, 7190, -30000, 4000, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_377D)

    Sleep(250)

    @scena.Lambda('lambda_379E')
    def lambda_379E():
        OP_97(0x000C, 490, 7190, -30000, 4500, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_379E)

    Sleep(200)

    @scena.Lambda('lambda_37BF')
    def lambda_37BF():
        OP_97(0x000C, 490, 7190, -30000, 7000, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_37BF)

    Sleep(30)

    @scena.Lambda('lambda_37E0')
    def lambda_37E0():
        OP_97(0x000C, 490, 7190, -30000, 9000, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_37E0)

    Sleep(30)

    @scena.Lambda('lambda_3801')
    def lambda_3801():
        OP_97(0x000C, 490, 7190, -30000, 11000, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_3801)

    Sleep(30)

    @scena.Lambda('lambda_3822')
    def lambda_3822():
        OP_97(0x000C, 490, 7190, -30000, 13000, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_3822)

    Sleep(30)

    @scena.Lambda('lambda_3843')
    def lambda_3843():
        OP_97(0x000C, 490, 7190, -30000, 15000, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_3843)

    Sleep(30)

    @scena.Lambda('lambda_3864')
    def lambda_3864():
        OP_97(0x000C, 490, 7190, -30000, 16000, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_3864)

    Sleep(30)

    @scena.Lambda('lambda_3885')
    def lambda_3885():
        OP_97(0x000C, 490, 7190, -30000, 17000, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_3885)

    Sleep(40)

    @scena.Lambda('lambda_38A6')
    def lambda_38A6():
        OP_97(0x000C, 490, 7190, -30000, 18000, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_38A6)

    Sleep(50)

    @scena.Lambda('lambda_38C7')
    def lambda_38C7():
        OP_97(0x000C, 490, 7190, -30000, 19000, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_38C7)

    Sleep(60)

    @scena.Lambda('lambda_38E8')
    def lambda_38E8():
        OP_97(0x000C, 490, 7190, -30000, 20000, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_38E8)

    Sleep(70)

    @scena.Lambda('lambda_3909')
    def lambda_3909():
        OP_97(0x000C, 490, 7190, -30000, 21000, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_3909)

    Sleep(80)

    @scena.Lambda('lambda_392A')
    def lambda_392A():
        OP_97(0x000C, 490, 7190, -30000, 22000, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_392A)

    Sleep(90)

    @scena.Lambda('lambda_394B')
    def lambda_394B():
        OP_97(0x000C, 490, 7190, -30000, 23000, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_394B)

    Sleep(100)

    @scena.Lambda('lambda_396C')
    def lambda_396C():
        OP_97(0x000C, 490, 7190, -30000, 24000, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_396C)

    Sleep(110)

    @scena.Lambda('lambda_398D')
    def lambda_398D():
        OP_97(0x000C, 490, 7190, -30000, 25000, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_398D)

    Sleep(120)

    @scena.Lambda('lambda_39AE')
    def lambda_39AE():
        OP_97(0x000C, 490, 7190, -30000, 26000, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_39AE)

    Sleep(130)

    @scena.Lambda('lambda_39CF')
    def lambda_39CF():
        OP_97(0x000C, 490, 7190, -100000, 27000, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_39CF)

    Return()

# id: 0x0004 offset: 0x39E6
@scena.Code('func_04_39E6')
def func_04_39E6():
    @scena.Lambda('lambda_39EC')
    def lambda_39EC():
        OP_6E(180, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_39EC)

    @scena.Lambda('lambda_39FC')
    def lambda_39FC():
        CameraSetDistance(730, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_39FC)

    OP_97(0x000D, 490, 7190, -1000, 2000, 0x0001)
    OP_97(0x000D, 490, 7190, -1000, 2000, 0x0001)
    OP_97(0x000D, 490, 7190, -1500, 3000, 0x0001)
    OP_97(0x000D, 490, 7190, -1500, 4000, 0x0001)
    OP_97(0x000D, 490, 7190, -2000, 5000, 0x0001)
    OP_97(0x000D, 490, 7190, -2000, 6000, 0x0001)
    OP_97(0x000D, 490, 7190, -2500, 7000, 0x0001)
    OP_97(0x000D, 490, 7190, -2500, 8000, 0x0001)
    OP_97(0x000D, 490, 7190, -2500, 9000, 0x0001)
    OP_97(0x000D, 490, 7190, -2500, 10000, 0x0001)
    OP_97(0x000D, 490, 7190, -2500, 11000, 0x0001)
    OP_97(0x000D, 490, 7190, -3100, 12000, 0x0001)
    OP_97(0x000D, 490, 7190, -3200, 13000, 0x0001)
    OP_97(0x000D, 490, 7190, -3300, 14000, 0x0001)
    OP_97(0x000D, 490, 7190, -3400, 15000, 0x0001)
    OP_97(0x000D, 490, 7190, -3500, 16000, 0x0001)
    OP_97(0x000D, 490, 7190, -3600, 17000, 0x0001)
    OP_97(0x000D, 490, 7190, -3700, 18000, 0x0001)
    OP_97(0x000D, 490, 7190, -2800, 17000, 0x0001)
    OP_97(0x000D, 490, 7190, -2600, 16000, 0x0001)
    OP_97(0x000D, 490, 7190, -2400, 15000, 0x0001)
    OP_97(0x000D, 490, 7190, -2200, 14000, 0x0001)
    OP_97(0x000D, 490, 7190, -2000, 13000, 0x0001)
    OP_97(0x000D, 490, 7190, -1800, 12000, 0x0001)
    OP_97(0x000D, 490, 7190, -1600, 11000, 0x0001)
    OP_97(0x000D, 490, 7190, -1400, 10000, 0x0001)
    OP_97(0x000D, 490, 7190, -1200, 9000, 0x0001)
    OP_97(0x000D, 490, 7190, -1000, 8000, 0x0001)
    OP_97(0x000D, 490, 7190, -800, 7000, 0x0001)
    OP_97(0x000D, 490, 7190, -600, 6000, 0x0001)
    OP_97(0x000D, 490, 7190, -400, 5000, 0x0001)
    OP_97(0x000D, 490, 7190, -200, 4000, 0x0001)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
