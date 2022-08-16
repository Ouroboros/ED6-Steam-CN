import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5406_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5406   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5406.x'
    header.mapIndex       = 1
    header.bgm            = 28
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
        ('ED6_DT27/CH03600._CH', 'ED6_DT27/CH03600P._CP'),
        ('ED6_DT27/CH04010._CH', 'ED6_DT27/CH04010P._CP'),
        ('ED6_DT29/CH12390._CH', 'ED6_DT29/CH12390P._CP'),
        ('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT29/CH12390._CH', 'ED6_DT29/CH12390P._CP'),
        ('ED6_DT27/CH04620._CH', 'ED6_DT27/CH04620P._CP'),
        ('ED6_DT27/CH04621._CH', 'ED6_DT27/CH04621P._CP'),
        ('ED6_DT27/CH04622._CH', 'ED6_DT27/CH04622P._CP'),
        ('ED6_DT26/CH20298._CH', 'ED6_DT26/CH20298P._CP'),
        ('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT27/CH04011._CH', 'ED6_DT27/CH04011P._CP'),
        ('ED6_DT27/CH04001._CH', 'ED6_DT27/CH04001P._CP'),
    ]

# id: 0x10001 offset: 0x10A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '小丑肯帕雷拉',
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
            name                = '亡命装甲兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x01C4,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '强化猎兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '强化猎兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '强化猎兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '强化猎兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '强化猎兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '强化猎兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '强化猎兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '强化猎兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '强化猎兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '强化猎兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x28A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x28A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 1130,
            y           = 3000,
            z           = -178880,
            range       = 3000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000023,
        ),
        ScenaEventData(
            x           = -2550,
            y           = -2000,
            z           = 7130,
            range       = 4630,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00001252,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000003,
        ),
    )

# id: 0x10004 offset: 0x2CA
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x2CA
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_2E4',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    Event(0, func_0B_1F5A)

    Jump('loc_2FB')

    def _loc_2E4(): pass

    label('loc_2E4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_2FB',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    Event(0, func_22_2AAB)

    def _loc_2FB(): pass

    label('loc_2FB')

    Return()

# id: 0x0001 offset: 0x2FC
@scena.Code('func_01_2FC')
def func_01_2FC():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_31A',
    )

    ExecExpressionWithVar(
        0x3B,
        (
            (Expr.PushLong, 0x227),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x3C,
        (
            (Expr.PushLong, 0x10A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_31A(): pass

    label('loc_31A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0385, 0, 0x1C28)),
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_354',
    )

    OP_72(0x0000, 0x0008)
    OP_72(0x0000, 0x0020)
    OP_6F(0x0000, 0)
    OP_72(0x0001, 0x0008)
    OP_72(0x0001, 0x0020)
    OP_6F(0x0001, 0)
    OP_71(0x0001, 0x0004)

    Jump('loc_377')

    def _loc_354(): pass

    label('loc_354')

    OP_71(0x0000, 0x0004)
    OP_72(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_72(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    OP_72(0x0005, 0x0004)
    OP_71(0x0008, 0x0004)

    def _loc_377(): pass

    label('loc_377')

    Return()

# id: 0x0002 offset: 0x378
@scena.Code('func_02_378')
def func_02_378():
    ExecExpressionWithReg(
        0x0001,
        (
            Expr.Rand,
            (Expr.PushLong, 0xE),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_39D',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_4DF')

    def _loc_39D(): pass

    label('loc_39D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3B6',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_4DF')

    def _loc_3B6(): pass

    label('loc_3B6')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3CF',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_4DF')

    def _loc_3CF(): pass

    label('loc_3CF')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3E8',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_4DF')

    def _loc_3E8(): pass

    label('loc_3E8')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_401',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_4DF')

    def _loc_401(): pass

    label('loc_401')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_41A',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_4DF')

    def _loc_41A(): pass

    label('loc_41A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_433',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_4DF')

    def _loc_433(): pass

    label('loc_433')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_44C',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_4DF')

    def _loc_44C(): pass

    label('loc_44C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_465',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_4DF')

    def _loc_465(): pass

    label('loc_465')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_47E',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_4DF')

    def _loc_47E(): pass

    label('loc_47E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_497',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_4DF')

    def _loc_497(): pass

    label('loc_497')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4B0',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_4DF')

    def _loc_4B0(): pass

    label('loc_4B0')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4C9',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_4DF')

    def _loc_4C9(): pass

    label('loc_4C9')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4DF',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_4DF(): pass

    label('loc_4DF')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4F4',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_4DF')

    def _loc_4F4(): pass

    label('loc_4F4')

    Return()

# id: 0x0003 offset: 0x4F5
@scena.Code('func_03_4F5')
def func_03_4F5():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0385, 0, 0x1C28)),
            Expr.Ez,
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x6),
            Expr.Neq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_507',
    )

    Return()

    def _loc_507(): pass

    label('loc_507')

    Call(0, 0x0004)
    Call(0, 0x0006)

    Return()

