import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C3607_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C3607   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'C3607.x'
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
        ('ED6_DT27/CH03500._CH', 'ED6_DT27/CH03500P._CP'),
        ('ED6_DT07/CH02610._CH', 'ED6_DT07/CH02610P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
        ('ED6_DT26/CH20242._CH', 'ED6_DT26/CH20242P._CP'),
        ('ED6_DT26/CH20280._CH', 'ED6_DT26/CH20280P._CP'),
        ('ED6_DT29/CH12140._CH', 'ED6_DT29/CH12140P._CP'),
        ('ED6_DT29/CH12141._CH', 'ED6_DT29/CH12141P._CP'),
    ]

# id: 0x10001 offset: 0xE2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '瘦狼瓦鲁特',
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
            name                = '雾香',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '福音',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 458754,
            chipIndex           = 2,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x142
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = 9600,
            z           = 250,
            y           = 1400,
            word_0C     = 0x010E,
            word_0E     = 0x0005,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01F5,
            word_18     = 0x2100,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x15E
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x15E
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x15E
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_16C',
    )

    OP_B5(0x00)

    def _loc_16C(): pass

    label('loc_16C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0420, 0, 0x2100)),
            Expr.Return,
        ),
        'loc_178',
    )

    ChrSetFlags(0x000B, 0x0080)

    def _loc_178(): pass

    label('loc_178')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_194',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x50),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_02_23A)

    def _loc_194(): pass

    label('loc_194')

    Return()

# id: 0x0001 offset: 0x195
@scena.Code('func_01_195')
def func_01_195():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1E3',
    )

    OP_72(0x0008, 0x0004)
    StopEffect(0x80, 0x00)
    StopEffect(0x81, 0x00)
    StopEffect(0x82, 0x00)
    StopEffect(0x83, 0x00)
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

    Jump('loc_21D')

    def _loc_1E3(): pass

    label('loc_1E3')

    StopEffect(0x80, 0x00)
    StopEffect(0x81, 0x00)
    StopEffect(0x82, 0x00)
    StopEffect(0x83, 0x00)
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

    def _loc_21D(): pass

    label('loc_21D')

    ExecExpressionWithValue(
        0x000B,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_239',
    )

    PlaySE(451, 0x00, 0x64)

    def _loc_239(): pass

    label('loc_239')

    Return()

