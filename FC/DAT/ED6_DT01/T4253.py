import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4253_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4253   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4253.x'
    header.mapIndex       = 1
    header.bgm            = 17
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
        ('ED6_DT07/CH02460._CH', 'ED6_DT07/CH02460P._CP'),
        ('ED6_DT07/CH02230._CH', 'ED6_DT07/CH02230P._CP'),
        ('ED6_DT07/CH02240._CH', 'ED6_DT07/CH02240P._CP'),
        ('ED6_DT07/CH01330._CH', 'ED6_DT07/CH01330P._CP'),
        ('ED6_DT07/CH00340._CH', 'ED6_DT07/CH00340P._CP'),
        ('ED6_DT07/CH00344._CH', 'ED6_DT07/CH00344P._CP'),
        ('ED6_DT07/CH00110._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT07/CH00111._CH', 'ED6_DT07/CH00111P._CP'),
        ('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP'),
        ('ED6_DT07/CH00171._CH', 'ED6_DT07/CH00171P._CP'),
        ('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP'),
        ('ED6_DT07/CH00131._CH', 'ED6_DT07/CH00131P._CP'),
        ('ED6_DT07/CH02090._CH', 'ED6_DT07/CH02090P._CP'),
    ]

# id: 0x10001 offset: 0x112
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '尤莉亚中尉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
    )

# id: 0x10002 offset: 0x1D2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
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
    )

# id: 0x0000 offset: 0x1D2
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1FC',
    )

    ChrSetChipByIndex(0x0000, 0)
    ChrSetChipByIndex(0x0001, 1)
    ChrSetChipByIndex(0x0138, 2)
    ChrSetFlags(0x0000, 0x1000)
    ChrSetFlags(0x0001, 0x1000)
    ChrSetFlags(0x0138, 0x1000)

    def _loc_1FC(): pass

    label('loc_1FC')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000065, 'loc_208'),
        (-1, 'loc_21E'),
    )

    def _loc_208(): pass

    label('loc_208')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 1, 0x661)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 0, 0x660)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_21B',
    )

    SetScenaFlags(ScenaFlag(0x00CC, 1, 0x661))
    Event(0, func_04_433)

    def _loc_21B(): pass

    label('loc_21B')

    Jump('loc_21E')

    def _loc_21E(): pass

    label('loc_21E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_245',
    )

    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 74910, 0, -38410, 99)
    CreateThread(0x000D, 0x00, 0x00, func_02_28F)

    Jump('loc_274')

    def _loc_245(): pass

    label('loc_245')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_24F',
    )

    Jump('loc_274')

    def _loc_24F(): pass

    label('loc_24F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_259',
    )

    Jump('loc_274')

    def _loc_259(): pass

    label('loc_259')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_263',
    )

    Jump('loc_274')

    def _loc_263(): pass

    label('loc_263')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_26D',
    )

    Jump('loc_274')

    def _loc_26D(): pass

    label('loc_26D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_274',
    )

    def _loc_274(): pass

    label('loc_274')

    Return()

# id: 0x0001 offset: 0x275
@scena.Code('func_01_275')
def func_01_275():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 4, 0x644)),
            Expr.Return,
        ),
        'loc_285',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_285(): pass

    label('loc_285')

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0002 offset: 0x28F
@scena.Code('func_02_28F')
def func_02_28F():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2A4',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_28F')

    def _loc_2A4(): pass

    label('loc_2A4')

    Return()