# id: 0x0004 offset: 0x510
@scena.Code('func_04_510')
def func_04_510():
    EventBegin(0x00)
    Fade(1000)
    CameraMove(1070, -1000, 4640, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0008, 1240, -1000, 20540, 180)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0101, 1880, -1000, 4290, 0)
    ChrSetPos(0x0102, 370, -1000, 4390, 0)
    OP_0D()

    NpcTalk(
        0x0008,
        '少年的声音',
        (
            '#0190330737V#4P嘻嘻……\n',
            '动作好慢啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_0600')
    def lambda_0600():
        CameraMove(1780, -1000, 9150, 3500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0600)

    @scena.Lambda('lambda_0618')
    def lambda_0618():
        OP_67(0, 6240, -10000, 3500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0618)

    @scena.Lambda('lambda_0630')
    def lambda_0630():
        CameraSetDistance(2800, 3500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0630)

    @scena.Lambda('lambda_0640')
    def lambda_0640():
        OP_6E(323, 3500)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_0640)

    ChrWalkTo(0x0008, 1280, -1000, 12000, 2500, 0x00)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010330738V#1020F#4P你、你是……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020330739V#1032F#6P……肯帕雷拉吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0190330740V#854F#5P真是无情啊，约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190330741V只顾着和莱维叙旧，\n',
            '却连个招呼都不和我打？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020330742V#1035F#6P没想到你会\n',
            '留在飞船上……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330743V#1030F看穿我的行动了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0190330744V#851F#5P啊哈哈，别小看人啊，\n',
            '至少我也担任着监视『计划』的任务呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190330745V和其他人相比，\n',
            '关注的事情自然多了些。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020330746V#1032F#6P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0190330747V#850F#5P呵呵，话说回来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190330748V五年不见，\n',
            '你倒是变了不少呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190330749V似乎变得更有男人味了嘛～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020330750V#1031F#6P倒是你……\n',
            '完全都没有变化啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330751V外表还是和以前一模一样，\n',
            '好像完全都没有长大。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0190330752V#851F#5P哼哼哼～那是因为\n',
            '我每天都很注意皮肤的保养哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190330753V#854F你好像也经常穿女装，\n',
            '要不要我介绍点好的化妆品？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020330754V#1030F#6P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330755V#1022F#4P啊～真是的！急死人了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330756V#1005F你既然埋伏在这里，\n',
            '就是想跟我们打一架对吧！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330757V那还等什么！赶快放马过来吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0190330758V#851F啊哈哈，好有气势的女孩子呀～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190330759V#850F早就听说你是约修亚的女朋友，\n',
            '我还一直在猜想会是怎样的女孩……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190330760V看来还挺般配的嘛？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330761V#1013F#4P女、女朋友……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0190330762V#854F哟，难道说女朋友不是你，\n',
            '而是那个空贼女孩吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190330763V#851F你好受欢迎呀，约修亚㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330764V#1019F#4P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020330765V#1035F#6P……玩笑\n',
            '就到此为止吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330766V虽然我很好奇你为何\n',
            '连乔丝特的事都知道……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0102, 1)
    ChrSetSubChip(0x0102, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020330767V#1030F#6P你的战斗力\n',
            '应该和我不相上下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330768V即使这样，也一定要分个高下吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0190330769V#851F#5P啊哈哈，没那个意思啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190330770V#850F刚才也说了，\n',
            '我只是负责观察『计划』而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190330771V并没有捕捉你们\n',
            '的义务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020330772V#1032F#6P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330773V#1015F#4P哼～是这样吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330774V那你为什么还要\n',
            '埋伏在这种地方？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0190330775V#853F#5P哼哼～那当然\n',
            '是为了问候你们二位一下了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190330776V#854F不过，就这样直接说再见\n',
            '未免也太缺乏艺术性了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190330777V我只是想给你们的逃亡演出\n',
            '增加一点高潮情节而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_0EB6')
    def lambda_0EB6():
        CameraMove(1800, -1000, 11000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0EB6)

    @scena.Lambda('lambda_0ECE')
    def lambda_0ECE():
        CameraSetDistance(2500, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0ECE)

    Sleep(500)

    ChrSetFlags(0x0008, 0x0002)
    ChrSetChipByIndex(0x0008, 8)
    ChrSetSubChip(0x0008, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_99(0x0008, 0x01, 0x02, 1500)
    PlaySE(188, 0x00, 0x64)
    Sleep(500)

    OP_1F(0x5A, 0x000003E8)
    PlaySE(119, 0x00, 0x64)
    PlaySE(309, 0x01, 0x32)
    Sleep(200)

    OP_24(0x0135, 0x3C)
    Sleep(200)

    OP_24(0x0135, 0x46)
    Sleep(200)

    OP_24(0x0135, 0x50)
    Sleep(200)

    OP_24(0x0135, 0x5A)
    Sleep(200)

    OP_24(0x0135, 0x64)
    Sleep(200)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(70)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(500)

    OP_1F(0x64, 0x000003E8)

    @scena.Lambda('lambda_0F99')
    def lambda_0F99():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0F99)

    Sleep(50)

    @scena.Lambda('lambda_0FAC')
    def lambda_0FAC():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0FAC)

    LoadEffect(0x01, 'map\\\\mp003_00.eff')
    CameraMove(1160, -1000, 2460, 1500)
    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x01, 0xFF, 0x00FF, 1390, -1000, -1260, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x01, 0xFF, 0x00FF, 1050, -1000, 420, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_1058')
    def lambda_1058():
        ChrJumpTo(0x00FE, -540, -1000, 5150, 400, 5000)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_1058)

    Sleep(100)

    @scena.Lambda('lambda_107B')
    def lambda_107B():
        ChrJumpTo(0x00FE, 2980, -1000, 4880, 400, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_107B)

    ChrSetFlags(0x0101, 0x0020)
    ChrSetChipByIndex(0x0101, 9)
    ChrSetSubChip(0x0101, 0)
    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x01, 0xFF, 0x00FF, 1420, -1000, 2270, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x01, 0xFF, 0x00FF, 1100, -1000, 3760, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x01, 0xFF, 0x00FF, 1600, -1000, 5220, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x01, 0xFF, 0x00FF, 1050, -1000, 6410, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    Sleep(500)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x0008, 0x0002)
    ChrSetChipByIndex(0x0008, 0)
    ChrSetSubChip(0x0008, 0)

    @scena.Lambda('lambda_11C1')
    def lambda_11C1():
        CameraMove(6550, 890, 5910, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_11C1)

    @scena.Lambda('lambda_11D9')
    def lambda_11D9():
        OP_67(0, 3790, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_11D9)

    @scena.Lambda('lambda_11F1')
    def lambda_11F1():
        CameraSetDistance(4030, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_11F1)

    @scena.Lambda('lambda_1201')
    def lambda_1201():
        OP_6C(90000, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1201)

    @scena.Lambda('lambda_1211')
    def lambda_1211():
        OP_6E(271, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_1211)

    ChrSetPos(0x0009, 7200, 3370, -17760, 0)
    ChrClearFlags(0x0009, 0x0080)

    @scena.Lambda('lambda_1237')
    def lambda_1237():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_1237')

    DispatchAsync2(0x0009, 0x0003, lambda_1237)

    @scena.Lambda('lambda_124A')
    def lambda_124A():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_124A')

    DispatchAsync2(0x0101, 0x0000, lambda_124A)

    @scena.Lambda('lambda_125B')
    def lambda_125B():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_125B')

    DispatchAsync2(0x0102, 0x0000, lambda_125B)

    CreateThread(0x0009, 0x00, 0x00, func_05_1476)
    Sleep(3000)

    @scena.Lambda('lambda_1278')
    def lambda_1278():
        ChrSetDirection(0x00FE, 270, 100)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1278)

    WaitForThreadExit(0x0101, 0x0001)
    ChrSetChipByIndex(0x0102, 10)
    TerminateThread(0x0102, 0x00)
    ChrWalkTo(0x0102, 2440, -1000, 6560, 4000, 0x00)
    ChrSetDirection(0x0102, 90, 400)
    ChrSetChipByIndex(0x0102, 1)
    WaitForThreadExit(0x0009, 0x0000)
    TerminateThread(0x0101, 0x00)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010330778V#1020F#4P什、什、什！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020330779V#1034F#6P高机动飞行人形兵器——\n',
            '『亡命装甲兵』！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330780V已经开始量产了吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    CameraMove(7630, -1000, 9550, 0)
    OP_67(0, 3790, -10000, 0)
    CameraSetDistance(4630, 0)
    OP_6C(42000, 0)
    OP_6E(271, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0190330781V#853F#5P历尽艰辛才重逢的两人，\n',
            '又被新的障碍阻住了去路。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190330782V#854F啊啊～少年和少女的命运将会如何呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_1421')
    def lambda_1421():
        ChrMoveTo(0x00FE, 6540, 300, 5660, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_1421)

    @scena.Lambda('lambda_143C')
    def lambda_143C():
        CameraSetDistance(3270, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_143C)

    WaitForThreadExit(0x0101, 0x0002)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    Battle(0x00000429, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_1470'),
        (-1, 'loc_1475'),
    )

    def _loc_1470(): pass

    label('loc_1470')

    OP_B4(0x00)

    Jump('loc_1475')

    def _loc_1475(): pass

    label('loc_1475')

    Return()

