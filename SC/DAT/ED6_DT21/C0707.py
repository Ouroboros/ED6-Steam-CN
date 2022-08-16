import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C0707_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C0707   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0707.x'
    header.mapIndex       = 1
    header.bgm            = 10
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
        ('ED6_DT27/CH03530._CH', 'ED6_DT27/CH03530P._CP'),
        ('ED6_DT27/CH04530._CH', 'ED6_DT27/CH04530P._CP'),
        ('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT27/CH04001._CH', 'ED6_DT27/CH04001P._CP'),
        ('ED6_DT27/CH04010._CH', 'ED6_DT27/CH04010P._CP'),
        ('ED6_DT27/CH04011._CH', 'ED6_DT27/CH04011P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
    ]

# id: 0x10001 offset: 0xE2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '怪盗布卢布兰',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '福音',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 458758,
            chipIndex           = 6,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x122
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x122
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x122
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x122
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_13E',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x51),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_02_140)

    def _loc_13E(): pass

    label('loc_13E')

    Return()

# id: 0x0001 offset: 0x13F
@scena.Code('func_01_13F')
def func_01_13F():
    Return()

# id: 0x0002 offset: 0x140
@scena.Code('func_02_140')
def func_02_140():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_157',
    )

    Call(0, 0x0006)
    Call(0, 0x0007)

    def _loc_157(): pass

    label('loc_157')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_178'),
        (0x00000005, 'loc_185'),
        (0x00000004, 'loc_192'),
        (0x00000006, 'loc_19F'),
        (0x00000007, 'loc_1AC'),
        (0x00000008, 'loc_1B9'),
        (-1, 'loc_1C6'),
    )

    def _loc_178(): pass

    label('loc_178')

    LoadChip('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP', 7)

    Jump('loc_1C6')

    def _loc_185(): pass

    label('loc_185')

    LoadChip('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP', 7)

    Jump('loc_1C6')

    def _loc_192(): pass

    label('loc_192')

    LoadChip('ED6_DT07/CH00140._CH', 'ED6_DT07/CH00140P._CP', 7)

    Jump('loc_1C6')

    def _loc_19F(): pass

    label('loc_19F')

    LoadChip('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP', 7)

    Jump('loc_1C6')

    def _loc_1AC(): pass

    label('loc_1AC')

    LoadChip('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP', 7)

    Jump('loc_1C6')

    def _loc_1B9(): pass

    label('loc_1B9')

    LoadChip('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP', 7)

    Jump('loc_1C6')

    def _loc_1C6(): pass

    label('loc_1C6')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_1E7'),
        (0x00000005, 'loc_1F4'),
        (0x00000004, 'loc_201'),
        (0x00000006, 'loc_20E'),
        (0x00000007, 'loc_21B'),
        (0x00000008, 'loc_228'),
        (-1, 'loc_235'),
    )

    def _loc_1E7(): pass

    label('loc_1E7')

    LoadChip('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP', 9)

    Jump('loc_235')

    def _loc_1F4(): pass

    label('loc_1F4')

    LoadChip('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP', 9)

    Jump('loc_235')

    def _loc_201(): pass

    label('loc_201')

    LoadChip('ED6_DT07/CH00140._CH', 'ED6_DT07/CH00140P._CP', 9)

    Jump('loc_235')

    def _loc_20E(): pass

    label('loc_20E')

    LoadChip('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP', 9)

    Jump('loc_235')

    def _loc_21B(): pass

    label('loc_21B')

    LoadChip('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP', 9)

    Jump('loc_235')

    def _loc_228(): pass

    label('loc_228')

    LoadChip('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP', 9)

    Jump('loc_235')

    def _loc_235(): pass

    label('loc_235')

    LoadChip('ED6_DT27/CH04538._CH', 'ED6_DT27/CH04538P._CP', 11)
    CameraMove(34920, 250, 12030, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3960, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    PlaySE(451, 0x00, 0x64)
    ChrSetPos(0x0008, 700, 950, 12150, 90)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 1)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0101, 2)
    ChrSetSubChip(0x0102, 0)
    ChrSetChipByIndex(0x0102, 4)
    ChrSetSubChip(0x00F8, 0)
    ChrSetChipByIndex(0x00F8, 7)
    ChrSetSubChip(0x00F9, 0)
    ChrSetChipByIndex(0x00F9, 9)
    ChrSetPos(0x0101, -700, 0, 4650, 90)
    ChrSetPos(0x0102, 700, 0, 4520, 90)
    ChrSetPos(0x00F8, -800, 0, 2930, 90)
    ChrSetPos(0x00F9, 800, 0, 2800, 90)
    LoadEffect(0x00, 'map\\\\mp046_00.eff')
    StopEffect(0x80, 0x00)
    StopEffect(0x82, 0x00)
    OP_72(0x0006, 0x0004)
    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    OP_79(0x00, 0x0002)
    OP_79(0x01, 0x0002)
    OP_79(0x02, 0x0002)
    OP_79(0x03, 0x0002)
    OP_79(0x04, 0x0002)
    OP_7B()
    FadeIn(1000, 0)

    @scena.Lambda('lambda_0369')
    def lambda_0369():
        CameraMove(1840, 0, 7670, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0369)

    @scena.Lambda('lambda_0381')
    def lambda_0381():
        OP_67(0, 5560, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0381)

    @scena.Lambda('lambda_0399')
    def lambda_0399():
        CameraSetDistance(4800, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0399)

    WaitForThreadExit(0x0101, 0x0000)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010340843V#1025F#6P啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_410',
    )

    ChrTalk(
        0x0109,
        (
            '#0180340844V#1062F#6P恢复原状了吗……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_509')

    def _loc_410(): pass

    label('loc_410')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_451',
    )

    ChrTalk(
        0x0105,
        (
            '#0060340845V#542F#6P恢、恢复原状了……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_509')

    def _loc_451(): pass

    label('loc_451')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_490',
    )

    ChrTalk(
        0x0103,
        (
            '#0030340846V#027F#6P恢复原状了吗……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_509')

    def _loc_490(): pass

    label('loc_490')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4CD',
    )

    ChrTalk(
        0x0108,
        (
            '#0080340847V#070F#6P恢复原状了吗……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_509')

    def _loc_4CD(): pass

    label('loc_4CD')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_509',
    )

    ChrTalk(
        0x0106,
        (
            '#0050340848V#051F#6P恢复原状了吗……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_509(): pass

    label('loc_509')

    ChrTalk(
        0x0008,
        (
            '#0170340849V#230F#6P唔，看来任务\n',
            '到此结束了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170340850V……没办法了。\n',
            '撤退吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 0, 400)

    @scena.Lambda('lambda_0570')
    def lambda_0570():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0570)

    Sleep(50)

    @scena.Lambda('lambda_0583')
    def lambda_0583():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_0583)

    Sleep(50)

    @scena.Lambda('lambda_0596')
    def lambda_0596():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_0596)

    Sleep(50)

    ChrTalk(
        0x0101,
        (
            '#0010340851V#1004F#6P什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_05CC')
    def lambda_05CC():
        CameraMove(1500, 0, 9790, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_05CC)

    @scena.Lambda('lambda_05E4')
    def lambda_05E4():
        OP_67(0, 5000, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_05E4)

    @scena.Lambda('lambda_05FC')
    def lambda_05FC():
        CameraSetDistance(4220, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_05FC)

    ChrSetDirection(0x0008, 180, 400)
    Sleep(500)

    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 11)
    OP_99(0x0008, 0x00, 0x05, 2000)
    PlayEffect(0x00, 0x00, 0x0008, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(266, 0x00, 0x64)
    Sleep(1000)

    WaitForThreadExit(0x0101, 0x0001)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6C8',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_706')

    def _loc_6C8(): pass

    label('loc_6C8')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6EF',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_706')

    def _loc_6EF(): pass

    label('loc_6EF')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_706(): pass

    label('loc_706')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_732',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_770')

    def _loc_732(): pass

    label('loc_732')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_759',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_770')

    def _loc_759(): pass

    label('loc_759')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_770(): pass

    label('loc_770')

    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010340852V#1005F#6P慢、慢着！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7D3',
    )

    ChrTalk(
        0x0105,
        (
            '#0060340853V#043F#4P等、等一下！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8B4')

    def _loc_7D3(): pass

    label('loc_7D3')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_813',
    )

    ChrTalk(
        0x0106,
        (
            '#0050340854V#054F#4P你小子……\n',
            '想逃吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8B4')

    def _loc_813(): pass

    label('loc_813')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_84D',
    )

    ChrTalk(
        0x0109,
        (
            '#0180340855V#1069F#4P喂、想逃吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8B4')

    def _loc_84D(): pass

    label('loc_84D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_882',
    )

    ChrTalk(
        0x0103,
        (
            '#0030340856V#024F#4P想逃吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8B4')

    def _loc_882(): pass

    label('loc_882')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8B4',
    )

    ChrTalk(
        0x0108,
        (
            '#0080340857V#076F#4P想逃吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8B4(): pass

    label('loc_8B4')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_973',
    )

    ChrTalk(
        0x0008,
        (
            '#0170340858V#231F#5P哈哈，殿下自不必说\n',
            '诸位游击士作战的模样\n',
            '真让我感动啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170340859V至于这是否真实，\n',
            '就留待下次见面时再确认吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170340860V#230F那么诸位，失陪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A26')

    def _loc_973(): pass

    label('loc_973')

    ChrTalk(
        0x0008,
        (
            '#0170340861V#231F#5P哈哈，『漆黑之牙』自不必说，\n',
            '诸位游击士也相当有本事嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170340862V至于那个光辉是否真实，\n',
            '等下次有机会我再确认吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170340860V#230F那么诸位，失陪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A26(): pass

    label('loc_A26')

    OP_99(0x0008, 0x05, 0x0E, 2000)
    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 2000)
    ChrSetFlags(0x0008, 0x0080)
    StopEffect(0x00, 0x02)
    CreateThread(0x0008, 0x03, 0x00, func_05_11D9)
    Sleep(3500)

    ChrTalk(
        0x0101,
        (
            '#0010340864V#1019F#6P逃、逃掉了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340865V#1042F#4P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x00F8, 65535)
    ChrSetChipByIndex(0x00F9, 65535)
    OP_0D()

    @scena.Lambda('lambda_0ACD')
    def lambda_0ACD():
        ChrWalkTo(0x00FE, 220, 950, 12120, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0ACD)

    @scena.Lambda('lambda_0AE8')
    def lambda_0AE8():
        CameraMove(0, 950, 13850, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0AE8)

    @scena.Lambda('lambda_0B00')
    def lambda_0B00():
        OP_67(0, 6500, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0B00)

    @scena.Lambda('lambda_0B18')
    def lambda_0B18():
        CameraSetDistance(3200, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0B18)

    @scena.Lambda('lambda_0B28')
    def lambda_0B28():
        OP_6C(45000, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_0B28)

    @scena.Lambda('lambda_0B38')
    def lambda_0B38():
        OP_6E(262, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_0B38)

    Sleep(200)

    @scena.Lambda('lambda_0B4D')
    def lambda_0B4D():
        ChrWalkTo(0x00FE, -1120, 950, 12020, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0B4D)

    Sleep(200)

    CreateThread(0x00F9, 0x01, 0x00, func_04_11C4)
    Sleep(200)

    CreateThread(0x00F8, 0x01, 0x00, func_03_11AF)
    WaitForThreadExit(0x00F9, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020340866V#1043F#4P这就是『β』……\n',
            '结社制作的『福音』的最终形态吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020340867V比至今为止的新型号\n',
            '好像还大一圈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340868V#1002F#6P塔顶上\n',
            '恢复了原状是不错，不过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010340869V问题是他们到底想\n',
            '使用这个来做什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CD7',
    )

    ChrTalk(
        0x0108,
        (
            '#0080340870V#072F#4P之前启动的装置\n',
            '好像也再度停了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080340871V#572F……糟糕透了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EA4')

    def _loc_CD7(): pass

    label('loc_CD7')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D44',
    )

    ChrTalk(
        0x0106,
        (
            '#0050340872V#552F#4P之前启动的装置\n',
            '好像也再度停止了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050340873V#053F……真是糟糕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EA4')

    def _loc_D44(): pass

    label('loc_D44')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DBB',
    )

    ChrTalk(
        0x0109,
        (
            '#0180340874V#1063F#4P之前启动的装置\n',
            '好像也再度停止了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180340875V#1068F总觉得有不好～的预感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EA4')

    def _loc_DBB(): pass

    label('loc_DBB')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E32',
    )

    ChrTalk(
        0x0103,
        (
            '#0030340876V#022F#4P之前启动的装置\n',
            '也再度停止了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030340877V#522F……总觉得有一种不祥的预感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EA4')

    def _loc_E32(): pass

    label('loc_E32')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_EA4',
    )

    ChrTalk(
        0x0107,
        (
            '#0070340878V#561F#4P之前启动的装置\n',
            '好像也再度停了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070340879V#063F总觉得有不好的预感……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EA4(): pass

    label('loc_EA4')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F0C',
    )

    ChrTalk(
        0x0105,
        (
            '#0060340880V#043F#4P而且，刚才\n',
            '笼罩着塔顶的结界……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060340881V那到底是什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10A9')

    def _loc_F0C(): pass

    label('loc_F0C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F74',
    )

    ChrTalk(
        0x0107,
        (
            '#0070340882V#065F#4P而、而且……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070340883V刚才笼罩着塔顶的\n',
            '结界到底是什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10A9')

    def _loc_F74(): pass

    label('loc_F74')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_FD9',
    )

    ChrTalk(
        0x0103,
        (
            '#0030340884V#522F而且，刚才\n',
            '笼罩着塔顶的结界……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030340885V那到底是什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10A9')

    def _loc_FD9(): pass

    label('loc_FD9')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_103F',
    )

    ChrTalk(
        0x0109,
        (
            '#0180340886V#1067F而且，刚才\n',
            '笼罩着塔顶的结界……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180340887V那到底是什么啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10A9')

    def _loc_103F(): pass

    label('loc_103F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_10A9',
    )

    ChrTalk(
        0x0106,
        (
            '#0050340888V#555F而且，刚才笼罩着\n',
            '塔顶的结界也让人很在意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050340889V那到底是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10A9(): pass

    label('loc_10A9')

    ChrTalk(
        0x0102,
        (
            '#0020340890V#1043F#4P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0102, 270, 400)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020340891V#1040F#2P总之这样一来，\n',
            '这座塔应该就恢复原状了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020340892V暂且先返回『埃尔赛尤』吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010340893V#1025F#6P嗯……\n',
            '得回去向博士报告才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    OP_20(0x000007D0)
    OP_21()
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    NewScene('ED6_DT21/E0311._SN', 103, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x11AF
@scena.Code('func_03_11AF')
def func_03_11AF():
    ChrWalkTo(0x00FE, -1100, 250, 11080, 3000, 0x00)

    Return()

# id: 0x0004 offset: 0x11C4
@scena.Code('func_04_11C4')
def func_04_11C4():
    ChrWalkTo(0x00FE, 380, 500, 11150, 3000, 0x00)

    Return()

# id: 0x0005 offset: 0x11D9
@scena.Code('func_05_11D9')
def func_05_11D9():
    Sleep(300)

    OP_24(0x010A, 0x5A)
    Sleep(300)

    OP_24(0x010A, 0x50)
    Sleep(300)

    OP_24(0x010A, 0x46)
    Sleep(300)

    OP_24(0x010A, 0x3C)
    Sleep(300)

    OP_24(0x010A, 0x32)
    Sleep(300)

    OP_24(0x010A, 0x28)
    Sleep(300)

    OP_24(0x010A, 0x1E)
    Sleep(300)

    OP_23(0x010A)

    Return()

# id: 0x0006 offset: 0x1221
@scena.Code('func_06_1221')
def func_06_1221():
    FadeOut(0, 0, -1)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)

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
        (0x00000000, 'loc_129B'),
        (0x00000001, 'loc_12A1'),
        (-1, 'loc_12A7'),
    )

    def _loc_129B(): pass

    label('loc_129B')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_12A7')

    def _loc_12A1(): pass

    label('loc_12A1')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_12A7')

    def _loc_12A7(): pass

    label('loc_12A7')

    Return()

# id: 0x0007 offset: 0x12A8
@scena.Code('func_07_12A8')
def func_07_12A8():
    FadeOut(0, 0, -1)
    CameraMove(-66940, 250, 36210, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(3700, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['雪拉扎德'],
            ChrTable['提妲'],
            ChrTable['科洛丝'],
            ChrTable['金'],
            ChrTable['凯文神父'],
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

    Sleep(100)

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