# id: 0x0003 offset: 0x2A5
@scena.Code('func_03_2A5')
def func_03_2A5():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_358',
    )

    ChrTalk(
        0x000D,
        (
            '#0101060012V#178F这次的事情让我深刻体会到\n',
            '自己还远远没有成熟。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0101060013V卡西乌斯上校也回来了。\n',
            '为了不再辱没亲卫队的名声，\n',
            '我更要借此机会身心兼顾地认真修炼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_42F')

    def _loc_358(): pass

    label('loc_358')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x000D,
        (
            '#0101060009V#176F呼～\n',
            '终于又回到这里来了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0101060010V这次的事情让我深刻体会到\n',
            '自己还远远没有成熟。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0101060011V#178F卡西乌斯上校也回来了。\n',
            '为了不再辱没亲卫队的名声，\n',
            '我更要借此机会身心兼顾地认真修炼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_42F(): pass

    label('loc_42F')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x433
@scena.Code('func_04_433')
def func_04_433():
    EventBegin(0x00)
    ChrSetChipByIndex(0x0102, 6)
    ChrSetChipByIndex(0x0108, 8)
    ChrSetChipByIndex(0x0104, 10)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x0102, 66560, 0, -30890, 186)
    ChrSetPos(0x0108, 65640, 0, -29760, 182)
    ChrSetPos(0x0104, 67130, 0, -29550, 172)
    ChrSetPos(0x0008, 68760, 0, -39520, 135)
    ChrSetPos(0x0009, 69890, 0, -40660, 315)
    ChrSetPos(0x000A, 65810, 0, -43750, 270)
    ChrSetPos(0x000B, 65730, 0, -41730, 214)
    ChrSetPos(0x000C, 63940, 0, -43580, 111)
    CameraMove(68190, 0, -42370, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    CameraMove(67700, 0, -42570, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_056E')
    def lambda_056E():
        CameraMove(66270, 0, -37030, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_056E)

    @scena.Lambda('lambda_0586')
    def lambda_0586():
        OP_6E(300, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_0586)

    @scena.Lambda('lambda_0596')
    def lambda_0596():
        OP_67(0, 5550, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_0596)

    @scena.Lambda('lambda_05AE')
    def lambda_05AE():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_05AE)

    Sleep(100)

    @scena.Lambda('lambda_05C1')
    def lambda_05C1():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_05C1)

    Sleep(100)

    @scena.Lambda('lambda_05D4')
    def lambda_05D4():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_05D4)

    Sleep(100)

    @scena.Lambda('lambda_05E7')
    def lambda_05E7():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_05E7)

    Sleep(100)

    @scena.Lambda('lambda_05FA')
    def lambda_05FA():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_05FA)

    WaitForThreadExit(0x0000, 0x0001)

    ChrTalk(
        0x0008,
        (
            '啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0008, 4)
    Sleep(100)

    ChrSetChipByIndex(0x000A, 4)
    ChrSetChipByIndex(0x000B, 4)
    Sleep(100)

    ChrSetChipByIndex(0x0009, 4)
    ChrSetChipByIndex(0x000C, 4)

    ChrTalk(
        0x0009,
        (
            '岂有此理，是侵入者！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#030F被侵入的一方\n',
            '肯定是会这么说的啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F用不着和他们解释什么的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F……我们上！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_06C0')
    def lambda_06C0():
        ChrWalkTo(0x00FE, 66130, 0, -52310, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_06C0)

    @scena.Lambda('lambda_06DB')
    def lambda_06DB():
        ChrWalkTo(0x00FE, 66130, 0, -52310, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_06DB)

    @scena.Lambda('lambda_06F6')
    def lambda_06F6():
        ChrWalkTo(0x00FE, 66130, 0, -52310, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_06F6)

    @scena.Lambda('lambda_0711')
    def lambda_0711():
        CameraMove(65930, 0, -40190, 800)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_0711)

    @scena.Lambda('lambda_0729')
    def lambda_0729():
        OP_6E(225, 800)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_0729)

    Sleep(500)

    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0108, 0xFF)
    TerminateThread(0x0104, 0xFF)
    Battle(0x000003A9, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_75D'),
        (-1, 'loc_760'),
    )

    def _loc_75D(): pass

    label('loc_75D')

    OP_B4(0x00)

    Return()

    def _loc_760(): pass

    label('loc_760')

    EventBegin(0x00)
    CameraMove(68410, 0, -39770, 0)
    OP_6E(309, 0)
    ChrSetPos(0x0102, 69140, 0, -41420, 217)
    ChrSetPos(0x0108, 66620, 0, -39440, 188)
    ChrSetPos(0x0104, 69070, 0, -39370, 233)
    ChrSetPos(0x0008, 64750, 0, -43440, 203)
    ChrSetPos(0x0009, 66130, 0, -44420, 111)
    ChrSetPos(0x000A, 65480, 0, -42510, 0)
    ChrSetPos(0x000B, 67860, 0, -42520, 0)
    ChrSetPos(0x000C, 66830, 0, -45880, 180)
    Sleep(500)

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0102, 65535)

    ExecExpressionWithValue(
        0x0104,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0104, 65535)

    ExecExpressionWithValue(
        0x0108,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0108, 65535)

    @scena.Lambda('lambda_083F')
    def lambda_083F():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_083F')

    DispatchAsync2(0x0108, 0x0001, lambda_083F)

    ChrTalk(
        0x0108,
        (
            '#0080131144V#070F好的，先胜一局。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0877')
    def lambda_0877():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_0877')

    DispatchAsync2(0x0104, 0x0001, lambda_0877)

    ChrTalk(
        0x0104,
        (
            '#030F哎呀，真不过瘾啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_08A5')
    def lambda_08A5():
        ChrWalkTo(0x00FE, 73930, 0, -42020, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_08A5)

    CameraMove(70990, 0, -40680, 2000)
    TerminateThread(0x0108, 0xFF)
    TerminateThread(0x0104, 0xFF)

    ChrTalk(
        0x0102,
        (
            '#010F现在我就开始操作\n',
            '城门的开关装置！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020131147V如果敌人来了请将其击退！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F噢，没问题！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我以『不动』之名保证，\n',
            '不让任何人攻入！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0108, 8)
    ChrSetDirection(0x0108, 270, 400)
    ChrSetChipByIndex(0x0104, 10)

    ChrTalk(
        0x0104,
        (
            '#030F呵呵，此刻就是\n',
            '天上之门打开之时了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '……最终的乐章奏响了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x004E, 0x04, 0x02)
    OP_28(0x004E, 0x04, 0x04)
    OP_28(0x004E, 0x01, 0x0001)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T4200._SN', 100, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