# id: 0x0005 offset: 0x1476
@scena.Code('func_05_1476')
def func_05_1476():
    @scena.Lambda('lambda_147C')
    def lambda_147C():
        ChrMoveTo(0x00FE, 11540, 900, 5660, 11000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_147C)

    Sleep(300)

    @scena.Lambda('lambda_149C')
    def lambda_149C():
        ChrMoveTo(0x00FE, 11540, 900, 5660, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_149C)

    Sleep(300)

    @scena.Lambda('lambda_14BC')
    def lambda_14BC():
        ChrMoveTo(0x00FE, 11540, 900, 5660, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_14BC)

    Sleep(300)

    @scena.Lambda('lambda_14DC')
    def lambda_14DC():
        ChrMoveTo(0x00FE, 11540, 900, 5660, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_14DC)

    Sleep(300)

    @scena.Lambda('lambda_14FC')
    def lambda_14FC():
        ChrMoveTo(0x00FE, 11540, 900, 5660, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_14FC)

    Sleep(300)

    @scena.Lambda('lambda_151C')
    def lambda_151C():
        ChrMoveTo(0x00FE, 11540, 900, 5660, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_151C)

    Sleep(300)

    @scena.Lambda('lambda_153C')
    def lambda_153C():
        ChrMoveTo(0x00FE, 11540, 900, 5660, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_153C)

    Return()