# id: 0x0002 offset: 0x23A
@scena.Code('func_02_23A')
def func_02_23A():
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
        'loc_251',
    )

    Call(0, 0x0006)
    Call(0, 0x0007)

    def _loc_251(): pass

    label('loc_251')

    CameraMove(34920, 250, 12030, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3960, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    PlaySE(451, 0x00, 0x64)
    ChrSetPos(0x0008, -2540, 250, 9040, 90)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetChipByIndex(0x0008, 4)
    ChrSetSubChip(0x0008, 0)
    ChrSetPos(0x0009, 40, 0, 6000, 90)
    ChrClearFlags(0x0009, 0x0080)
    StopEffect(0x80, 0x00)
    StopEffect(0x82, 0x00)
    ChrSetPos(0x0108, 2730, 250, 8740, 90)
    ChrSetPos(0x0101, 200, 0, 2110, 90)
    ChrSetPos(0x0102, 1000, 0, 1470, 90)
    ChrSetPos(0x00F9, -800, 0, 1110, 90)
    OP_72(0x0007, 0x0004)
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

    @scena.Lambda('lambda_034C')
    def lambda_034C():
        CameraMove(1840, 0, 7670, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_034C)

    @scena.Lambda('lambda_0364')
    def lambda_0364():
        OP_67(0, 5560, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0364)

    @scena.Lambda('lambda_037C')
    def lambda_037C():
        CameraSetDistance(4800, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_037C)

    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    WaitForThreadExit(0x0101, 0x0000)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0200341162V#252F嘻嘻……\n',
            '此次的任务完成了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0008, 0x0020)
    ChrTurnDirection(0x0008, 0x0009, 400)
    ChrClearFlags(0x0008, 0x0020)

    @scena.Lambda('lambda_03EA')
    def lambda_03EA():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_03EA')

    DispatchAsync2(0x0009, 0x0001, lambda_03EA)

    Sleep(50)

    @scena.Lambda('lambda_0400')
    def lambda_0400():
        ChrSetDirection(0x00FE, 225, 400)
        Yield()

        Jump('lambda_0400')

    DispatchAsync2(0x0108, 0x0001, lambda_0400)

    Sleep(50)

    @scena.Lambda('lambda_0416')
    def lambda_0416():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_0416')

    DispatchAsync2(0x0101, 0x0001, lambda_0416)

    Sleep(50)

    @scena.Lambda('lambda_042C')
    def lambda_042C():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_042C')

    DispatchAsync2(0x0102, 0x0001, lambda_042C)

    Sleep(50)

    @scena.Lambda('lambda_0442')
    def lambda_0442():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_0442')

    DispatchAsync2(0x00F9, 0x0001, lambda_0442)

    Sleep(400)

    Fade(500)
    CameraMove(210, 0, 8800, 0)
    OP_67(0, 4650, -10000, 0)
    CameraSetDistance(2880, 0)
    OP_6C(0, 0)
    OP_6E(315, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0200341163V#251F……雾香。\n',
            '最后能遇见你我很高兴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0580341164V#794F我则是忧喜参半呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580341165V#792F以后大概不会再见面了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0200341166V#257F嗯……\n',
            '以后就是我和这家伙的问题了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200341167V#251F不过你啊，这种时候\n',
            '就不能表现得温顺点吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200341168V到了最后还是这么不饶人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0580341169V#791F呵呵……\n',
            '你喜欢的不就是我这一点么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0200341170V#253F嘿嘿嘿……没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 90, 400)
    ChrSetFlags(0x0008, 0x0020)
    ChrSetFlags(0x0008, 0x0040)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetAfterImage(0x00, 0x0008, 0x0032, 0x01F4)
    ChrSetChipByIndex(0x0008, 3)
    ChrSetSubChip(0x0008, 1)
    Sleep(300)

    PlaySE(571, 0x00, 0x64)
    ChrSetSubChip(0x0008, 2)

    @scena.Lambda('lambda_0660')
    def lambda_0660():
        ChrJumpTo(0x00FE, 2080, 950, 12870, 1500, 8000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0660)

    WaitForThreadExit(0x0008, 0x0001)
    PlaySE(164, 0x00, 0x64)
    ChrSetSubChip(0x0008, 1)
    Sleep(50)

    PlaySE(571, 0x00, 0x64)
    ChrSetSubChip(0x0008, 2)

    @scena.Lambda('lambda_069C')
    def lambda_069C():
        ChrJumpTo(0x00FE, 12720, 250, 13130, 1000, 8000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_069C)

    ChrSetSubChip(0x0008, 1)
    Fade(500)
    CameraMove(15140, 250, 15230, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(33000, 0)
    OP_6E(277, 0)
    WaitForThreadExit(0x0008, 0x0001)
    PlaySE(164, 0x00, 0x64)
    ChrSetAfterImage(0x01, 0x0008, 0x0000, 0x0000)
    WaitForThreadExit(0x0102, 0x0003)
    Sleep(500)

    Fade(500)
    ChrSetChipByIndex(0x0008, 4)
    ChrSetSubChip(0x0008, 0)
    Sleep(500)

    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x00F9, 0x01)
    TerminateThread(0x0108, 0x01)
    TerminateThread(0x0009, 0x01)

    ChrTalk(
        0x0108,
        (
            '#0080341171V#073F#2P喂、喂！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0769')
    def lambda_0769():
        CameraMove(13250, 250, 13830, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0769)

    @scena.Lambda('lambda_0781')
    def lambda_0781():
        OP_67(0, 6960, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0781)

    ChrWalkTo(0x0108, 1510, 0, 9630, 6000, 0x00)
    ChrWalkTo(0x0108, 9110, 250, 12840, 6000, 0x00)
    ChrTurnDirection(0x0108, 0x0008, 400)
    Sleep(500)

    TerminateThread(0x0008, 0x01)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#0200341172V#250F#5P……金。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200341173V为什么我会和老头子\n',
            '进行生死决斗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200341174V如果想知道的话，\n',
            '就试着将我打败吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200341175V用老头子\n',
            '传给你的『活人拳』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0008, 3)
    ChrSetSubChip(0x0008, 1)
    Sleep(300)

    PlaySE(571, 0x00, 0x64)
    ChrSetSubChip(0x0008, 2)
    ChrClearFlags(0x0008, 0x0001)

    @scena.Lambda('lambda_08A3')
    def lambda_08A3():
        CameraMove(14850, 250, 15000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_08A3)

    @scena.Lambda('lambda_08BB')
    def lambda_08BB():
        OP_67(0, 6450, -10000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_08BB)

    @scena.Lambda('lambda_08D3')
    def lambda_08D3():
        ChrJumpTo(0x00FE, 14050, 1300, 13300, 2000, 4000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_08D3)

    ChrSetSubChip(0x0008, 1)
    WaitForThreadExit(0x0008, 0x0001)
    PlaySE(164, 0x00, 0x64)
    ChrSetChipByIndex(0x0008, 4)
    ChrSetSubChip(0x0008, 0)
    WaitForThreadExit(0x0008, 0x0001)
    WaitForThreadExit(0x0101, 0x0001)
    ChrSetDirection(0x0008, 270, 400)
    WaitForThreadExit(0x0008, 0x0000)
    Sleep(500)

    ChrSetAfterImage(0x00, 0x0008, 0x0032, 0x01F4)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapClearFlags(0x00000010)
    ChrSetChipByIndex(0x0008, 3)
    ChrSetSubChip(0x0008, 1)
    Sleep(300)

    PlaySE(571, 0x00, 0x64)
    ChrSetSubChip(0x0008, 0)

    @scena.Lambda('lambda_0954')
    def lambda_0954():
        CameraSetDistance(2800, 500)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_0954)

    @scena.Lambda('lambda_0964')
    def lambda_0964():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0964)

    @scena.Lambda('lambda_0976')
    def lambda_0976():
        ChrJumpTo(0x00FE, 16590, -5000, 14080, 1000, 4000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0976)

    Sleep(500)

    OP_62(0x0108, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    WaitForThreadExit(0x0008, 0x0001)
    ChrSetFlags(0x0008, 0x0080)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(500)

    ChrTalk(
        0x0108,
        (
            '#0080341176V#077F#5P什……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    MapSetFlags(0x00000010)
    CameraMove(1580, 0, 5260, 0)
    OP_67(0, 3900, -10000, 0)
    CameraSetDistance(2670, 0)
    OP_6C(21000, 0)
    OP_6E(303, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010300882V#1020F#6P慢、慢着！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    CameraMove(12720, 250, 13130, 0)
    OP_67(0, 6250, -10000, 0)
    CameraSetDistance(3330, 0)
    OP_6C(45000, 0)
    OP_6E(301, 0)

    @scena.Lambda('lambda_0AA5')
    def lambda_0AA5():
        CameraMove(15810, 250, 13140, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0AA5)

    @scena.Lambda('lambda_0ABD')
    def lambda_0ABD():
        OP_67(0, 5700, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0ABD)

    @scena.Lambda('lambda_0AD5')
    def lambda_0AD5():
        CameraSetDistance(3000, 4000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0AD5)

    @scena.Lambda('lambda_0AE5')
    def lambda_0AE5():
        ChrWalkTo(0x00FE, 13350, 250, 12650, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_0AE5)

    CreateThread(0x0101, 0x01, 0x00, func_03_10FE)
    Sleep(500)

    CreateThread(0x0102, 0x01, 0x00, func_04_112E)
    Sleep(500)

    CreateThread(0x00F9, 0x01, 0x00, func_05_115E)
    WaitForThreadExit(0x0108, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    Sleep(500)

    ChrTalk(
        0x0108,
        (
            '#0080341178V#572F#6P…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341179V#1020F#6P开，开玩笑吧！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010341180V『执行者』\n',
            '从这个高度落下也没事吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341181V#1035F#6P虽然不是所有人都这样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020341182V#1042F但是像他这种高手\n',
            '就算没事也不足为奇。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080341183V#074F#6P啊啊，撑住外壁\n',
            '降低下落速度。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080341184V#072F好厉害的硬功和化劲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0009, 2760, 250, 10680, 90)
    OP_E5(0x09, 0x00, 0x00)

    ChrTalk(
        0x0009,
        (
            '#0580341185V#2P真是的……\n',
            '吓唬人也要有个程度啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0CD5')
    def lambda_0CD5():
        CameraMove(13910, 250, 12760, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0CD5)

    @scena.Lambda('lambda_0CED')
    def lambda_0CED():
        OP_67(0, 6000, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0CED)

    @scena.Lambda('lambda_0D05')
    def lambda_0D05():
        ChrWalkTo(0x00FE, 10190, 250, 11430, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0D05)

    @scena.Lambda('lambda_0D20')
    def lambda_0D20():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_0D20')

    DispatchAsync2(0x0101, 0x0001, lambda_0D20)

    Sleep(50)

    @scena.Lambda('lambda_0D36')
    def lambda_0D36():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_0D36')

    DispatchAsync2(0x0108, 0x0001, lambda_0D36)

    Sleep(50)

    @scena.Lambda('lambda_0D4C')
    def lambda_0D4C():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_0D4C')

    DispatchAsync2(0x0102, 0x0001, lambda_0D4C)

    Sleep(50)

    @scena.Lambda('lambda_0D62')
    def lambda_0D62():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_0D62')

    DispatchAsync2(0x00F9, 0x0001, lambda_0D62)

    WaitForThreadExit(0x0009, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x0108, 0x01)
    TerminateThread(0x00F9, 0x01)

    ChrTalk(
        0x0108,
        (
            '#0080341186V#072F#5P雾香……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080341187V你怎么知道瓦鲁特\n',
            '来了这里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0580341188V#794F#6P你以为我不知道？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580341189V#792F真是的……\n',
            '你也好瓦鲁特也好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580341190V#791F男人为什么\n',
            '都这么笨拙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080341191V#075F#5P呜唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010341192V#1019F#5P……………………（盯）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341193V#1048F#2P……我在反省啦\n',
            '拜托别用那种眼神看我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F22',
    )

    ChrTalk(
        0x0103,
        (
            '#0030341194V#027F#6P呵呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F22(): pass

    label('loc_F22')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F52',
    )

    ChrTalk(
        0x0107,
        (
            '#0070320670V#061F#6P嘿嘿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F52(): pass

    label('loc_F52')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F84',
    )

    ChrTalk(
        0x0105,
        (
            '#0060341196V#048F#6P哈哈哈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F84(): pass

    label('loc_F84')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_FC5',
    )

    ChrTalk(
        0x0106,
        (
            '#0050341197V#051F#6P嘿……\n',
            '怎么扯到那么远了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FC5(): pass

    label('loc_FC5')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1003',
    )

    ChrTalk(
        0x0109,
        (
            '#0180341198V#1068F#6P嗯……\n',
            '这话真刺耳啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1003(): pass

    label('loc_1003')

    ChrTalk(
        0x0009,
        (
            '#0580341199V#792F#6P好了，私事解决了，\n',
            '我也差不多该回蔡斯了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580341200V#791F……祝各位好运。\n',
            '去其他的塔时也请当心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1086')
    def lambda_1086():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1086)

    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010341201V#1025F#2P雾香……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080341202V#070F#5P嗯嗯……明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    OP_20(0x000007D0)
    OP_21()
    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    NewScene('ED6_DT21/E0311._SN', 103, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x10FE
@scena.Code('func_03_10FE')
def func_03_10FE():
    ChrWalkTo(0x00FE, 2350, 250, 8130, 5000, 0x00)
    ChrWalkTo(0x00FE, 13940, 250, 11470, 5000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x0004 offset: 0x112E
@scena.Code('func_04_112E')
def func_04_112E():
    ChrWalkTo(0x00FE, 2350, 250, 8130, 5000, 0x00)
    ChrWalkTo(0x00FE, 13760, 250, 10210, 5000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x0005 offset: 0x115E
@scena.Code('func_05_115E')
def func_05_115E():
    ChrWalkTo(0x00FE, 2350, 250, 8130, 5000, 0x00)
    ChrWalkTo(0x00FE, 12580, 250, 11120, 5000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x0006 offset: 0x118E
@scena.Code('func_06_118E')
def func_06_118E():
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
        (0x00000000, 'loc_1208'),
        (0x00000001, 'loc_120E'),
        (-1, 'loc_1214'),
    )

    def _loc_1208(): pass

    label('loc_1208')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_1214')

    def _loc_120E(): pass

    label('loc_120E')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_1214')

    def _loc_1214(): pass

    label('loc_1214')

    Return()

# id: 0x0007 offset: 0x1215
@scena.Code('func_07_1215')
def func_07_1215():
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
            ChrTable['金'],
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['雪拉扎德'],
            ChrTable['提妲'],
            ChrTable['科洛丝'],
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
