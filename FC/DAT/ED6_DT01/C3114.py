import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C3114_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C3114   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '阿加特'),
    TXT(0x02, '提妲'),
    TXT(0x03, '拉赛尔博士'),
    TXT(0x04, '地图物体0'),
    TXT(0x05, ''),
]

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

# id: 0xFFFF offset: 0xABD
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
        ('ED6_DT07/CH00050._CH', 'ED6_DT07/CH00050P._CP'),
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT07/CH02020._CH', 'ED6_DT07/CH02020P._CP'),
        ('ED6_DT07/CH00005._CH', 'ED6_DT07/CH00005P._CP'),
        ('ED6_DT07/CH00015._CH', 'ED6_DT07/CH00015P._CP'),
    ]

# id: 0x10002 offset: 0xD2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
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

# id: 0x10003 offset: 0x152
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x152
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

# id: 0x10005 offset: 0x172
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x172
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_185',
    )

    SetMapFlags(0x10000000)
    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x0002)

    def _loc_185(): pass

    label('loc_185')

    Return()

# id: 0x0001 offset: 0x186
@scena.Code('Init')
def Init():
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

    ClearChrFlags(0x0009, 0x0004)
    ClearChrFlags(0x0008, 0x0004)
    ClearChrFlags(0x000A, 0x0004)
    SetChrBattleFlags(0x0009, 0x0020)
    SetChrBattleFlags(0x0008, 0x0020)
    SetChrBattleFlags(0x000A, 0x0020)
    OP_89(0x0009, 3380, 1000, 12290, 180)
    OP_89(0x0008, 2780, 1000, 12440, 180)
    OP_89(0x000A, 2780, 1000, 11260, 180)
    OP_A1(0x000B, 0x0000)
    OP_10(0x00, 0x00)
    PlaySE(461, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x218
@scena.Code('ReInit')
def ReInit():
    ClearMapFlags(0x10000000)
    EventBegin(0x00)
    CameraMove(6310, 0, -12430, 0)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x0A, 0xFF)
    SetChrFlags(0x0101, 0x0080)
    SetChrPos(0x0101, 8300, 1980, -14000, 270)
    SetChrFlags(0x0102, 0x0080)
    SetChrPos(0x0102, 8300, 1980, -14000, 270)
    SetChrChipByIndex(0x0101, 3)
    SetChrChipByIndex(0x0102, 4)
    SetChrFlags(0x0102, 0x0004)
    SetChrFlags(0x0101, 0x0004)
    SetChrFlags(0x0102, 0x0020)
    SetChrFlags(0x0101, 0x0020)
    SetChrFlags(0x0101, 0x1000)
    SetChrFlags(0x0102, 0x1000)
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

    ClearChrFlags(0x0101, 0x0080)
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    PlaySE(173, 0x00, 0x64)
    ChrMoveTo(0x0101, 5650, 0, -14750, 13000, 0x00)
    ClearChrFlags(0x0101, 0x0004)
    ChrJumpTo(0x0101, 4800, 0, -15150, 800, 5000)
    SetChrChipByIndex(0x0101, 65535)
    ClearChrFlags(0x0101, 0x0020)
    ClearChrFlags(0x0101, 0x1000)
    Sleep(200)

    @scena.Lambda('lambda_0337')
    def lambda_0337():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_0337')

    DispatchAsync2(0x0101, 0x0002, lambda_0337)

    Sleep(500)

    @scena.Lambda('lambda_034D')
    def lambda_034D():
        ChrMoveTo(0x00FE, 5290, 0, -13890, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_034D)

    ClearChrFlags(0x0102, 0x0080)
    PlaySE(173, 0x00, 0x64)
    ChrWalkTo(0x0102, 5650, 0, -14750, 13000, 0x00)
    ClearChrFlags(0x0102, 0x0004)
    ChrJumpTo(0x0102, 4800, 0, -15150, 800, 7000)
    SetChrChipByIndex(0x0102, 65535)
    ClearChrFlags(0x0102, 0x0020)
    ClearChrFlags(0x0102, 0x1000)
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

