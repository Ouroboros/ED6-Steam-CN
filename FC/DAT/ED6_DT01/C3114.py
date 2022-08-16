import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C3114_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C3114   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'C3114.x'
    header.mapIndex       = 1
    header.bgm            = 34
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
        ('ED6_DT07/CH00050._CH', 'ED6_DT07/CH00050P._CP'),
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT07/CH02020._CH', 'ED6_DT07/CH02020P._CP'),
        ('ED6_DT07/CH00005._CH', 'ED6_DT07/CH00005P._CP'),
        ('ED6_DT07/CH00015._CH', 'ED6_DT07/CH00015P._CP'),
    ]

# id: 0x10001 offset: 0xD2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '阿加特',
            x                   = 3380,
            z                   = -1100,
            y                   = 12290,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '提妲',
            x                   = 2780,
            z                   = -1100,
            y                   = 12440,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '拉赛尔博士',
            x                   = 2780,
            z                   = -1100,
            y                   = 11260,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '地图物体0',
            x                   = 3000,
            z                   = -1000,
            y                   = 12000,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0008,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x152
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x152
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 2680,
            y           = -1000,
            z           = 12450,
            range       = 5000,
            dword_10    = 0x00001388,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000003,
        ),
    )

# id: 0x10004 offset: 0x172
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x172
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_185',
    )

    MapSetFlags(0x10000000)
    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_02_218)

    def _loc_185(): pass

    label('loc_185')

    Return()

