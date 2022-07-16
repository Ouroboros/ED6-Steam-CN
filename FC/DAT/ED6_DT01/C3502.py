import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C3502_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C3502   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '黑衣男子'),
    TXT(0x02, '黑衣男子'),
    TXT(0x03, '黑衣男子'),
    TXT(0x04, '拉赛尔博士'),
    TXT(0x05, '特务艇'),
    TXT(0x06, ' '),
    TXT(0x07, '黑衣男子'),
    TXT(0x08, ''),
]

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

# id: 0xFFFF offset: 0x39FA
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

# id: 0x10002 offset: 0x172
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
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

# id: 0x10003 offset: 0x252
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x252
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x252
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x252
@scena.Code('PreInit')
def PreInit():
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
    Event(0, 0x0002)

    def _loc_271(): pass

    label('loc_271')

    Jump('loc_274')

    def _loc_274(): pass

    label('loc_274')

    Return()

# id: 0x0001 offset: 0x275
@scena.Code('Init')
def Init():
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
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x00)
    CameraMove(940, 250, 31840, 0)
    CameraSetDistance(5000, 0)
    SetChrPos(0x0106, 300, 0, -2410, 50)
    SetChrPos(0x0101, 1330, 0, -2710, 50)
    SetChrPos(0x0102, 60, 0, -3500, 50)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x0008, 11190, 250, 4260, 96)
    SetChrPos(0x0009, 11310, 250, 5950, 96)
    SetChrPos(0x000A, 12710, 250, 4560, 96)
    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, 13330, 250, 4520, 180)
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

    @scena.Lambda('lambda_03F3')
    def lambda_03F3():
        OP_67(0, 4700, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_03F3)

    @scena.Lambda('lambda_040B')
    def lambda_040B():
        CameraMove(9830, 250, 2770, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_040B)

    @scena.Lambda('lambda_0423')
    def lambda_0423():
        CameraSetDistance(3700, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0423)

    SetChrChipByIndex(0x0101, 4)

    @scena.Lambda('lambda_0438')
    def lambda_0438():
        ChrWalkTo(0x00FE, 7230, 250, -390, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0438)

    Sleep(200)

    SetChrChipByIndex(0x0106, 8)

    @scena.Lambda('lambda_045D')
    def lambda_045D():
        ChrWalkTo(0x00FE, 6190, 250, 590, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_045D)

    Sleep(200)

    SetChrChipByIndex(0x0102, 6)

    @scena.Lambda('lambda_0482')
    def lambda_0482():
        ChrWalkTo(0x00FE, 5920, 250, -660, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0482)

    Sleep(500)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(500)

    @scena.Lambda('lambda_04EC')
    def lambda_04EC():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_04EC)

    @scena.Lambda('lambda_04FA')
    def lambda_04FA():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_04FA)

    @scena.Lambda('lambda_0508')
    def lambda_0508():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0508)

    WaitForThreadExit(0x0101, 0x0001)
    ChrTurnDirection(0x0101, 0x0008, 400)
    WaitForThreadExit(0x0106, 0x0001)
    ChrTurnDirection(0x0106, 0x0008, 400)
    WaitForThreadExit(0x0102, 0x0001)
    ChrTurnDirection(0x0102, 0x0008, 400)
    SetChrSubChip(0x0102, 11)
    WaitForThreadExit(0x0101, 0x0003)
    ChrMoveTo(0x0008, 11670, 250, 4710, 2000, 0x00)
    SetChrChipByIndex(0x0008, 22)
    Sleep(300)

    SetChrChipByIndex(0x0009, 22)
    SetChrChipByIndex(0x000A, 1)

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
    SetChrChipByIndex(0x0008, 23)

    @scena.Lambda('lambda_0795')
    def lambda_0795():
        ChrMoveToRelative(0x00FE, -3000, 0, -3000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0795)

    Sleep(50)

    SetChrChipByIndex(0x000A, 2)

    @scena.Lambda('lambda_07BA')
    def lambda_07BA():
        ChrMoveToRelative(0x00FE, -3000, 0, -3000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_07BA)

    Sleep(50)

    SetChrChipByIndex(0x0009, 23)

    @scena.Lambda('lambda_07DF')
    def lambda_07DF():
        ChrMoveToRelative(0x00FE, -3000, 0, -3000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_07DF)

    @scena.Lambda('lambda_07FA')
    def lambda_07FA():
        ChrMoveToRelative(0x00FE, 3000, 0, 3000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_07FA)

    Sleep(50)

    @scena.Lambda('lambda_081A')
    def lambda_081A():
        ChrMoveToRelative(0x00FE, 3000, 0, 3000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_081A)

    Sleep(50)

    @scena.Lambda('lambda_083A')
    def lambda_083A():
        ChrMoveToRelative(0x00FE, 3000, 0, 3000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_083A)

    Sleep(200)

    Battle(0x000003A0, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_86D'),
        (-1, 'loc_870'),
    )

    def _loc_86D(): pass

    label('loc_86D')

    OP_B4(0x00)

    Return()

    def _loc_870(): pass

    label('loc_870')

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
    SetChrPos(0x0101, 8730, 250, 6030, 108)
    SetChrPos(0x0106, 8240, 250, 3640, 87)
    SetChrPos(0x0102, 7230, 250, 4750, 101)
    SetChrPos(0x0107, 2860, 250, -2970, 58)
    SetChrChipByIndex(0x0101, 4)
    SetChrChipByIndex(0x0102, 6)
    SetChrSubChip(0x0102, 11)
    SetChrChipByIndex(0x0106, 8)
    SetChrChipByIndex(0x0107, 10)

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

    SetChrChipByIndex(0x0008, 24)
    SetChrChipByIndex(0x0009, 3)
    SetChrChipByIndex(0x000A, 24)
    SetChrPos(0x0008, 12260, 250, 4130, 268)
    SetChrPos(0x0009, 12650, 250, 2620, 288)
    SetChrPos(0x000A, 13120, 250, 5220, 280)
    SetChrPos(0x000B, 14750, 250, 2210, 280)
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

    @scena.Lambda('lambda_0A01')
    def lambda_0A01():
        OP_99(0x00FE, 0x03, 0x00, 800)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0A01)

    @scena.Lambda('lambda_0A11')
    def lambda_0A11():
        OP_99(0x00FE, 0x03, 0x00, 1000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0A11)

    @scena.Lambda('lambda_0A21')
    def lambda_0A21():
        OP_99(0x00FE, 0x03, 0x00, 700)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0A21)

    WaitForThreadExit(0x0009, 0x0001)
    SetChrChipByIndex(0x0009, 1)
    ChrJumpTo(0x0009, 14400, 250, 2770, 500, 5000)
    PlaySE(164, 0x00, 0x64)

    @scena.Lambda('lambda_0A57')
    def lambda_0A57():
        CameraMove(12670, 250, 5070, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0A57)

    WaitForThreadExit(0x000A, 0x0001)
    SetChrChipByIndex(0x000A, 22)

    @scena.Lambda('lambda_0A79')
    def lambda_0A79():
        ChrMoveTo(0x00FE, 14590, 250, 4730, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0A79)

    Sleep(200)

    WaitForThreadExit(0x0008, 0x0001)
    SetChrChipByIndex(0x0008, 22)

    @scena.Lambda('lambda_0AA3')
    def lambda_0AA3():
        ChrMoveTo(0x00FE, 13520, 250, 3650, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0AA3)

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
    SetChrPos(0x000C, 22050, -10000, -11170, 305)
    OP_24(0x0079, 0x50)

    @scena.Lambda('lambda_0D1F')
    def lambda_0D1F():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_0D1F')

    DispatchAsync2(0x0101, 0x0000, lambda_0D1F)

    @scena.Lambda('lambda_0D30')
    def lambda_0D30():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_0D30')

    DispatchAsync2(0x0102, 0x0000, lambda_0D30)

    @scena.Lambda('lambda_0D41')
    def lambda_0D41():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_0D41')

    DispatchAsync2(0x0106, 0x0000, lambda_0D41)

    ChrTalk(
        0x0102,
        (
            '#0020081189V#016F艾丝蒂尔，危险！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_72(0x0004, 0x0004)
    SetChrFlags(0x000C, 0x0040)
    SetChrFlags(0x000C, 0x0004)
    OP_A1(0x000C, 0x0004)
    OP_B0(0x0004, 0x1E)
    OP_6F(0x0004, 975)

    @scena.Lambda('lambda_0D93')
    def lambda_0D93():
        CameraMove(15860, 250, 4980, 5300)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0D93)

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
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000E, 0x0004)
    SetChrBattleFlags(0x000E, 0x0020)
    OP_89(0x000E, 19530, 1810, -9400, 270)

    @scena.Lambda('lambda_0E02')
    def lambda_0E02():
        ChrMoveTo(0x00FE, 23110, 250, 1830, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0E02)

    Sleep(200)

    @scena.Lambda('lambda_0E22')
    def lambda_0E22():
        SetChrDirection(0x00FE, 0, 20)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_0E22)

    @scena.Lambda('lambda_0E30')
    def lambda_0E30():
        ChrMoveTo(0x00FE, 23110, -3000, 1830, 4800, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0E30)

    Sleep(200)

    @scena.Lambda('lambda_0E50')
    def lambda_0E50():
        SetChrDirection(0x00FE, 0, 19)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_0E50)

    @scena.Lambda('lambda_0E5E')
    def lambda_0E5E():
        ChrMoveTo(0x00FE, 23110, -3000, 1830, 4800, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0E5E)

    Sleep(200)

    @scena.Lambda('lambda_0E7E')
    def lambda_0E7E():
        SetChrDirection(0x00FE, 0, 18)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_0E7E)

    @scena.Lambda('lambda_0E8C')
    def lambda_0E8C():
        ChrMoveTo(0x00FE, 23110, -3000, 1830, 4500, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0E8C)

    Sleep(500)

    @scena.Lambda('lambda_0EAC')
    def lambda_0EAC():
        OP_6E(350, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0EAC)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x00FF, 12230, 1000, 1240, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x00FF, 10470, 1000, 1770, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x00FF, 10180, 1000, 3370, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_0F74')
    def lambda_0F74():
        ChrJumpTo(0x00FE, 7000, 250, 6330, 800, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0F74)

    Sleep(100)

    @scena.Lambda('lambda_0F97')
    def lambda_0F97():
        ChrJumpTo(0x00FE, 5140, 250, 4910, 500, 8000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_0F97)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x00FF, 8600, 1000, 3960, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    @scena.Lambda('lambda_0FF4')
    def lambda_0FF4():
        ChrJumpTo(0x00FE, 6160, 250, 2800, 700, 8000)

        ExitThread()

    DispatchAsync(0x0106, 0x0003, lambda_0FF4)

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

    @scena.Lambda('lambda_1113')
    def lambda_1113():
        SetChrDirection(0x00FE, 0, 12)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_1113)

    @scena.Lambda('lambda_1121')
    def lambda_1121():
        ChrMoveTo(0x00FE, 23110, -3000, 1830, 4200, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1121)

    Sleep(100)

    OP_70(0x0004, 1000)
    Sleep(100)

    @scena.Lambda('lambda_114D')
    def lambda_114D():
        SetChrDirection(0x00FE, 0, 11)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_114D)

    @scena.Lambda('lambda_115B')
    def lambda_115B():
        ChrMoveTo(0x00FE, 23110, -3000, 1830, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_115B)

    Sleep(100)

    @scena.Lambda('lambda_117B')
    def lambda_117B():
        SetChrDirection(0x00FE, 0, 10)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_117B)

    @scena.Lambda('lambda_1189')
    def lambda_1189():
        ChrMoveTo(0x00FE, 23110, -3000, 1830, 3500, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1189)

    Sleep(200)

    @scena.Lambda('lambda_11A9')
    def lambda_11A9():
        SetChrDirection(0x00FE, 355, 9)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_11A9)

    @scena.Lambda('lambda_11B7')
    def lambda_11B7():
        ChrMoveTo(0x00FE, 23110, -3000, 1830, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_11B7)

    Sleep(200)

    @scena.Lambda('lambda_11D7')
    def lambda_11D7():
        SetChrDirection(0x00FE, 355, 8)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_11D7)

    @scena.Lambda('lambda_11E5')
    def lambda_11E5():
        ChrMoveTo(0x00FE, 23110, -3000, 1830, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_11E5)

    Sleep(200)

    @scena.Lambda('lambda_1205')
    def lambda_1205():
        SetChrDirection(0x00FE, 355, 6)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_1205)

    @scena.Lambda('lambda_1213')
    def lambda_1213():
        ChrMoveTo(0x00FE, 23110, -3000, 1830, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1213)

    Sleep(200)

    @scena.Lambda('lambda_1233')
    def lambda_1233():
        SetChrDirection(0x00FE, 355, 4)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_1233)

    @scena.Lambda('lambda_1241')
    def lambda_1241():
        ChrMoveTo(0x00FE, 23110, -3000, 1830, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1241)

    Sleep(200)

    @scena.Lambda('lambda_1261')
    def lambda_1261():
        SetChrDirection(0x00FE, 355, 3)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_1261)

    @scena.Lambda('lambda_126F')
    def lambda_126F():
        ChrMoveTo(0x00FE, 23110, -3000, 1830, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_126F)

    Sleep(200)

    @scena.Lambda('lambda_128F')
    def lambda_128F():
        SetChrDirection(0x00FE, 355, 2)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_128F)

    @scena.Lambda('lambda_129D')
    def lambda_129D():
        ChrMoveTo(0x00FE, 23110, -3000, 1830, 500, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_129D)

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

    @scena.Lambda('lambda_1328')
    def lambda_1328():
        ChrMoveTo(0x00FE, 19830, -3500, 7300, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1328)

    @scena.Lambda('lambda_1343')
    def lambda_1343():
        SetChrDirection(0x00FE, 5, 2)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_1343)

    Sleep(300)

    @scena.Lambda('lambda_1356')
    def lambda_1356():
        CameraMove(10930, 650, 4120, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1356)

    @scena.Lambda('lambda_136E')
    def lambda_136E():
        OP_6E(292, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_136E)

    @scena.Lambda('lambda_137E')
    def lambda_137E():
        SetChrDirection(0x00FE, 5, 3)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_137E)

    @scena.Lambda('lambda_138C')
    def lambda_138C():
        ChrMoveTo(0x00FE, 19830, -3500, 7300, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_138C)

    Sleep(300)

    @scena.Lambda('lambda_13AC')
    def lambda_13AC():
        SetChrDirection(0x00FE, 5, 5)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_13AC)

    @scena.Lambda('lambda_13BA')
    def lambda_13BA():
        ChrMoveTo(0x00FE, 19830, -3500, 7300, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_13BA)

    Sleep(1000)

    @scena.Lambda('lambda_13DA')
    def lambda_13DA():
        SetChrDirection(0x00FE, 5, 4)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_13DA)

    @scena.Lambda('lambda_13E8')
    def lambda_13E8():
        ChrMoveTo(0x00FE, 19830, -3500, 7300, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_13E8)

    Sleep(400)

    @scena.Lambda('lambda_1408')
    def lambda_1408():
        SetChrDirection(0x00FE, 5, 3)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_1408)

    @scena.Lambda('lambda_1416')
    def lambda_1416():
        ChrMoveTo(0x00FE, 19830, -3500, 7300, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1416)

    Sleep(400)

    @scena.Lambda('lambda_1436')
    def lambda_1436():
        SetChrDirection(0x00FE, 5, 2)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_1436)

    @scena.Lambda('lambda_1444')
    def lambda_1444():
        ChrMoveTo(0x00FE, 19830, -3500, 7300, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1444)

    Sleep(300)

    @scena.Lambda('lambda_1464')
    def lambda_1464():
        SetChrDirection(0x00FE, 5, 1)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_1464)

    @scena.Lambda('lambda_1472')
    def lambda_1472():
        ChrMoveTo(0x00FE, 19830, -3500, 7300, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1472)

    Sleep(200)

    @scena.Lambda('lambda_1492')
    def lambda_1492():
        ChrMoveTo(0x00FE, 19830, -3500, 7300, 500, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1492)

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

    @scena.Lambda('lambda_16ED')
    def lambda_16ED():
        CameraMove(13430, 650, 4770, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_16ED)

    SetChrFlags(0x0008, 0x0004)
    SetChrFlags(0x0009, 0x0004)
    SetChrFlags(0x000A, 0x0004)
    SetChrChipByIndex(0x000A, 15)
    Sleep(250)

    ChrJumpTo(0x000A, 15670, 1100, 4880, 1300, 5000)
    PlaySE(164, 0x00, 0x64)
    ChrJumpTo(0x000A, 17180, -120, 4710, 500, 5000)
    PlaySE(164, 0x00, 0x64)
    ClearChrFlags(0x000A, 0x0004)
    SetChrBattleFlags(0x000A, 0x0020)
    OP_89(0x000A, 17180, 1000, 4710, 270)
    ChrMoveTo(0x000A, 18650, -150, 5150, 2000, 0x00)
    SetChrChipByIndex(0x0008, 15)
    Sleep(250)

    ChrMoveTo(0x0008, 14720, 250, 3800, 2000, 0x00)
    Sleep(100)

    ChrJumpTo(0x0008, 15660, 1100, 4070, 1300, 5000)
    PlaySE(164, 0x00, 0x64)
    ChrJumpTo(0x0008, 16830, -150, 3710, 500, 5000)
    PlaySE(164, 0x00, 0x64)
    ClearChrFlags(0x0008, 0x0004)
    SetChrBattleFlags(0x0008, 0x0020)
    OP_89(0x0008, 16830, 1000, 3710, 270)
    ChrMoveTo(0x0008, 19200, -130, 3740, 1500, 0x00)
    Sleep(500)

    SetChrChipByIndex(0x0009, 15)
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

    @scena.Lambda('lambda_1869')
    def lambda_1869():
        CameraMove(15200, 250, 4740, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1869)

    SetChrPos(0x0107, 4970, 250, -4350, 45)

    NpcTalk(
        0x0107,
        '小女孩的声音',
        (
            '#0070081206V#18A#2P#3S住、住手～！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    @scena.Lambda('lambda_18C2')
    def lambda_18C2():
        ChrWalkTo(0x00FE, 27140, 250, -840, 4100, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_18C2)

    Sleep(50)

    @scena.Lambda('lambda_18E2')
    def lambda_18E2():
        ChrWalkTo(0x00FE, 27140, 250, -840, 4100, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_18E2)

    Sleep(50)

    @scena.Lambda('lambda_1902')
    def lambda_1902():
        ChrWalkTo(0x00FE, 27140, 250, -840, 4100, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1902)

    SetChrPos(0x000D, 17450, 1200, 7800, 0)
    PlaySE(506, 0x00, 0x64)
    PlayEffect(0x02, 0xFF, 0x0107, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x000D, 0, 0, 0, 0)
    Sleep(620)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    SetChrChipByIndex(0x0009, 0)

    @scena.Lambda('lambda_19B7')
    def lambda_19B7():
        ChrTurnDirection(0x00FE, 0x0107, 600)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_19B7)

    @scena.Lambda('lambda_19C5')
    def lambda_19C5():
        ChrTurnDirection(0x00FE, 0x0107, 600)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_19C5)

    @scena.Lambda('lambda_19D3')
    def lambda_19D3():
        ChrTurnDirection(0x00FE, 0x0107, 600)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_19D3)

    @scena.Lambda('lambda_19E1')
    def lambda_19E1():
        OP_94(0x00, 0x00FE, 0x0000, 0x00000190, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_19E1)

    OP_62(0x0106, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(100)

    @scena.Lambda('lambda_1A13')
    def lambda_1A13():
        OP_94(0x00, 0x00FE, 0x0000, 0x00000190, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1A13)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    @scena.Lambda('lambda_1A45')
    def lambda_1A45():
        OP_94(0x00, 0x00FE, 0x0000, 0x00000190, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1A45)

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

    @scena.Lambda('lambda_1A91')
    def lambda_1A91():
        CameraMove(12830, 250, 2990, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1A91)

    @scena.Lambda('lambda_1AA9')
    def lambda_1AA9():
        OP_6E(270, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1AA9)

    @scena.Lambda('lambda_1AB9')
    def lambda_1AB9():
        ChrTurnDirection(0x00FE, 0x0107, 600)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_1AB9)

    Sleep(50)

    @scena.Lambda('lambda_1ACC')
    def lambda_1ACC():
        ChrTurnDirection(0x00FE, 0x0107, 600)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1ACC)

    Sleep(50)

    @scena.Lambda('lambda_1ADF')
    def lambda_1ADF():
        ChrTurnDirection(0x00FE, 0x0107, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1ADF)

    Sleep(500)

    @scena.Lambda('lambda_1AF2')
    def lambda_1AF2():
        ChrTurnDirection(0x00FE, 0x0107, 0)
        Yield()

        Jump('lambda_1AF2')

    DispatchAsync2(0x0101, 0x0000, lambda_1AF2)

    @scena.Lambda('lambda_1B03')
    def lambda_1B03():
        ChrTurnDirection(0x00FE, 0x0107, 0)
        Yield()

        Jump('lambda_1B03')

    DispatchAsync2(0x0102, 0x0000, lambda_1B03)

    @scena.Lambda('lambda_1B14')
    def lambda_1B14():
        ChrTurnDirection(0x00FE, 0x0107, 0)
        Yield()

        Jump('lambda_1B14')

    DispatchAsync2(0x0106, 0x0000, lambda_1B14)

    @scena.Lambda('lambda_1B25')
    def lambda_1B25():
        ChrWalkTo(0x00FE, 8580, 250, -2130, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_1B25)

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
    SetChrChipByIndex(0x0107, 17)

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
    SetChrPos(0x000D, 17450, 1200, 7800, 0)
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

    @scena.Lambda('lambda_1C91')
    def lambda_1C91():
        CameraMove(11750, 250, 1440, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1C91)

    @scena.Lambda('lambda_1CA9')
    def lambda_1CA9():
        OP_6E(242, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1CA9)

    PlaySE(216, 0x00, 0x64)
    SetChrChipByIndex(0x0009, 16)
    TerminateThread(0x0106, 0x00)
    TerminateThread(0x0102, 0x00)
    TerminateThread(0x0101, 0x00)

    @scena.Lambda('lambda_1CCF')
    def lambda_1CCF():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1CCF)

    @scena.Lambda('lambda_1CDD')
    def lambda_1CDD():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1CDD)

    @scena.Lambda('lambda_1CEB')
    def lambda_1CEB():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_1CEB)

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

    @scena.Lambda('lambda_1D66')
    def lambda_1D66():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_1D66)

    ChrTalk(
        0x0106,
        (
            '#0050081218V#550F……嘁！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0106, 18)

    @scena.Lambda('lambda_1D93')
    def lambda_1D93():
        CameraMove(9360, 250, -2160, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1D93)

    @scena.Lambda('lambda_1DAB')
    def lambda_1DAB():
        OP_6C(40000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1DAB)

    SetChrFlags(0x0106, 0x1000)
    SetChrChipByIndex(0x0106, 19)

    @scena.Lambda('lambda_1DC5')
    def lambda_1DC5():
        ChrWalkTo(0x00FE, 8060, 250, -640, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_1DC5)

    Sleep(200)

    @scena.Lambda('lambda_1DE5')
    def lambda_1DE5():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1DE5)

    @scena.Lambda('lambda_1DF3')
    def lambda_1DF3():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1DF3)

    WaitForThreadExit(0x0106, 0x0001)

    @scena.Lambda('lambda_1E06')
    def lambda_1E06():
        OP_92(0x00FE, 0x0107, 500, 8000, 0x01)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_1E06)

    SetChrPos(0x000D, 8580, 1000, -2130, 0)
    PlayEffect(0x00, 0xFF, 0x0009, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0x000D, 0, 0, 0, 0)

    @scena.Lambda('lambda_1E61')
    def lambda_1E61():
        OP_99(0x00FE, 0x00, 0x07, 2000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1E61)

    WaitForThreadExit(0x0106, 0x0001)
    SetChrFlags(0x0107, 0x1000)
    SetChrFlags(0x0107, 0x0020)

    ExecExpressionWithValue(
        0x0107,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0107, 21)
    ChrTurnDirection(0x0107, 0x0106, 0)

    @scena.Lambda('lambda_1E97')
    def lambda_1E97():
        OP_99(0x00FE, 0x00, 0x03, 1500)

        ExitThread()

    DispatchAsync(0x0107, 0x0002, lambda_1E97)

    @scena.Lambda('lambda_1EA7')
    def lambda_1EA7():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_1EA7)

    WaitForThreadExit(0x0106, 0x0001)
    SetChrDirection(0x0106, 180, 0)
    SetChrFlags(0x0106, 0x0020)

    ExecExpressionWithValue(
        0x0106,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0106, 20)

    @scena.Lambda('lambda_1EDE')
    def lambda_1EDE():
        ChrJumpTo(0x00FE, 7970, 250, -2730, 600, 6000)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_1EDE)

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
    ClearChrFlags(0x0106, 0x1000)

    @scena.Lambda('lambda_1FAB')
    def lambda_1FAB():
        CameraSetDistance(3500, 1200)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_1FAB)

    @scena.Lambda('lambda_1FBB')
    def lambda_1FBB():
        CameraMove(12340, 250, 2410, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1FBB)

    @scena.Lambda('lambda_1FD3')
    def lambda_1FD3():
        OP_6E(312, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1FD3)

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
    SetChrChipByIndex(0x0009, 0)
    SetChrFlags(0x0009, 0x0004)
    SetChrFlags(0x000B, 0x0004)
    ChrTurnDirection(0x0009, 0x000B, 800)
    ChrTurnDirection(0x000B, 0x0009, 800)

    @scena.Lambda('lambda_20AF')
    def lambda_20AF():
        ChrJumpTo(0x00FE, 17270, -120, 3140, 1300, 5000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_20AF)

    @scena.Lambda('lambda_20CD')
    def lambda_20CD():
        ChrJumpTo(0x00FE, 17360, -140, 2550, 1300, 5000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_20CD)

    @scena.Lambda('lambda_20EB')
    def lambda_20EB():
        CameraMove(12820, 250, 1370, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_20EB)

    WaitForThreadExit(0x0009, 0x0001)
    WaitForThreadExit(0x000B, 0x0001)
    ClearChrFlags(0x0009, 0x0004)
    ClearChrFlags(0x000B, 0x0004)
    SetChrBattleFlags(0x0009, 0x0020)
    SetChrBattleFlags(0x000B, 0x0020)
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

    @scena.Lambda('lambda_216B')
    def lambda_216B():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_216B)

    @scena.Lambda('lambda_2179')
    def lambda_2179():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2179)

    @scena.Lambda('lambda_2187')
    def lambda_2187():
        OP_99(0x00FE, 0x03, 0x00, 2000)

        ExitThread()

    DispatchAsync(0x0107, 0x0002, lambda_2187)

    @scena.Lambda('lambda_2197')
    def lambda_2197():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_2197)

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

    @scena.Lambda('lambda_21EF')
    def lambda_21EF():
        CameraMove(17230, 300, 5990, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_21EF)

    @scena.Lambda('lambda_2207')
    def lambda_2207():
        ChrMoveTo(0x00FE, 23110, -3000, 1830, 500, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_2207)

    Sleep(100)

    @scena.Lambda('lambda_2227')
    def lambda_2227():
        ChrMoveTo(0x00FE, 23110, -3000, 1830, 750, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_2227)

    Sleep(100)

    @scena.Lambda('lambda_2247')
    def lambda_2247():
        ChrMoveTo(0x00FE, 23110, -3000, 1830, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_2247)

    Sleep(100)

    @scena.Lambda('lambda_2267')
    def lambda_2267():
        ChrMoveTo(0x00FE, 23110, -3000, 1830, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_2267)

    Sleep(1300)

    @scena.Lambda('lambda_2287')
    def lambda_2287():
        ChrMoveTo(0x00FE, 23110, -3000, 1830, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_2287)

    Sleep(100)

    @scena.Lambda('lambda_22A7')
    def lambda_22A7():
        ChrMoveTo(0x00FE, 23110, -3000, 1830, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_22A7)

    Sleep(100)

    @scena.Lambda('lambda_22C7')
    def lambda_22C7():
        ChrMoveTo(0x00FE, 23110, -3000, 1830, 750, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_22C7)

    Sleep(100)

    @scena.Lambda('lambda_22E7')
    def lambda_22E7():
        ChrMoveTo(0x00FE, 23110, -3000, 1830, 500, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_22E7)

    Sleep(100)

    TerminateThread(0x000C, 0xFF)
    WaitForThreadExit(0x0101, 0x0001)
    Fade(1000)
    SetChrFlags(0x000E, 0x0080)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    OP_71(0x0004, 0x0002)
    OP_66(0x0000)
    SetChrPos(0x000D, 31230, 250, -250, 355)
    SetChrPos(0x000C, 31230, 250, -250, 355)
    OP_69(0x000D, 0)
    OP_6A(0x000D)
    OP_67(9050, 60020, -29580, 0)
    CameraSetDistance(1560, 0)
    OP_6C(37000, 0)
    OP_6E(171, 0)
    CreateThread(0x000C, 0x01, 0x00, 0x0003)
    CreateThread(0x000D, 0x01, 0x00, 0x0004)
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
    ClearMapFlags(0x00000001)
    OP_66(0x0001)
    CameraMove(13840, 500, 5330, 0)
    OP_67(0, 4990, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrPos(0x0101, 12850, 250, 6370, 130)
    SetChrPos(0x0102, 14370, 250, 6810, 192)
    ClearChrFlags(0x0106, 0x0020)
    SetChrChipByIndex(0x0106, 18)
    SetChrSubChip(0x0106, 0)
    SetChrPos(0x0106, 11040, 250, 3390, 45)
    SetChrPos(0x0107, 14260, 250, 5330, 250)
    SetChrFlags(0x0107, 0x0002)
    SetChrChipByIndex(0x0107, 12)
    SetChrSubChip(0x0107, 0)

    @scena.Lambda('lambda_24B9')
    def lambda_24B9():
        OP_99(0x00FE, 0x00, 0x04, 1500)
        Yield()

        Jump('lambda_24B9')

    DispatchAsync2(0x0107, 0x0001, lambda_24B9)

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

    @scena.Lambda('lambda_25CA')
    def lambda_25CA():
        OP_99(0x00FE, 0x07, 0x0A, 1500)
        Yield()

        Jump('lambda_25CA')

    DispatchAsync2(0x0107, 0x0001, lambda_25CA)

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

    @scena.Lambda('lambda_2692')
    def lambda_2692():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2692)

    @scena.Lambda('lambda_26A0')
    def lambda_26A0():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_26A0)

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

    @scena.Lambda('lambda_26E2')
    def lambda_26E2():
        ChrTurnDirection(0x00FE, 0x0106, 0)
        Yield()

        Jump('lambda_26E2')

    DispatchAsync2(0x0102, 0x0002, lambda_26E2)

    @scena.Lambda('lambda_26F3')
    def lambda_26F3():
        ChrTurnDirection(0x00FE, 0x0106, 0)
        Yield()

        Jump('lambda_26F3')

    DispatchAsync2(0x0101, 0x0002, lambda_26F3)

    @scena.Lambda('lambda_2704')
    def lambda_2704():
        CameraMove(13840, 500, 5330, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2704)

    @scena.Lambda('lambda_271C')
    def lambda_271C():
        CameraSetDistance(2780, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_271C)

    ChrWalkTo(0x0106, 13410, 250, 5290, 3000, 0x00)
    SetChrFlags(0x0106, 0x0002)
    SetChrChipByIndex(0x0106, 13)
    SetChrSubChip(0x0106, 0)
    WaitForThreadExit(0x0101, 0x0001)
    SetChrSubChip(0x0106, 0)
    Sleep(60)

    SetChrSubChip(0x0106, 1)
    Sleep(60)

    SetChrSubChip(0x0106, 2)
    Sleep(60)

    SetChrSubChip(0x0106, 3)
    Sleep(100)

    SetChrSubChip(0x0106, 4)
    Sleep(40)

    SetChrSubChip(0x0106, 5)
    Sleep(40)

    SetChrSubChip(0x0106, 6)
    PlaySE(165, 0x00, 0x64)
    SetChrSubChip(0x0107, 11)
    Sleep(60)

    SetChrSubChip(0x0106, 7)
    Sleep(80)

    SetChrSubChip(0x0106, 8)
    Sleep(80)

    SetChrSubChip(0x0106, 9)
    Sleep(80)

    SetChrSubChip(0x0106, 10)
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

    SetChrChipByIndex(0x0106, 18)
    ClearChrFlags(0x0106, 0x1000)
    ClearChrFlags(0x0106, 0x0020)
    ClearChrFlags(0x0106, 0x0002)
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

    @scena.Lambda('lambda_2A3D')
    def lambda_2A3D():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_2A3D)

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

    @scena.Lambda('lambda_2B9B')
    def lambda_2B9B():
        OP_99(0x00FE, 0x15, 0x1A, 1800)
        Yield()

        Jump('lambda_2B9B')

    DispatchAsync2(0x0107, 0x0001, lambda_2B9B)

    Sleep(200)

    @scena.Lambda('lambda_2BB3')
    def lambda_2BB3():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2BB3)

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
    SetChrSubChip(0x0107, 32)
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
    SetChrSubChip(0x0107, 31)
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
    SetChrSubChip(0x0107, 35)
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

    SetChrChipByIndex(0x0107, 65535)
    ClearChrFlags(0x0107, 0x1000)
    ClearChrFlags(0x0107, 0x0020)
    ClearChrFlags(0x0107, 0x0002)
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
    SetChrChipByIndex(0x0106, 65535)
    EventEnd(0x00)

    Return()