# id: 0x0003 offset: 0x442
@scena.Code('func_03_442')
def func_03_442():
    EventBegin(0x00)
    SetChrFlags(0x000B, 0x0040)
    SetChrFlags(0x000B, 0x0004)

    @scena.Lambda('lambda_0454')
    def lambda_0454():
        ChrTurnDirection(0x0101, 0x0009, 0)
        Yield()

        Jump('lambda_0454')

    DispatchAsync2(0x0101, 0x0001, lambda_0454)

    @scena.Lambda('lambda_0465')
    def lambda_0465():
        ChrTurnDirection(0x0102, 0x0009, 0)
        Yield()

        Jump('lambda_0465')

    DispatchAsync2(0x0102, 0x0001, lambda_0465)

    @scena.Lambda('lambda_0476')
    def lambda_0476():
        ChrWalkTo(0x0101, 4660, 0, 13460, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0476)

    @scena.Lambda('lambda_0491')
    def lambda_0491():
        ChrWalkTo(0x0102, 4710, 0, 12480, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0491)

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
    SetChrFlags(0x0102, 0x0040)
    SetChrFlags(0x0102, 0x0004)

    ExecExpressionWithValue(
        0x0102,
        0x0B,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrFlags(0x0102, 0x1000)
    SetChrDirection(0x0102, 270, 0)
    SetChrSubChip(0x0102, 2)

    @scena.Lambda('lambda_058C')
    def lambda_058C():
        OP_99(0x00FE, 0x02, 0x00, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_058C)

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

    ClearChrFlags(0x0102, 0x1000)
    SetChrSubChip(0x0102, 0)
    ClearChrFlags(0x0102, 0x0004)
    ChrWalkTo(0x0102, 2670, -1100, 13810, 3000, 0x00)
    SetChrFlags(0x0101, 0x0040)
    SetChrFlags(0x0101, 0x0004)
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

    SetChrFlags(0x0101, 0x1000)
    SetChrDirection(0x0101, 270, 0)
    SetChrSubChip(0x0101, 4)

    @scena.Lambda('lambda_060E')
    def lambda_060E():
        OP_99(0x00FE, 0x04, 0x06, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_060E)

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

    ClearChrFlags(0x0101, 0x1000)
    SetChrSubChip(0x0101, 0)
    ChrTurnDirection(0x0101, 0x000A, 400)
    ClearChrFlags(0x0101, 0x0004)
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

    @scena.Lambda('lambda_06B8')
    def lambda_06B8():
        SetChrDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_06B8)

    Sleep(400)

    @scena.Lambda('lambda_06CB')
    def lambda_06CB():
        SetChrDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_06CB)

    @scena.Lambda('lambda_06D9')
    def lambda_06D9():
        SetChrDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_06D9)

    @scena.Lambda('lambda_06E7')
    def lambda_06E7():
        SetChrDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_06E7)

    @scena.Lambda('lambda_06F5')
    def lambda_06F5():
        SetChrDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_06F5)

    @scena.Lambda('lambda_0703')
    def lambda_0703():
        CameraMove(890, 0, 18340, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0703)

    @scena.Lambda('lambda_071B')
    def lambda_071B():
        OP_67(0, 3790, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_071B)

    @scena.Lambda('lambda_0733')
    def lambda_0733():
        OP_6C(60000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0733)

    PlaySE(146, 0x00, 0x64)
    LoadEffect(0x04, 'map\\\\mp013_00.eff')
    LoadEffect(0x05, 'map\\\\mp013_01.eff')
    PlayEffect(0x04, 0x00, 0x000B, 0, 0, 2200, 180, 0, 0, 600, 100, 3000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x05, 0x01, 0x000B, 0, 0, -1800, 180, 0, 0, 700, 700, 700, 0x00FF, 0, 0, 0, 0)
    Sleep(800)

    @scena.Lambda('lambda_07DF')
    def lambda_07DF():
        SetChrDirection(0x00FE, 135, 5)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_07DF)

    @scena.Lambda('lambda_07ED')
    def lambda_07ED():
        ChrMoveToRelativeAsync(0x00FE, -3000, 0, 3000, 600, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_07ED)

    Sleep(200)

    @scena.Lambda('lambda_080D')
    def lambda_080D():
        SetChrDirection(0x00FE, 135, 10)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_080D)

    @scena.Lambda('lambda_081B')
    def lambda_081B():
        ChrMoveToRelativeAsync(0x00FE, -3000, 0, 3000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_081B)

    Sleep(500)

    @scena.Lambda('lambda_083B')
    def lambda_083B():
        SetChrDirection(0x00FE, 135, 20)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_083B)

    @scena.Lambda('lambda_0849')
    def lambda_0849():
        ChrMoveToRelativeAsync(0x00FE, -3000, 0, 3000, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0849)

    @scena.Lambda('lambda_0864')
    def lambda_0864():
        SetChrDirection(0x00FE, 135, 13)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_0864)

    Sleep(100)

    @scena.Lambda('lambda_0877')
    def lambda_0877():
        ChrMoveToRelativeAsync(0x00FE, -3000, 0, 3000, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0877)

    Sleep(100)

    @scena.Lambda('lambda_0897')
    def lambda_0897():
        SetChrDirection(0x00FE, 135, 13)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_0897)

    @scena.Lambda('lambda_08A5')
    def lambda_08A5():
        ChrMoveToRelativeAsync(0x00FE, -3000, 0, 3000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_08A5)

    Sleep(250)

    @scena.Lambda('lambda_08C5')
    def lambda_08C5():
        SetChrDirection(0x00FE, 135, 8)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_08C5)

    @scena.Lambda('lambda_08D3')
    def lambda_08D3():
        ChrMoveToRelativeAsync(0x00FE, -3000, 0, 3000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_08D3)

    Sleep(250)

    @scena.Lambda('lambda_08F3')
    def lambda_08F3():
        SetChrDirection(0x00FE, 135, 5)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_08F3)

    @scena.Lambda('lambda_0901')
    def lambda_0901():
        ChrMoveToRelativeAsync(0x00FE, -3000, 0, 3000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0901)

    Sleep(250)

    @scena.Lambda('lambda_0921')
    def lambda_0921():
        SetChrDirection(0x00FE, 180, 5)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_0921)

    @scena.Lambda('lambda_092F')
    def lambda_092F():
        ChrMoveToRelativeAsync(0x00FE, -3000, 0, 3000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_092F)

    Sleep(300)

    @scena.Lambda('lambda_094F')
    def lambda_094F():
        SetChrDirection(0x00FE, 180, 10)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_094F)

    @scena.Lambda('lambda_095D')
    def lambda_095D():
        ChrMoveToRelativeAsync(0x00FE, -3000, 0, 3000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_095D)

    Sleep(100)

    @scena.Lambda('lambda_097D')
    def lambda_097D():
        SetChrDirection(0x00FE, 180, 15)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_097D)

    @scena.Lambda('lambda_098B')
    def lambda_098B():
        ChrMoveToRelativeAsync(0x00FE, -3000, 0, 3000, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_098B)

    Sleep(100)

    @scena.Lambda('lambda_09AB')
    def lambda_09AB():
        SetChrDirection(0x00FE, 180, 20)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_09AB)

    @scena.Lambda('lambda_09B9')
    def lambda_09B9():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 10000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_09B9)

    Sleep(300)

    PlayEffect(0x04, 0x02, 0x000B, 0, 0, 2200, 180, 0, 0, 1000, 100, 3000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_0A0E')
    def lambda_0A0E():
        SetChrDirection(0x00FE, 180, 25)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_0A0E)

    @scena.Lambda('lambda_0A1C')
    def lambda_0A1C():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 10000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0A1C)

    Sleep(300)

    @scena.Lambda('lambda_0A3C')
    def lambda_0A3C():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 10000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0A3C)

    @scena.Lambda('lambda_0A57')
    def lambda_0A57():
        SetChrDirection(0x00FE, 180, 20)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_0A57)

    Sleep(300)

    @scena.Lambda('lambda_0A6A')
    def lambda_0A6A():
        SetChrDirection(0x00FE, 180, 10)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_0A6A)

    @scena.Lambda('lambda_0A78')
    def lambda_0A78():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 10000, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0A78)

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
