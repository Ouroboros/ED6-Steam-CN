import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2100_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2100_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T2100.x'
    header.mapIndex       = 1
    header.bgm            = 12
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
    )

# id: 0x10000 offset: 0x64
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
    ]

# id: 0x10001 offset: 0x64
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10002 offset: 0x64
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x64
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x64
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x64
@scena.Code('Init')
def Init():
    MapClearFlags(0x00000001)
    EventBegin(0x00)

    ExecExpressionWithValue(
        0x0012,
        0x01,
        (
            (Expr.PushLong, 0x32C8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0012,
        0x02,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0012,
        0x03,
        (
            (Expr.PushLong, 0x11EB8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_28(0x0020, 0x01, 0x0004)
    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirectionByPos(0x0000, 13500, 73400, 400)
    Fade(1000)

    If(
        (
            (Expr.GetChrWork, 0x1, 0x3),
            (Expr.PushLong, 0x11EB8),
            Expr.Geq,
            (Expr.GetChrWork, 0x2, 0x3),
            (Expr.PushLong, 0x11EB8),
            Expr.Geq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_139',
    )

    ExecExpressionWithValue(
        0x0001,
        0x01,
        (
            (Expr.GetChrWork, 0x0, 0x1),
            (Expr.PushLong, 0x258),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0001,
        0x02,
        (
            (Expr.GetChrWork, 0x0, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0001,
        0x03,
        (
            (Expr.GetChrWork, 0x0, 0x3),
            (Expr.PushLong, 0x4B0),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0002,
        0x01,
        (
            (Expr.GetChrWork, 0x1, 0x1),
            (Expr.PushLong, 0x64),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0002,
        0x02,
        (
            (Expr.GetChrWork, 0x1, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0002,
        0x03,
        (
            (Expr.GetChrWork, 0x1, 0x3),
            (Expr.PushLong, 0x4B0),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetDirection(0x0001, 180, 0)
    ChrSetDirection(0x0002, 180, 0)

    Jump('loc_2B0')

    def _loc_139(): pass

    label('loc_139')

    If(
        (
            (Expr.GetChrWork, 0x1, 0x3),
            (Expr.PushLong, 0x11EB8),
            Expr.Lss,
            (Expr.GetChrWork, 0x2, 0x3),
            (Expr.PushLong, 0x11EB8),
            Expr.Geq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1B7',
    )

    ExecExpressionWithValue(
        0x0001,
        0x01,
        (
            (Expr.GetChrWork, 0x0, 0x1),
            (Expr.PushLong, 0x258),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0001,
        0x02,
        (
            (Expr.GetChrWork, 0x0, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0001,
        0x03,
        (
            (Expr.GetChrWork, 0x0, 0x3),
            (Expr.PushLong, 0x4B0),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0002,
        0x01,
        (
            (Expr.GetChrWork, 0x1, 0x1),
            (Expr.PushLong, 0x64),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0002,
        0x02,
        (
            (Expr.GetChrWork, 0x1, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0002,
        0x03,
        (
            (Expr.GetChrWork, 0x1, 0x3),
            (Expr.PushLong, 0x4B0),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetDirection(0x0001, 180, 0)
    ChrSetDirection(0x0002, 180, 0)

    Jump('loc_2B0')

    def _loc_1B7(): pass

    label('loc_1B7')

    If(
        (
            (Expr.GetChrWork, 0x1, 0x3),
            (Expr.PushLong, 0x11EB8),
            Expr.Lss,
            (Expr.GetChrWork, 0x2, 0x3),
            (Expr.PushLong, 0x11EB8),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_235',
    )

    ExecExpressionWithValue(
        0x0001,
        0x01,
        (
            (Expr.GetChrWork, 0x0, 0x1),
            (Expr.PushLong, 0x258),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0001,
        0x02,
        (
            (Expr.GetChrWork, 0x0, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0001,
        0x03,
        (
            (Expr.GetChrWork, 0x0, 0x3),
            (Expr.PushLong, 0x4B0),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0002,
        0x01,
        (
            (Expr.GetChrWork, 0x1, 0x1),
            (Expr.PushLong, 0x64),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0002,
        0x02,
        (
            (Expr.GetChrWork, 0x1, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0002,
        0x03,
        (
            (Expr.GetChrWork, 0x1, 0x3),
            (Expr.PushLong, 0x4B0),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetDirection(0x0001, 0, 0)
    ChrSetDirection(0x0002, 0, 0)

    Jump('loc_2B0')

    def _loc_235(): pass

    label('loc_235')

    If(
        (
            (Expr.GetChrWork, 0x1, 0x3),
            (Expr.PushLong, 0x11EB8),
            Expr.Geq,
            (Expr.GetChrWork, 0x2, 0x3),
            (Expr.PushLong, 0x11EB8),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2B0',
    )

    ExecExpressionWithValue(
        0x0001,
        0x01,
        (
            (Expr.GetChrWork, 0x0, 0x1),
            (Expr.PushLong, 0x258),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0001,
        0x02,
        (
            (Expr.GetChrWork, 0x0, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0001,
        0x03,
        (
            (Expr.GetChrWork, 0x0, 0x3),
            (Expr.PushLong, 0x4B0),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0002,
        0x01,
        (
            (Expr.GetChrWork, 0x1, 0x1),
            (Expr.PushLong, 0x64),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0002,
        0x02,
        (
            (Expr.GetChrWork, 0x1, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0002,
        0x03,
        (
            (Expr.GetChrWork, 0x1, 0x3),
            (Expr.PushLong, 0x4B0),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetDirection(0x0001, 0, 0)
    ChrSetDirection(0x0002, 0, 0)

    def _loc_2B0(): pass

    label('loc_2B0')

    If(
        (
            (Expr.PushValueByIndex, 0x64),
            (Expr.PushLong, 0x2D),
            Expr.Geq,
            (Expr.PushValueByIndex, 0x64),
            (Expr.PushLong, 0x5A),
            Expr.Leq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2E9',
    )

    @scena.Lambda('lambda_02CB')
    def lambda_02CB():
        CameraMove(13500, 1500, 73400, 3000)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_02CB)

    OP_6C(135000, 3000)

    Jump('loc_3CA')

    def _loc_2E9(): pass

    label('loc_2E9')

    If(
        (
            (Expr.PushValueByIndex, 0x64),
            (Expr.PushLong, 0x5A),
            Expr.Gtr,
            (Expr.PushValueByIndex, 0x64),
            (Expr.PushLong, 0x87),
            Expr.Leq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_322',
    )

    @scena.Lambda('lambda_0304')
    def lambda_0304():
        CameraMove(13500, 1500, 73400, 3000)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_0304)

    OP_6C(45000, 3000)

    Jump('loc_3CA')

    def _loc_322(): pass

    label('loc_322')

    If(
        (
            (Expr.PushValueByIndex, 0x64),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            (Expr.PushValueByIndex, 0x64),
            (Expr.PushLong, 0x2D),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_35B',
    )

    @scena.Lambda('lambda_033D')
    def lambda_033D():
        CameraMove(13500, 1500, 73400, 3000)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_033D)

    OP_6C(45000, 3000)

    Jump('loc_3CA')

    def _loc_35B(): pass

    label('loc_35B')

    If(
        (
            (Expr.PushValueByIndex, 0x64),
            (Expr.PushLong, 0x10E),
            Expr.Geq,
            (Expr.PushValueByIndex, 0x64),
            (Expr.PushLong, 0x168),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_394',
    )

    @scena.Lambda('lambda_0376')
    def lambda_0376():
        CameraMove(13500, 1500, 73400, 3000)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_0376)

    OP_6C(45000, 3000)

    Jump('loc_3CA')

    def _loc_394(): pass

    label('loc_394')

    If(
        (
            (Expr.PushValueByIndex, 0x64),
            (Expr.PushLong, 0x87),
            Expr.Gtr,
            (Expr.PushValueByIndex, 0x64),
            (Expr.PushLong, 0x10E),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3CA',
    )

    @scena.Lambda('lambda_03AF')
    def lambda_03AF():
        CameraMove(13500, 1500, 73400, 3000)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_03AF)

    OP_6C(135000, 3000)

    def _loc_3CA(): pass

    label('loc_3CA')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_47D',
    )

    ChrTalk(
        0x0101,
        (
            '#0010170112V#002F#1P…………嗯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0402')
    def lambda_0402():
        ChrTurnDirection(0x0102, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0402)

    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020170113V#014F怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170114V#002F#1P……那、那个。\n',
            '不是卡片吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_046B')
    def lambda_046B():
        ChrTurnDirection(0x0102, 0x0012, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_046B)

    ChrTurnDirection(0x0105, 0x0012, 400)

    Jump('loc_6C2')

    def _loc_47D(): pass

    label('loc_47D')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5C9',
    )

    ChrTalk(
        0x0102,
        (
            '#0020170115V#014F#1P嗯…………？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_04B5')
    def lambda_04B5():
        ChrTurnDirection(0x0101, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_04B5)

    ChrTurnDirection(0x0105, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010160011V#501F怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020170117V#014F#1P…………是卡片。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010170118V#004F……啊！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170119V在、在哪里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020170120V#012F#1P在那块金属板上面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0596')
    def lambda_0596():
        ChrTurnDirection(0x0101, 0x0012, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0596)

    ChrTurnDirection(0x0105, 0x0012, 400)

    ChrTalk(
        0x0101,
        (
            '#0010170121V#004F啊，果然！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6C2')

    def _loc_5C9(): pass

    label('loc_5C9')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6C2',
    )

    ChrTalk(
        0x0105,
        (
            '#0060170122V#044F#1P咦…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_05FF')
    def lambda_05FF():
        ChrTurnDirection(0x0102, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_05FF)

    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010160011V#501F怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060170124V#044F#1P那里有一张卡片……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_0676')
    def lambda_0676():
        ChrTurnDirection(0x0101, 0x0012, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0676)

    ChrTurnDirection(0x0102, 0x0012, 400)

    ChrTalk(
        0x0101,
        (
            '#0010170125V#004F啊…………！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170126V啊，果然！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6C2(): pass

    label('loc_6C2')

    ChrTalk(
        0x0102,
        (
            '#0020170127V#012F#2P……我来确认一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0102, 0x0040)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_74E',
    )

    @scena.Lambda('lambda_0705')
    def lambda_0705():
        OP_92(0x0001, 0x0012, 1000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0705)

    @scena.Lambda('lambda_071A')
    def lambda_071A():
        OP_92(0x0002, 0x0012, 2000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_071A)

    ChrWalkTo(0x0102, 12600, 0, 73400, 2000, 0x00)
    ChrTurnDirection(0x0001, 0x0012, 0)
    ChrTurnDirection(0x0002, 0x0012, 0)

    Jump('loc_83B')

    def _loc_74E(): pass

    label('loc_74E')

    If(
        (
            (Expr.PushValueByIndex, 0xB),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7C3',
    )

    @scena.Lambda('lambda_0760')
    def lambda_0760():
        ChrMoveToRelativeAsync(0x0000, -800, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0760)

    ChrMoveToRelativeAsync(0x0102, 600, 0, 0, 2000, 0x00)

    @scena.Lambda('lambda_078F')
    def lambda_078F():
        OP_92(0x0002, 0x0012, 1500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_078F)

    ChrWalkTo(0x0102, 12600, 0, 73400, 2000, 0x00)
    ChrTurnDirection(0x0000, 0x0012, 0)
    ChrTurnDirection(0x0002, 0x0012, 0)

    Jump('loc_83B')

    def _loc_7C3(): pass

    label('loc_7C3')

    If(
        (
            (Expr.PushValueByIndex, 0xC),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_83B',
    )

    @scena.Lambda('lambda_07D5')
    def lambda_07D5():
        ChrMoveToRelativeAsync(0x0000, -800, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_07D5)

    @scena.Lambda('lambda_07F0')
    def lambda_07F0():
        ChrMoveToRelativeAsync(0x0001, -200, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_07F0)

    ChrMoveToRelativeAsync(0x0102, 700, 0, 0, 2000, 0x00)
    ChrTurnDirection(0x0000, 0x0012, 0)
    ChrTurnDirection(0x0001, 0x0012, 0)
    ChrWalkTo(0x0102, 12600, 0, 73400, 2000, 0x00)

    def _loc_83B(): pass

    label('loc_83B')

    ChrClearFlags(0x0102, 0x0040)

    ExecExpressionWithValue(
        0x0012,
        0x01,
        (
            (Expr.GetChrWork, 0x102, 0x1),
            (Expr.GetChrWork, 0x101, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0012,
        0x02,
        (
            (Expr.GetChrWork, 0x102, 0x2),
            (Expr.GetChrWork, 0x101, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0012,
        0x03,
        (
            (Expr.GetChrWork, 0x102, 0x3),
            (Expr.GetChrWork, 0x101, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_0885')
    def lambda_0885():
        OP_69(0x0012, 1000)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_0885)

    ChrSetDirection(0x0102, 90, 400)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020170128V#012F…………果然没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170129V这上面贴的卡片\n',
            '和在市长官邸里看到的一样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170130V原来如此…………\n',
            '所谓的『三只眼』\n',
            '指的就是这个东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(800)

    Fade(1000)

    If(
        (
            (Expr.PushValueByIndex, 0x64),
            (Expr.PushLong, 0x2D),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_978',
    )

    OP_67(0, 4875, -10000, 0)
    CameraMove(21130, 1900, 79750, 3000)

    Jump('loc_99A')

    def _loc_978(): pass

    label('loc_978')

    OP_67(0, 4875, -10000, 0)
    CameraMove(21130, 1900, 66830, 3000)

    def _loc_99A(): pass

    label('loc_99A')

    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010170131V#501F啊，原来是这样啊。\n',
            '这样看来的确是三只眼睛呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(800)

    Fade(1000)
    OP_69(0x0012, 0)
    OP_67(0, 9500, -10000, 0)
    OP_0D()
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010170132V#002F…………\n',
            '卡片上面写的又是什么呢？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020170133V#010F嗯，来看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0102, 90, 400)
    Sleep(400)

    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '#0170170134V',
            (TxtCtl.SetColor, 0x0),
            '『啊，探寻者们。\n',
            '　如女神一般直视真实，\n',
            '　抛弃虚伪的人啊。\n',
            '　\n',
            '　前往红与黑交织的\n',
            '　无尽圆舞曲所在之处吧。\n',
            '　如是，探寻者们，\n',
            '　汝等将至苍之光所在。\n',
            '　　　　　　　　　　　怪盗Ｂ』',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010170135V#006F记录下来了，\n',
            '这样就可以确定地点了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170136V『红与黑交织的无尽\n',
            '　圆舞曲所在之处』\n',
            '…………就是这个地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060170137V#040F是红与黑……啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060170138V我没猜错的话，\n',
            '这也应该在卢安市内的某个地方吧？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0C64')
    def lambda_0C64():
        ChrTurnDirection(0x0101, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0C64)

    ChrTurnDirection(0x0102, 0x0105, 400)

    ChrTalk(
        0x0102,
        (
            '#0020170139V#010F大概是这样吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170140V犯人似乎以让别人\n',
            '去解自己设下的谜题为乐……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170141V所以应该不会破坏\n',
            '自己所定下的规则。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0D08')
    def lambda_0D08():
        ChrTurnDirection(0x0105, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_0D08)

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010170142V#009F真是个喜欢捉弄人的讨厌鬼。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170143V#006F总而言之，\n',
            '我们现在就继续展开搜索吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_64(0x00, 0x0001)
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