# id: 0x0006 offset: 0x1552
@scena.Code('func_06_1552')
def func_06_1552():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    LoadChip('ED6_DT26/CH20305._CH', 'ED6_DT26/CH20305P._CP', 12)
    TerminateThread(0x0009, 0x02)
    TerminateThread(0x0008, 0x00)
    ChrSetPos(0x0008, 1280, -1000, 12000, 180)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0009, 11540, 900, 5660, 270)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0101, 2110, -1000, 3460, 90)
    ChrSetPos(0x0102, 950, -1000, 4990, 90)
    ChrSetChipByIndex(0x0101, 9)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0102, 1)
    ChrSetSubChip(0x0102, 0)
    CameraMove(6550, -400, 6000, 0)
    OP_67(0, 4950, -10000, 0)
    CameraSetDistance(2530, 0)
    OP_6C(57000, 0)
    OP_6E(365, 0)
    LoadEffect(0x02, 'battle\\btbomb00.eff')
    LoadEffect(0x03, 'map\\mp090_00.eff')
    CreateThread(0x0009, 0x03, 0x00, func_08_1D14)
    FadeIn(2000, 0)
    OP_0D()
    WaitForThreadExit(0x0009, 0x0003)
    Sleep(300)

    ChrTalk(
        0x0008,
        (
            '#0190330783V#2P啊哈哈，挺有一手嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1682')
    def lambda_1682():
        CameraMove(2270, -1000, 8930, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1682)

    @scena.Lambda('lambda_169A')
    def lambda_169A():
        OP_67(0, 6740, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_169A)

    @scena.Lambda('lambda_16B2')
    def lambda_16B2():
        CameraSetDistance(2500, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_16B2)

    @scena.Lambda('lambda_16C2')
    def lambda_16C2():
        OP_6C(45000, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_16C2)

    @scena.Lambda('lambda_16D2')
    def lambda_16D2():
        OP_6E(365, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_16D2)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#0190330784V#851F#5P约修亚也就罢了，\n',
            '没想到这位小姐的实力也很不错呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0101, 0x0020)
    ChrSetFlags(0x0102, 0x0020)

    @scena.Lambda('lambda_173C')
    def lambda_173C():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_173C)

    Sleep(100)

    ChrSetDirection(0x0102, 0, 400)
    ChrClearFlags(0x0101, 0x0020)
    ChrClearFlags(0x0102, 0x0020)
    ChrSetChipByIndex(0x0101, 11)
    ChrSetSubChip(0x0101, 0)
    ChrSetFlags(0x0101, 0x1000)
    ChrMoveTo(0x0101, 2170, -1000, 4700, 5000, 0x00)
    ChrClearFlags(0x0101, 0x1000)
    ChrSetChipByIndex(0x0101, 9)
    ChrSetSubChip(0x0101, 0)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010330785V#1005F#4P你、你这个人～……\n',
            '恶作剧也要有个限度啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0190330786V#853F#5P别生气～别生气。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190330787V#850F好了，演出结束，\n',
            '小丑该退场了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    LoadEffect(0x02, 'map\\\\mp055_00.eff')
    Sleep(200)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_1860')
    def lambda_1860():
        CameraMove(1800, -1000, 10200, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1860)

    @scena.Lambda('lambda_1878')
    def lambda_1878():
        CameraSetDistance(2300, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1878)

    Sleep(500)

    ChrSetFlags(0x0008, 0x0002)
    ChrSetChipByIndex(0x0008, 8)
    ChrSetSubChip(0x0008, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_99(0x0008, 0x01, 0x02, 1500)
    PlaySE(188, 0x00, 0x64)
    Sleep(1000)

    PlayEffect(0x02, 0x00, 0x0008, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(266, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010330788V#1020F#4P！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0008, 0x0002)
    ChrSetChipByIndex(0x0008, 12)
    ChrSetSubChip(0x0008, 0)
    OP_99(0x0008, 0x00, 0x03, 1500)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0190330789V#854F#5P哈哈哈……\n',
            '那么两位。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190330790V在不久的将来再见吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 1000)
    ChrSetFlags(0x0008, 0x0080)
    StopEffect(0x00, 0x02)
    CreateThread(0x0008, 0x03, 0x00, func_07_1CCC)
    Sleep(1500)

    @scena.Lambda('lambda_19AE')
    def lambda_19AE():
        CameraMove(2550, -1000, 7750, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_19AE)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010330791V#1020F#2P消、消失了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020330792V#1035F#6P这是幻术的一种。\n',
            '不必介意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330793V#1030F现在必须赶快──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0008, 990, -1000, -17770, 0)

    NpcTalk(
        0x0008,
        '男人的声音',
        (
            '#4210330794V#1S#1P喂！\n',
            '他们真的跑到这里了吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_20(0x000007D0)

    @scena.Lambda('lambda_1ADC')
    def lambda_1ADC():
        CameraMove(1020, -1000, -10820, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1ADC)

    @scena.Lambda('lambda_1AF4')
    def lambda_1AF4():
        ChrSetDirection(0x00FE, 180, 600)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1AF4)

    ChrSetChipByIndex(0x0102, 65535)
    ChrSetSubChip(0x0102, 0)
    Sleep(100)

    @scena.Lambda('lambda_1B11')
    def lambda_1B11():
        ChrSetDirection(0x00FE, 180, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1B11)

    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    WaitForThreadExit(0x0101, 0x0003)

    NpcTalk(
        0x0008,
        '男人的声音',
        (
            '#4220330795V#1S#1P啊啊……没错！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    PlayBGM(43)
    Sleep(500)

    Fade(500)
    CameraMove(1210, -1000, 5170, 0)
    OP_67(0, 6990, -10000, 0)
    CameraSetDistance(3090, 0)
    OP_6C(60000, 0)
    OP_6E(311, 0)
    OP_0D()
    ChrTurnDirection(0x0102, 0x0101, 600)
    Sleep(400)

    ChrTalk(
        0x0102,
        (
            '#0020330796V#1036F#6P艾丝蒂尔、赶快！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 600)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010330797V#1002F#2P嗯，嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1C14')
    def lambda_1C14():
        CameraMove(12680, -910, 27340, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1C14)

    @scena.Lambda('lambda_1C2C')
    def lambda_1C2C():
        OP_67(0, 9500, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1C2C)

    @scena.Lambda('lambda_1C44')
    def lambda_1C44():
        OP_6C(45000, 6000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_1C44)

    @scena.Lambda('lambda_1C54')
    def lambda_1C54():
        OP_6E(375, 6000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_1C54)

    CreateThread(0x0102, 0x01, 0x00, func_09_1EAC)
    Sleep(500)

    CreateThread(0x0101, 0x01, 0x00, func_0A_1F1D)
    WaitForThreadExit(0x0102, 0x0003)
    Sleep(300)

    ChrWalkTo(0x0101, 12030, -910, 26570, 5000, 0x00)
    ChrSetFlags(0x0101, 0x0080)
    OP_72(0x0000, 0x0020)
    PlaySE(253, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 119)
    OP_73(0x0000)
    FadeOut(1000, 0, -1)
    OP_0D()
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    NewScene('ED6_DT21/E0610._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0007 offset: 0x1CCC
@scena.Code('func_07_1CCC')
def func_07_1CCC():
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

# id: 0x0008 offset: 0x1D14
@scena.Code('func_08_1D14')
def func_08_1D14():
    @scena.Lambda('lambda_1D1A')
    def lambda_1D1A():
        OP_D1(0x00FE, 0, 90000, -45000, 500)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_1D1A)

    @scena.Lambda('lambda_1D34')
    def lambda_1D34():
        ChrMoveTo(0x00FE, 11540, -4000, 5660, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_1D34)

    PlayEffect(0x02, 0xFF, 0x0009, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x02, 0xFF, 0x0009, 300, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    PlayEffect(0x02, 0xFF, 0x0009, 0, 0, 300, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(400)

    PlayEffect(0x02, 0xFF, 0x0009, 100, 200, 200, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    Sleep(500)

    PlayEffect(0x02, 0xFF, 0x0009, 500, 200, 100, 0, 0, 0, 1200, 1200, 1200, 0x00FF, 0, 0, 0, 0)
    WaitForThreadExit(0x0009, 0x0000)
    PlayEffect(0x03, 0xFF, 0x0009, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    ChrSetRGBAMask(0x0009, 255, 255, 255, 0, 600)

    Return()

# id: 0x0009 offset: 0x1EAC
@scena.Code('func_09_1EAC')
def func_09_1EAC():
    ChrWalkTo(0x00FE, 600, -1000, 14960, 6000, 0x00)
    ChrWalkTo(0x00FE, 12030, -1000, 16090, 6000, 0x00)
    ChrWalkTo(0x00FE, 11910, -1150, 25050, 6000, 0x00)
    OP_72(0x0000, 0x0020)
    PlaySE(253, 0x00, 0x64)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 59)
    OP_73(0x0000)
    ChrWalkTo(0x00FE, 12030, -910, 26570, 6000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x000A offset: 0x1F1D
@scena.Code('func_0A_1F1D')
def func_0A_1F1D():
    ChrWalkTo(0x00FE, 1830, -1000, 14850, 6000, 0x00)
    ChrWalkTo(0x00FE, 12030, -1000, 16090, 6000, 0x00)
    ChrWalkTo(0x00FE, 11870, -1150, 23760, 6000, 0x00)

    Return()

# id: 0x000B offset: 0x1F5A
@scena.Code('func_0B_1F5A')
def func_0B_1F5A():
    EventBegin(0x00)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    CameraMove(12550, -1000, 29240, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(4000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_71(0x0004, 0x0004)
    OP_72(0x0000, 0x0020)
    OP_6F(0x0000, 140)
    OP_70(0x0000, 750)
    CreateThread(0x0008, 0x01, 0x00, func_0C_22F1)
    FadeIn(1000, 0)
    OP_0D()
    LoadEffect(0x01, 'map\\\\mp003_00.eff')
    LoadEffect(0x04, 'monster\\\\msc0555.eff')
    ChrSetPos(0x000A, 2200, -1000, 5060, 0)
    ChrSetPos(0x000B, 2200, -1000, 5060, 0)
    ChrSetPos(0x000C, 2200, -1000, 5060, 0)
    ChrSetPos(0x000D, 2200, -1000, 5060, 0)
    ChrSetPos(0x000E, 2200, -1000, 5060, 0)
    ChrSetPos(0x000F, 310, -1000, 4040, 0)
    ChrSetPos(0x0010, 310, -1000, 4040, 0)
    ChrSetPos(0x0011, 310, -1000, 4040, 0)
    ChrSetPos(0x0012, 310, -1000, 4040, 0)
    ChrSetPos(0x0013, 310, -1000, 4040, 0)

    @scena.Lambda('lambda_20AC')
    def lambda_20AC():
        CameraMove(9470, -1150, 23720, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_20AC)

    @scena.Lambda('lambda_20C4')
    def lambda_20C4():
        OP_67(0, 4190, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_20C4)

    @scena.Lambda('lambda_20DC')
    def lambda_20DC():
        OP_6E(360, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_20DC)

    Sleep(1500)

    CreateThread(0x000A, 0x01, 0x00, func_0E_25EC)
    CreateThread(0x000F, 0x01, 0x00, func_13_2726)
    Sleep(200)

    CreateThread(0x000B, 0x01, 0x00, func_0F_2633)
    CreateThread(0x0010, 0x01, 0x00, func_14_2768)
    Sleep(200)

    CreateThread(0x000C, 0x01, 0x00, func_10_267F)
    CreateThread(0x0011, 0x01, 0x00, func_15_27AF)
    Sleep(200)

    CreateThread(0x000D, 0x01, 0x00, func_11_26C6)
    CreateThread(0x0012, 0x01, 0x00, func_16_27DF)
    Sleep(200)

    CreateThread(0x000E, 0x01, 0x00, func_12_26F6)
    CreateThread(0x0013, 0x01, 0x00, func_17_280F)
    WaitForThreadExit(0x0013, 0x0001)
    WaitForThreadExit(0x0101, 0x0003)
    Sleep(1000)

    ChrTalk(
        0x000F,
        (
            '#4240330808V#5P可、可恶……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#4210330809V#5P发射！\n',
            '绝对不能让他们逃走！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_21AD')
    def lambda_21AD():
        CameraMove(9390, -1000, 24480, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_21AD)

    @scena.Lambda('lambda_21C5')
    def lambda_21C5():
        OP_67(0, 6620, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_21C5)

    @scena.Lambda('lambda_21DD')
    def lambda_21DD():
        OP_6E(338, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_21DD)

    CreateThread(0x000A, 0x01, 0x00, func_18_283F)
    CreateThread(0x000F, 0x01, 0x00, func_1D_299D)
    Sleep(100)

    CreateThread(0x000B, 0x01, 0x00, func_19_2885)
    CreateThread(0x0010, 0x01, 0x00, func_1E_29CF)
    Sleep(100)

    CreateThread(0x000C, 0x01, 0x00, func_1A_28D0)
    CreateThread(0x0011, 0x01, 0x00, func_1F_2A06)
    Sleep(100)

    CreateThread(0x000D, 0x01, 0x00, func_1B_291B)
    CreateThread(0x0012, 0x01, 0x00, func_20_2A3D)
    Sleep(100)

    CreateThread(0x000E, 0x01, 0x00, func_1C_2966)
    CreateThread(0x0013, 0x01, 0x00, func_21_2A74)
    WaitForThreadExit(0x0101, 0x0003)
    Sleep(2000)

    OP_73(0x0000)
    OP_6F(0x0000, 750)
    OP_70(0x0000, 840)
    PlaySE(310, 0x00, 0x64)
    OP_73(0x0000)
    Sleep(500)

    OP_6F(0x0000, 840)
    OP_70(0x0000, 980)
    PlaySE(310, 0x00, 0x64)
    Sleep(1000)

    FadeOut(1000, 0, -1)
    TerminateThread(0x000A, 0x01)
    Sleep(100)

    TerminateThread(0x000B, 0x01)
    Sleep(100)

    TerminateThread(0x000C, 0x01)
    Sleep(100)

    TerminateThread(0x000D, 0x01)
    Sleep(100)

    TerminateThread(0x000E, 0x01)
    Sleep(100)

    TerminateThread(0x000F, 0x01)
    Sleep(100)

    TerminateThread(0x0010, 0x01)
    Sleep(100)

    TerminateThread(0x0011, 0x01)
    Sleep(100)

    TerminateThread(0x0012, 0x01)
    Sleep(100)

    TerminateThread(0x0013, 0x01)
    OP_73(0x0000)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    NewScene('ED6_DT21/E0610._SN', 102, 0, 0)
    IdleLoop()

    Return()

# id: 0x000C offset: 0x22F1
@scena.Code('func_0C_22F1')
def func_0C_22F1():
    Sleep(500)

    PlaySE(307, 0x00, 0x64)
    Sleep(4500)

    PlaySE(307, 0x00, 0x64)
    Sleep(5000)

    Return()

# id: 0x000D offset: 0x230B
@scena.Code('func_0D_230B')
def func_0D_230B():
    ChrSetChipByIndex(0x00FE, 7)
    ChrSetSubChip(0x00FE, 0)
    def _loc_2315(): pass

    label('loc_2315')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_25EB',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            Expr.Rand,
            (Expr.PushLong, 0xC),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_23B7',
    )

    Sleep(400)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x04, 0xFF, 0x00FE, 0, 500, 1000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_99(0x00FE, 0x00, 0x07, 2000)
    PlayEffect(0x01, 0xFF, 0x00FF, 9790, -1300, 27370, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    Jump('loc_25E8')

    def _loc_23B7(): pass

    label('loc_23B7')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2444',
    )

    Sleep(500)

    PlayEffect(0x04, 0xFF, 0x00FE, 0, 500, 1000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(503, 0x00, 0x64)
    OP_99(0x00FE, 0x00, 0x07, 2000)
    PlayEffect(0x01, 0xFF, 0x00FF, 9870, -1200, 29300, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    Jump('loc_25E8')

    def _loc_2444(): pass

    label('loc_2444')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_24D1',
    )

    Sleep(600)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x04, 0xFF, 0x00FE, 0, 500, 1000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_99(0x00FE, 0x00, 0x07, 2000)
    PlayEffect(0x01, 0xFF, 0x00FF, 9840, 2500, 27360, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    Jump('loc_25E8')

    def _loc_24D1(): pass

    label('loc_24D1')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_255E',
    )

    Sleep(700)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x04, 0xFF, 0x00FE, 0, 500, 1000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_99(0x00FE, 0x00, 0x07, 2000)
    PlayEffect(0x01, 0xFF, 0x00FF, 10850, 2500, 25410, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    Jump('loc_25E8')

    def _loc_255E(): pass

    label('loc_255E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_25E8',
    )

    Sleep(800)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x04, 0xFF, 0x00FE, 0, 500, 1000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_99(0x00FE, 0x00, 0x07, 2000)
    PlayEffect(0x01, 0xFF, 0x00FF, 10920, -1150, 25380, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    def _loc_25E8(): pass

    label('loc_25E8')

    Jump('loc_2315')

    def _loc_25EB(): pass

    label('loc_25EB')

    Return()

# id: 0x000E offset: 0x25EC
@scena.Code('func_0E_25EC')
def func_0E_25EC():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetChipByIndex(0x00FE, 6)
    ChrWalkTo(0x00FE, 2430, -1000, 15470, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 5)
    ChrSetDirection(0x00FE, 45, 400)
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    Return()

# id: 0x000F offset: 0x2633
@scena.Code('func_0F_2633')
def func_0F_2633():
    Sleep(50)

    ChrClearFlags(0x00FE, 0x0080)
    ChrSetChipByIndex(0x00FE, 6)
    ChrWalkTo(0x00FE, 3010, -1000, 14200, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 5)
    ChrSetDirection(0x00FE, 45, 400)
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    Return()

# id: 0x0010 offset: 0x267F
@scena.Code('func_10_267F')
def func_10_267F():
    Sleep(70)

    ChrClearFlags(0x00FE, 0x0080)
    ChrSetChipByIndex(0x00FE, 6)
    ChrWalkTo(0x00FE, 1940, -1000, 12800, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 5)
    ChrSetDirection(0x00FE, 45, 400)
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Return()

# id: 0x0011 offset: 0x26C6
@scena.Code('func_11_26C6')
def func_11_26C6():
    Sleep(100)

    ChrClearFlags(0x00FE, 0x0080)
    ChrSetChipByIndex(0x00FE, 6)
    ChrWalkTo(0x00FE, 2190, -1000, 11260, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 5)
    ChrSetDirection(0x00FE, 45, 400)

    Return()

# id: 0x0012 offset: 0x26F6
@scena.Code('func_12_26F6')
def func_12_26F6():
    Sleep(120)

    ChrClearFlags(0x00FE, 0x0080)
    ChrSetChipByIndex(0x00FE, 6)
    ChrWalkTo(0x00FE, 1750, -1000, 9500, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 5)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0013 offset: 0x2726
@scena.Code('func_13_2726')
def func_13_2726():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetChipByIndex(0x00FE, 6)
    ChrWalkTo(0x00FE, 740, -1000, 15110, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 5)
    ChrSetDirection(0x00FE, 45, 400)
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Return()

# id: 0x0014 offset: 0x2768
@scena.Code('func_14_2768')
def func_14_2768():
    Sleep(50)

    ChrClearFlags(0x00FE, 0x0080)
    ChrSetChipByIndex(0x00FE, 6)
    ChrWalkTo(0x00FE, 310, -1000, 13480, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 5)
    ChrSetDirection(0x00FE, 45, 400)
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Return()

# id: 0x0015 offset: 0x27AF
@scena.Code('func_15_27AF')
def func_15_27AF():
    Sleep(70)

    ChrClearFlags(0x00FE, 0x0080)
    ChrSetChipByIndex(0x00FE, 6)
    ChrWalkTo(0x00FE, -540, -1000, 11810, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 5)
    ChrSetDirection(0x00FE, 45, 400)

    Return()

# id: 0x0016 offset: 0x27DF
@scena.Code('func_16_27DF')
def func_16_27DF():
    Sleep(100)

    ChrClearFlags(0x00FE, 0x0080)
    ChrSetChipByIndex(0x00FE, 6)
    ChrWalkTo(0x00FE, 250, -1000, 10760, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 5)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0017 offset: 0x280F
@scena.Code('func_17_280F')
def func_17_280F():
    Sleep(120)

    ChrClearFlags(0x00FE, 0x0080)
    ChrSetChipByIndex(0x00FE, 6)
    ChrWalkTo(0x00FE, -170, -1000, 9280, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 5)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0018 offset: 0x283F
@scena.Code('func_18_283F')
def func_18_283F():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetChipByIndex(0x00FE, 6)
    ChrWalkTo(0x00FE, 4090, -1000, 16079, 5000, 0x00)
    ChrWalkTo(0x00FE, 9080, -1000, 16200, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 5)
    ChrSetDirection(0x00FE, 0, 400)
    CreateThread(0x000A, 0x01, 0x00, func_0D_230B)

    Return()

# id: 0x0019 offset: 0x2885
@scena.Code('func_19_2885')
def func_19_2885():
    Sleep(50)

    ChrClearFlags(0x00FE, 0x0080)
    ChrSetChipByIndex(0x00FE, 6)
    ChrWalkTo(0x00FE, 4090, -1000, 16079, 5000, 0x00)
    ChrWalkTo(0x00FE, 7910, -1000, 16690, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 5)
    ChrSetDirection(0x00FE, 0, 400)
    CreateThread(0x000B, 0x01, 0x00, func_0D_230B)

    Return()

# id: 0x001A offset: 0x28D0
@scena.Code('func_1A_28D0')
def func_1A_28D0():
    Sleep(70)

    ChrClearFlags(0x00FE, 0x0080)
    ChrSetChipByIndex(0x00FE, 6)
    ChrWalkTo(0x00FE, 4090, -1000, 16079, 5000, 0x00)
    ChrWalkTo(0x00FE, 6560, -1000, 16950, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 5)
    ChrSetDirection(0x00FE, 0, 400)
    CreateThread(0x000C, 0x01, 0x00, func_0D_230B)

    Return()

# id: 0x001B offset: 0x291B
@scena.Code('func_1B_291B')
def func_1B_291B():
    Sleep(100)

    ChrClearFlags(0x00FE, 0x0080)
    ChrSetChipByIndex(0x00FE, 6)
    ChrWalkTo(0x00FE, 4090, -1000, 16079, 5000, 0x00)
    ChrWalkTo(0x00FE, 4740, -1000, 16309, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 5)
    ChrSetDirection(0x00FE, 45, 400)
    CreateThread(0x000D, 0x01, 0x00, func_0D_230B)

    Return()

# id: 0x001C offset: 0x2966
@scena.Code('func_1C_2966')
def func_1C_2966():
    Sleep(120)

    ChrClearFlags(0x00FE, 0x0080)
    ChrSetChipByIndex(0x00FE, 6)
    ChrWalkTo(0x00FE, 3660, -1000, 16880, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 5)
    ChrSetDirection(0x00FE, 45, 400)
    CreateThread(0x000E, 0x01, 0x00, func_0D_230B)

    Return()

# id: 0x001D offset: 0x299D
@scena.Code('func_1D_299D')
def func_1D_299D():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetChipByIndex(0x00FE, 6)
    ChrWalkTo(0x00FE, 2250, -1000, 21720, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 5)
    ChrSetDirection(0x00FE, 45, 400)
    CreateThread(0x000F, 0x01, 0x00, func_0D_230B)

    Return()

# id: 0x001E offset: 0x29CF
@scena.Code('func_1E_29CF')
def func_1E_29CF():
    Sleep(50)

    ChrClearFlags(0x00FE, 0x0080)
    ChrSetChipByIndex(0x00FE, 6)
    ChrWalkTo(0x00FE, 1870, -1000, 20380, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 5)
    ChrSetDirection(0x00FE, 45, 400)
    CreateThread(0x0010, 0x01, 0x00, func_0D_230B)

    Return()

# id: 0x001F offset: 0x2A06
@scena.Code('func_1F_2A06')
def func_1F_2A06():
    Sleep(70)

    ChrClearFlags(0x00FE, 0x0080)
    ChrSetChipByIndex(0x00FE, 6)
    ChrWalkTo(0x00FE, 2840, -1000, 19970, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 5)
    ChrSetDirection(0x00FE, 45, 400)
    CreateThread(0x0011, 0x01, 0x00, func_0D_230B)

    Return()

# id: 0x0020 offset: 0x2A3D
@scena.Code('func_20_2A3D')
def func_20_2A3D():
    Sleep(100)

    ChrClearFlags(0x00FE, 0x0080)
    ChrSetChipByIndex(0x00FE, 6)
    ChrWalkTo(0x00FE, 1830, -1000, 18100, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 5)
    ChrSetDirection(0x00FE, 45, 400)
    CreateThread(0x0012, 0x01, 0x00, func_0D_230B)

    Return()

# id: 0x0021 offset: 0x2A74
@scena.Code('func_21_2A74')
def func_21_2A74():
    Sleep(120)

    ChrClearFlags(0x00FE, 0x0080)
    ChrSetChipByIndex(0x00FE, 6)
    ChrWalkTo(0x00FE, 2920, -1000, 17940, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 5)
    ChrSetDirection(0x00FE, 45, 400)
    CreateThread(0x0013, 0x01, 0x00, func_0D_230B)

    Return()

# id: 0x0022 offset: 0x2AAB
@scena.Code('func_22_2AAB')
def func_22_2AAB():
    EventBegin(0x00)
    OP_72(0x0000, 0x0004)
    OP_71(0x0004, 0x0004)
    OP_71(0x0000, 0x0020)
    OP_72(0x0000, 0x0008)
    OP_6F(0x0000, 980)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrSetPos(0x000A, 9080, -1000, 16200, 0)
    ChrSetPos(0x000B, 7910, -1000, 16690, 0)
    ChrSetPos(0x000C, 6560, -1000, 16950, 0)
    ChrSetPos(0x000D, 4740, -1000, 16309, 45)
    ChrSetPos(0x000E, 3660, -1000, 16880, 45)
    ChrSetPos(0x000F, 2250, -1000, 21720, 45)
    ChrSetPos(0x0010, 1870, -1000, 20380, 45)
    ChrSetPos(0x0011, 2840, -1000, 19970, 45)
    ChrSetPos(0x0012, 1830, -1000, 18100, 45)
    ChrSetPos(0x0013, 2920, -1000, 17940, 45)
    CameraMove(6900, -1000, 20600, 0)
    OP_67(0, 6420, -10000, 0)
    CameraSetDistance(3820, 0)
    OP_6C(45000, 0)
    OP_6E(248, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x000F,
        (
            '#4240330813V#5P唔……\n',
            '别想就这么逃跑！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#4210330814V#5P我们也乘飞艇出动！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    NewScene('ED6_DT21/C5408._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0023 offset: 0x2C65
@scena.Code('func_23_2C65')
def func_23_2C65():
    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