# id: 0x0001 offset: 0x186
@scena.Code('func_01_186')
def func_01_186():
    @scena.Lambda('lambda_018C')
    def lambda_018C():
        ChrTurnDirection(0x00FE, 0x0000, 0)
        Yield()

        Jump('lambda_018C')

    DispatchAsync2(0x0009, 0x0002, lambda_018C)

    @scena.Lambda('lambda_019D')
    def lambda_019D():
        ChrTurnDirection(0x00FE, 0x0000, 0)
        Yield()

        Jump('lambda_019D')

    DispatchAsync2(0x0008, 0x0002, lambda_019D)

    @scena.Lambda('lambda_01AE')
    def lambda_01AE():
        ChrTurnDirection(0x00FE, 0x0000, 0)
        Yield()

        Jump('lambda_01AE')

    DispatchAsync2(0x000A, 0x0002, lambda_01AE)

    ChrClearFlags(0x0009, 0x0004)
    ChrClearFlags(0x0008, 0x0004)
    ChrClearFlags(0x000A, 0x0004)
    ChrSetBattleFlags(0x0009, 0x0020)
    ChrSetBattleFlags(0x0008, 0x0020)
    ChrSetBattleFlags(0x000A, 0x0020)
    OP_89(0x0009, 3380, 1000, 12290, 180)
    OP_89(0x0008, 2780, 1000, 12440, 180)
    OP_89(0x000A, 2780, 1000, 11260, 180)
    OP_A1(0x000B, 0x0000)
    OP_10(0x00, 0x00)
    PlaySE(461, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x218
@scena.Code('func_02_218')
def func_02_218():
    MapClearFlags(0x10000000)
    EventBegin(0x00)
    CameraMove(6310, 0, -12430, 0)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x0A, 0xFF)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetPos(0x0101, 8300, 1980, -14000, 270)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetPos(0x0102, 8300, 1980, -14000, 270)
    ChrSetChipByIndex(0x0101, 3)
    ChrSetChipByIndex(0x0102, 4)
    ChrSetFlags(0x0102, 0x0004)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetFlags(0x0102, 0x0020)
    ChrSetFlags(0x0101, 0x0020)
    ChrSetFlags(0x0101, 0x1000)
    ChrSetFlags(0x0102, 0x1000)
    FadeIn(1000, 0)
    OP_0D()

    NpcTalk(
        0x0101,
        '艾丝蒂尔的声音',
        (
            '#0010091365V#16A#3P#1S呜哇啊啊啊！？',
            0x5,
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrClearFlags(0x0101, 0x0080)
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    PlaySE(173, 0x00, 0x64)
    ChrMoveTo(0x0101, 5650, 0, -14750, 13000, 0x00)
    ChrClearFlags(0x0101, 0x0004)
    ChrJumpTo(0x0101, 4800, 0, -15150, 800, 5000)
    ChrSetChipByIndex(0x0101, 65535)
    ChrClearFlags(0x0101, 0x0020)
    ChrClearFlags(0x0101, 0x1000)
    Sleep(200)

    @scena.Lambda('lambda_033C')
    def lambda_033C():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_033C')

    DispatchAsync2(0x0101, 0x0002, lambda_033C)

    Sleep(500)

    @scena.Lambda('lambda_0352')
    def lambda_0352():
        ChrMoveTo(0x00FE, 5290, 0, -13890, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0352)

    ChrClearFlags(0x0102, 0x0080)
    PlaySE(173, 0x00, 0x64)
    ChrWalkTo(0x0102, 5650, 0, -14750, 13000, 0x00)
    ChrClearFlags(0x0102, 0x0004)
    ChrJumpTo(0x0102, 4800, 0, -15150, 800, 7000)
    ChrSetChipByIndex(0x0102, 65535)
    ChrClearFlags(0x0102, 0x0020)
    ChrClearFlags(0x0102, 0x1000)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0101,
        (
            '#0010091366V#008F呼～吓了我一大跳！\n',
            '没想到会是这样滑下来的设计。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091367V#010F看来已经到达秘密水道了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020091368V走，快点追上去吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    EventEnd(0x00)

    Return()

# id: 0x0003 offset: 0x456
@scena.Code('func_03_456')
def func_03_456():
    EventBegin(0x00)
    ChrSetFlags(0x000B, 0x0040)
    ChrSetFlags(0x000B, 0x0004)

    @scena.Lambda('lambda_0468')
    def lambda_0468():
        ChrTurnDirection(0x0101, 0x0009, 0)
        Yield()

        Jump('lambda_0468')

    DispatchAsync2(0x0101, 0x0001, lambda_0468)

    @scena.Lambda('lambda_0479')
    def lambda_0479():
        ChrTurnDirection(0x0102, 0x0009, 0)
        Yield()

        Jump('lambda_0479')

    DispatchAsync2(0x0102, 0x0001, lambda_0479)

    @scena.Lambda('lambda_048A')
    def lambda_048A():
        ChrWalkTo(0x0101, 4660, 0, 13460, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_048A)

    @scena.Lambda('lambda_04A5')
    def lambda_04A5():
        ChrWalkTo(0x0102, 4710, 0, 12480, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_04A5)

    CameraMove(4330, 0, 12390, 1000)

    ChrTalk(
        0x000A,
        (
            '#0540091369V#103F哦，好像来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070091370V#560F姐姐，这边！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050091371V#054F太慢了！\n',
            '在磨蹭什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010091372V#506F不好意思。\n',
            '刚才稍微谈了点老爸的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    ChrSetFlags(0x0102, 0x0040)
    ChrSetFlags(0x0102, 0x0004)

    ExecExpressionWithValue(
        0x0102,
        0x0B,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x0102, 0x1000)
    ChrSetDirection(0x0102, 270, 0)
    ChrSetSubChip(0x0102, 2)

    @scena.Lambda('lambda_05B4')
    def lambda_05B4():
        OP_99(0x00FE, 0x02, 0x00, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_05B4)

    ChrJumpTo(0x0102, 3380, -1100, 13810, 1000, 6000)

    ExecExpressionWithValue(
        0x0102,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x0102, 0x1000)
    ChrSetSubChip(0x0102, 0)
    ChrClearFlags(0x0102, 0x0004)
    ChrWalkTo(0x0102, 2670, -1100, 13810, 3000, 0x00)
    ChrSetFlags(0x0101, 0x0040)
    ChrSetFlags(0x0101, 0x0004)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ExecExpressionWithValue(
        0x0101,
        0x0B,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x0101, 0x1000)
    ChrSetDirection(0x0101, 270, 0)
    ChrSetSubChip(0x0101, 4)

    @scena.Lambda('lambda_0636')
    def lambda_0636():
        OP_99(0x00FE, 0x04, 0x06, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0636)

    ChrJumpTo(0x0101, 3380, -1100, 13810, 1000, 6000)

    ExecExpressionWithValue(
        0x0101,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x0101, 0x1000)
    ChrSetSubChip(0x0101, 0)
    ChrTurnDirection(0x0101, 0x000A, 400)
    ChrClearFlags(0x0101, 0x0004)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x000A, 0xFF)

    ChrTalk(
        0x0102,
        (
            '#0020091373V#012F让你们久等了。\n',
            '我们这就出发吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0540091374V#105F好……\n',
            '你们抓紧了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_06EA')
    def lambda_06EA():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_06EA)

    Sleep(400)

    @scena.Lambda('lambda_06FD')
    def lambda_06FD():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_06FD)

    @scena.Lambda('lambda_070B')
    def lambda_070B():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_070B)

    @scena.Lambda('lambda_0719')
    def lambda_0719():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0719)

    @scena.Lambda('lambda_0727')
    def lambda_0727():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0727)

    @scena.Lambda('lambda_0735')
    def lambda_0735():
        CameraMove(890, 0, 18340, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0735)

    @scena.Lambda('lambda_074D')
    def lambda_074D():
        OP_67(0, 3790, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_074D)

    @scena.Lambda('lambda_0765')
    def lambda_0765():
        OP_6C(60000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0765)

    PlaySE(146, 0x00, 0x64)
    LoadEffect(0x04, 'map\\\\mp013_00.eff')
    LoadEffect(0x05, 'map\\\\mp013_01.eff')
    PlayEffect(0x04, 0x00, 0x000B, 0, 0, 2200, 180, 0, 0, 600, 100, 3000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x05, 0x01, 0x000B, 0, 0, -1800, 180, 0, 0, 700, 700, 700, 0x00FF, 0, 0, 0, 0)
    Sleep(800)

    @scena.Lambda('lambda_0811')
    def lambda_0811():
        ChrSetDirection(0x00FE, 135, 5)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_0811)

    @scena.Lambda('lambda_081F')
    def lambda_081F():
        ChrMoveToRelativeAsync(0x00FE, -3000, 0, 3000, 600, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_081F)

    Sleep(200)

    @scena.Lambda('lambda_083F')
    def lambda_083F():
        ChrSetDirection(0x00FE, 135, 10)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_083F)

    @scena.Lambda('lambda_084D')
    def lambda_084D():
        ChrMoveToRelativeAsync(0x00FE, -3000, 0, 3000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_084D)

    Sleep(500)

    @scena.Lambda('lambda_086D')
    def lambda_086D():
        ChrSetDirection(0x00FE, 135, 20)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_086D)

    @scena.Lambda('lambda_087B')
    def lambda_087B():
        ChrMoveToRelativeAsync(0x00FE, -3000, 0, 3000, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_087B)

    @scena.Lambda('lambda_0896')
    def lambda_0896():
        ChrSetDirection(0x00FE, 135, 13)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_0896)

    Sleep(100)

    @scena.Lambda('lambda_08A9')
    def lambda_08A9():
        ChrMoveToRelativeAsync(0x00FE, -3000, 0, 3000, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_08A9)

    Sleep(100)

    @scena.Lambda('lambda_08C9')
    def lambda_08C9():
        ChrSetDirection(0x00FE, 135, 13)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_08C9)

    @scena.Lambda('lambda_08D7')
    def lambda_08D7():
        ChrMoveToRelativeAsync(0x00FE, -3000, 0, 3000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_08D7)

    Sleep(250)

    @scena.Lambda('lambda_08F7')
    def lambda_08F7():
        ChrSetDirection(0x00FE, 135, 8)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_08F7)

    @scena.Lambda('lambda_0905')
    def lambda_0905():
        ChrMoveToRelativeAsync(0x00FE, -3000, 0, 3000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0905)

    Sleep(250)

    @scena.Lambda('lambda_0925')
    def lambda_0925():
        ChrSetDirection(0x00FE, 135, 5)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_0925)

    @scena.Lambda('lambda_0933')
    def lambda_0933():
        ChrMoveToRelativeAsync(0x00FE, -3000, 0, 3000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0933)

    Sleep(250)

    @scena.Lambda('lambda_0953')
    def lambda_0953():
        ChrSetDirection(0x00FE, 180, 5)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_0953)

    @scena.Lambda('lambda_0961')
    def lambda_0961():
        ChrMoveToRelativeAsync(0x00FE, -3000, 0, 3000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0961)

    Sleep(300)

    @scena.Lambda('lambda_0981')
    def lambda_0981():
        ChrSetDirection(0x00FE, 180, 10)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_0981)

    @scena.Lambda('lambda_098F')
    def lambda_098F():
        ChrMoveToRelativeAsync(0x00FE, -3000, 0, 3000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_098F)

    Sleep(100)

    @scena.Lambda('lambda_09AF')
    def lambda_09AF():
        ChrSetDirection(0x00FE, 180, 15)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_09AF)

    @scena.Lambda('lambda_09BD')
    def lambda_09BD():
        ChrMoveToRelativeAsync(0x00FE, -3000, 0, 3000, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_09BD)

    Sleep(100)

    @scena.Lambda('lambda_09DD')
    def lambda_09DD():
        ChrSetDirection(0x00FE, 180, 20)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_09DD)

    @scena.Lambda('lambda_09EB')
    def lambda_09EB():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 10000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_09EB)

    Sleep(300)

    PlayEffect(0x04, 0x02, 0x000B, 0, 0, 2200, 180, 0, 0, 1000, 100, 3000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_0A40')
    def lambda_0A40():
        ChrSetDirection(0x00FE, 180, 25)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_0A40)

    @scena.Lambda('lambda_0A4E')
    def lambda_0A4E():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 10000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0A4E)

    Sleep(300)

    @scena.Lambda('lambda_0A6E')
    def lambda_0A6E():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 10000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0A6E)

    @scena.Lambda('lambda_0A89')
    def lambda_0A89():
        ChrSetDirection(0x00FE, 180, 20)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_0A89)

    Sleep(300)

    @scena.Lambda('lambda_0A9C')
    def lambda_0A9C():
        ChrSetDirection(0x00FE, 180, 10)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_0A9C)

    @scena.Lambda('lambda_0AAA')
    def lambda_0AAA():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 10000, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0AAA)

    Sleep(1000)

    OP_20(0x000007D0)
    FadeOut(1500, 0, -1)
    OP_0D()
    OP_21()
    Sleep(2000)

    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/C3104._SN', 100, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