# id: 0x0003 offset: 0x33C5
@scena.Code('func_03_33C5')
def func_03_33C5():
    LoadEffect(0x00, 'map\\\\mp021_04.eff')

    @scena.Lambda('lambda_33DF')
    def lambda_33DF():
        OP_97(0x000C, 490, 7190, -30000, 500, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_33DF)

    Sleep(250)

    @scena.Lambda('lambda_3400')
    def lambda_3400():
        OP_97(0x000C, 490, 7190, -30000, 1000, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_3400)

    Sleep(250)

    @scena.Lambda('lambda_3421')
    def lambda_3421():
        OP_97(0x000C, 490, 7190, -30000, 1500, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_3421)

    Sleep(250)

    @scena.Lambda('lambda_3442')
    def lambda_3442():
        OP_97(0x000C, 490, 7190, -30000, 2000, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_3442)

    Sleep(300)

    @scena.Lambda('lambda_3463')
    def lambda_3463():
        OP_97(0x000C, 490, 7190, -30000, 2500, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_3463)

    Sleep(300)

    @scena.Lambda('lambda_3484')
    def lambda_3484():
        OP_97(0x000C, 490, 7190, -30000, 3000, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_3484)

    Sleep(300)

    @scena.Lambda('lambda_34A5')
    def lambda_34A5():
        OP_97(0x000C, 490, 7190, -30000, 3500, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_34A5)

    Sleep(250)

    @scena.Lambda('lambda_34C6')
    def lambda_34C6():
        OP_97(0x000C, 490, 7190, -30000, 4000, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_34C6)

    Sleep(250)

    @scena.Lambda('lambda_34E7')
    def lambda_34E7():
        OP_97(0x000C, 490, 7190, -30000, 4500, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_34E7)

    Sleep(200)

    @scena.Lambda('lambda_3508')
    def lambda_3508():
        OP_97(0x000C, 490, 7190, -30000, 7000, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_3508)

    Sleep(30)

    @scena.Lambda('lambda_3529')
    def lambda_3529():
        OP_97(0x000C, 490, 7190, -30000, 9000, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_3529)

    Sleep(30)

    @scena.Lambda('lambda_354A')
    def lambda_354A():
        OP_97(0x000C, 490, 7190, -30000, 11000, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_354A)

    Sleep(30)

    @scena.Lambda('lambda_356B')
    def lambda_356B():
        OP_97(0x000C, 490, 7190, -30000, 13000, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_356B)

    Sleep(30)

    @scena.Lambda('lambda_358C')
    def lambda_358C():
        OP_97(0x000C, 490, 7190, -30000, 15000, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_358C)

    Sleep(30)

    @scena.Lambda('lambda_35AD')
    def lambda_35AD():
        OP_97(0x000C, 490, 7190, -30000, 16000, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_35AD)

    Sleep(30)

    @scena.Lambda('lambda_35CE')
    def lambda_35CE():
        OP_97(0x000C, 490, 7190, -30000, 17000, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_35CE)

    Sleep(40)

    @scena.Lambda('lambda_35EF')
    def lambda_35EF():
        OP_97(0x000C, 490, 7190, -30000, 18000, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_35EF)

    Sleep(50)

    @scena.Lambda('lambda_3610')
    def lambda_3610():
        OP_97(0x000C, 490, 7190, -30000, 19000, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_3610)

    Sleep(60)

    @scena.Lambda('lambda_3631')
    def lambda_3631():
        OP_97(0x000C, 490, 7190, -30000, 20000, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_3631)

    Sleep(70)

    @scena.Lambda('lambda_3652')
    def lambda_3652():
        OP_97(0x000C, 490, 7190, -30000, 21000, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_3652)

    Sleep(80)

    @scena.Lambda('lambda_3673')
    def lambda_3673():
        OP_97(0x000C, 490, 7190, -30000, 22000, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_3673)

    Sleep(90)

    @scena.Lambda('lambda_3694')
    def lambda_3694():
        OP_97(0x000C, 490, 7190, -30000, 23000, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_3694)

    Sleep(100)

    @scena.Lambda('lambda_36B5')
    def lambda_36B5():
        OP_97(0x000C, 490, 7190, -30000, 24000, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_36B5)

    Sleep(110)

    @scena.Lambda('lambda_36D6')
    def lambda_36D6():
        OP_97(0x000C, 490, 7190, -30000, 25000, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_36D6)

    Sleep(120)

    @scena.Lambda('lambda_36F7')
    def lambda_36F7():
        OP_97(0x000C, 490, 7190, -30000, 26000, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_36F7)

    Sleep(130)

    @scena.Lambda('lambda_3718')
    def lambda_3718():
        OP_97(0x000C, 490, 7190, -100000, 27000, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_3718)

    Return()

# id: 0x0004 offset: 0x372F
@scena.Code('func_04_372F')
def func_04_372F():
    @scena.Lambda('lambda_3735')
    def lambda_3735():
        OP_6E(180, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3735)

    @scena.Lambda('lambda_3745')
    def lambda_3745():
        CameraSetDistance(730, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3745)

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
