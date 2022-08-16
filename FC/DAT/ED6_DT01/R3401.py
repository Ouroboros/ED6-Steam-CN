import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import R3401_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R3401   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'R3401.x'
    header.mapIndex       = 1
    header.bgm            = 30
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
        ('ED6_DT09/CH10750._CH', 'ED6_DT09/CH10750P._CP'),
        ('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP'),
        ('ED6_DT07/CH00162._CH', 'ED6_DT07/CH00162P._CP'),
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00101._CH', 'ED6_DT07/CH00101P._CP'),
        ('ED6_DT07/CH00110._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT07/CH00111._CH', 'ED6_DT07/CH00111P._CP'),
        ('ED6_DT07/CH00102._CH', 'ED6_DT07/CH00102P._CP'),
        ('ED6_DT07/CH00161._CH', 'ED6_DT07/CH00161P._CP'),
        ('ED6_DT09/CH10130._CH', 'ED6_DT09/CH10130P._CP'),
        ('ED6_DT09/CH10131._CH', 'ED6_DT09/CH10131P._CP'),
        ('ED6_DT09/CH10750._CH', 'ED6_DT09/CH10750P._CP'),
        ('ED6_DT09/CH10751._CH', 'ED6_DT09/CH10751P._CP'),
        ('ED6_DT09/CH10760._CH', 'ED6_DT09/CH10760P._CP'),
        ('ED6_DT09/CH10761._CH', 'ED6_DT09/CH10761P._CP'),
        ('ED6_DT09/CH10770._CH', 'ED6_DT09/CH10770P._CP'),
        ('ED6_DT09/CH10771._CH', 'ED6_DT09/CH10771P._CP'),
    ]

# id: 0x10001 offset: 0x132
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '魔兽',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '魔兽',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '魔兽',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '魔兽',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '艾尔·雷登关所方向',
            x                   = 169300,
            z                   = 0,
            y                   = -27030,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '蔡斯方向',
            x                   = 330710,
            z                   = 0,
            y                   = -37560,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
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
            dword_10            = 1,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x212
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = 257600,
            z           = 70,
            y           = -24310,
            word_0C     = 0x00B4,
            word_0E     = 0x000F,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01D3,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 286240,
            z           = 20,
            y           = -35830,
            word_0C     = 0x00B4,
            word_0E     = 0x0009,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01D1,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x24A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 222300,
            y           = -1000,
            z           = -28000,
            range       = 217700,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFF6CBC,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000004,
        ),
    )

# id: 0x10004 offset: 0x26A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 199000,
            triggerZ            = 500,
            triggerY            = -22200,
            triggerRange        = 800,
            actorX              = 199000,
            actorZ              = 1500,
            actorY              = -22200,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 285640,
            triggerZ            = 0,
            triggerY            = -26290,
            triggerRange        = 1000,
            actorX              = 285640,
            actorZ              = 1000,
            actorY              = -26290,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2B2
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x2B3
@scena.Code('func_01_2B3')
def func_01_2B3():
    OP_16(0x02, 4000, 127000, -157000, 196664)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 6, 0x506)),
            Expr.Return,
        ),
        'loc_2DA',
    )

    OP_71(0x0000, 0x0004)
    OP_72(0x0001, 0x0004)
    OP_64(0x00, 0x0001)

    def _loc_2DA(): pass

    label('loc_2DA')

    LoadEffect(0x00, 'map\\\\mp027_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, 285640, 1000, -26290, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)

    Return()

# id: 0x0002 offset: 0x324
@scena.Code('func_02_324')
def func_02_324():
    ExecExpressionWithValue(
        0x00FE,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0000,
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
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_354',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_496')

    def _loc_354(): pass

    label('loc_354')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_36D',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_496')

    def _loc_36D(): pass

    label('loc_36D')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_386',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_496')

    def _loc_386(): pass

    label('loc_386')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_39F',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_496')

    def _loc_39F(): pass

    label('loc_39F')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3B8',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_496')

    def _loc_3B8(): pass

    label('loc_3B8')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3D1',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_496')

    def _loc_3D1(): pass

    label('loc_3D1')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3EA',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_496')

    def _loc_3EA(): pass

    label('loc_3EA')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_403',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_496')

    def _loc_403(): pass

    label('loc_403')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_41C',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_496')

    def _loc_41C(): pass

    label('loc_41C')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_435',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_496')

    def _loc_435(): pass

    label('loc_435')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_44E',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_496')

    def _loc_44E(): pass

    label('loc_44E')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_467',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_496')

    def _loc_467(): pass

    label('loc_467')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_480',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_496')

    def _loc_480(): pass

    label('loc_480')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_496',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_496(): pass

    label('loc_496')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4AB',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_496')

    def _loc_4AB(): pass

    label('loc_4AB')

    Return()

# id: 0x0003 offset: 0x4AC
@scena.Code('func_03_4AC')
def func_03_4AC():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 4, 0x504)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5B9',
    )

    SetScenaFlags(ScenaFlag(0x00A0, 4, 0x504))

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_502',
    )

    ChrTalk(
        0x0101,
        (
            '#0010070371V#004F咦……\n',
            '这个照明灯，是不是有点怪呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_53C')

    def _loc_502(): pass

    label('loc_502')

    ChrTalk(
        0x0101,
        (
            '#0010070372V#004F咦……\n',
            '那个照明灯，是不是有点怪呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_53C(): pass

    label('loc_53C')

    ChrTalk(
        0x0102,
        (
            '#0020070373V#012F确实是。\n',
            '应该是有点故障了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020070374V导力器的导力\n',
            '是可以自动积蓄的，\n',
            '所以，我想应该不用担心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_62D')

    def _loc_5B9(): pass

    label('loc_5B9')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5F5',
    )

    ChrTalk(
        0x0101,
        (
            '#0010070375V#000F照明灯好像有点怪怪的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_62D')

    def _loc_5F5(): pass

    label('loc_5F5')

    ChrTalk(
        0x0102,
        (
            '#0020070376V#015F照明灯有点闪烁。\n',
            '看来有点故障了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_62D(): pass

    label('loc_62D')

    EventEnd(0x01)

    Return()

# id: 0x0004 offset: 0x630
@scena.Code('func_04_630')
def func_04_630():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 6, 0x506)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 5, 0x505)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1E4F',
    )

    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    SetScenaFlags(ScenaFlag(0x00A0, 6, 0x506))
    EventBegin(0x00)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x0008, 197700, 0, -23200, 45)
    ChrSetPos(0x0009, 199000, 0, -24200, 0)
    ChrSetPos(0x000A, 200900, 0, -24200, 315)
    ChrSetPos(0x000B, 200600, 0, -23100, 315)
    ChrSetFlags(0x0008, 0x0040)
    ChrSetFlags(0x0009, 0x0040)
    ChrSetFlags(0x000A, 0x0040)
    ChrSetFlags(0x000B, 0x0040)

    NpcTalk(
        0x0008,
        '女孩子的声音',
        (
            '#0070070406V啊——！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    Fade(1000)
    OP_6C(45000, 0)
    CameraMove(200700, 2000, -24400, 0)
    ChrSetStatus(0x0006, 0x00, 18)
    OP_B5(0x0006, 0x00)
    OP_B5(0x0006, 0x01)
    OP_B5(0x0006, 0x05)
    OP_B5(0x0006, 0x04)
    EquipCmd(0x06, 0x00B5)
    EquipCmd(0x06, 0x00F4)
    EquipCmd(0x06, 0x0112)
    EquipCmd(0x06, 0x02C9, 0x00)
    EquipCmd(0x06, 0x0271, 0x01)
    EquipCmd(0x06, 0x0262, 0x05)
    EquipCmd(0x06, 0x026B, 0x04)
    AddCraft(0x0006, 0x00D2)
    AddSCraft(0x0006, 0x0104)
    FormationAddMember(0x06, 0xFF)
    ChrSetPos(0x0107, 204300, 0, -26400, 270)
    OP_0D()
    OP_21()
    PlayBGM(86)
    ChrSetFlags(0x0101, 0x1000)
    ChrSetFlags(0x0102, 0x1000)
    Sleep(500)

    OP_62(0x0107, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    NpcTalk(
        0x0107,
        '小女孩',
        (
            '#0070070407V#065F#2P已、已经聚集了\n',
            '这么多只魔兽啊～……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070408V这样下去会坏掉的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070409V既、既然这样的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0839')
    def lambda_0839():
        CameraSetDistance(2600, 2500)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_0839)

    Sleep(1000)

    PlaySE(216, 0x00, 0x64)
    ChrSetChipByIndex(0x0107, 2)

    ExecExpressionWithValue(
        0x0107,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(1000)

    Sleep(500)

    ChrTurnDirection(0x0107, 0x000A, 0)

    NpcTalk(
        0x0107,
        '小女孩',
        (
            '#0070070410V#062F#2P方向ＯＫ，仰角２０度……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    NpcTalk(
        0x0107,
        '小女孩',
        (
            '#0070070411V#062F导力填充率３０％……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070412V#068F……发射！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    LoadEffect(0x02, 'map\\\\mp019_00.eff')

    @scena.Lambda('lambda_0917')
    def lambda_0917():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000001F4, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_0917)

    ChrSetChipByIndex(0x0107, 2)
    ChrSetPos(0x000E, 196500, 1500, -22500, 0)
    PlaySE(506, 0x00, 0x64)
    PlayEffect(0x02, 0xFF, 0x0107, 250, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0x000E, 0, 0, 0, 0)
    OP_99(0x0107, 0x00, 0x03, 2000)
    OP_99(0x0107, 0x03, 0x07, 2000)

    @scena.Lambda('lambda_098F')
    def lambda_098F():
        OP_94(0x01, 0x00FE, 0x0078, 0x00000384, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_098F)

    @scena.Lambda('lambda_09A5')
    def lambda_09A5():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_09A5)

    @scena.Lambda('lambda_09BB')
    def lambda_09BB():
        OP_94(0x01, 0x00FE, 0x00E6, 0x000002BC, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_09BB)

    @scena.Lambda('lambda_09D1')
    def lambda_09D1():
        OP_94(0x01, 0x00FE, 0x005A, 0x000001F4, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_09D1)

    Sleep(1000)

    WaitForThreadExit(0x0008, 0x0001)

    @scena.Lambda('lambda_09F1')
    def lambda_09F1():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_09F1)

    WaitForThreadExit(0x0009, 0x0001)

    @scena.Lambda('lambda_0A04')
    def lambda_0A04():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0A04)

    WaitForThreadExit(0x000A, 0x0001)

    @scena.Lambda('lambda_0A17')
    def lambda_0A17():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0A17)

    WaitForThreadExit(0x000B, 0x0001)

    @scena.Lambda('lambda_0A2A')
    def lambda_0A2A():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0A2A)

    ChrSetDirection(0x0107, 270, 0)
    Sleep(400)

    NpcTalk(
        0x0107,
        '小女孩',
        (
            '#0070070413V#062F#2P再、再靠近的话，\n',
            '这次真的会打中你们哦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070414V真、真的哦，我是认真的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(300)

    OP_62(0x0009, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(100)

    OP_62(0x000B, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(100)

    OP_62(0x0008, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(200)

    Sleep(1000)

    @scena.Lambda('lambda_0B13')
    def lambda_0B13():
        CameraMove(201700, 2000, -25100, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0B13)

    ChrSetFlags(0x0008, 0x0020)
    ChrSetFlags(0x0009, 0x0020)
    ChrSetFlags(0x000A, 0x0020)
    ChrSetFlags(0x000B, 0x0020)

    @scena.Lambda('lambda_0B3F')
    def lambda_0B3F():
        OP_94(0x00, 0x00FE, 0x0000, 0x0000012C, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0B3F)

    OP_63(0x000A)
    Sleep(300)

    @scena.Lambda('lambda_0B5D')
    def lambda_0B5D():
        OP_94(0x00, 0x00FE, 0x0000, 0x00000258, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0B5D)

    OP_63(0x000B)

    @scena.Lambda('lambda_0B76')
    def lambda_0B76():
        OP_94(0x00, 0x00FE, 0x0000, 0x000003E8, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0B76)

    OP_63(0x0009)
    Sleep(600)

    @scena.Lambda('lambda_0B94')
    def lambda_0B94():
        OP_94(0x00, 0x00FE, 0x0000, 0x00000320, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0B94)

    OP_63(0x0008)
    ChrSetChipByIndex(0x0107, 1)
    OP_62(0x0107, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1700)

    NpcTalk(
        0x0107,
        '小女孩',
        (
            '#0070070415V#065F#2P啊……\n',
            '起、起到反效果了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0101, 210200, 0, -30000, 0)
    ChrSetPos(0x0102, 209330, 0, -30000, 0)
    ChrSetFlags(0x0102, 0x0004)

    @scena.Lambda('lambda_0C31')
    def lambda_0C31():
        OP_94(0x00, 0x00FE, 0x0000, 0x000003E8, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0C31)

    Sleep(150)

    @scena.Lambda('lambda_0C4C')
    def lambda_0C4C():
        OP_94(0x00, 0x00FE, 0x0000, 0x000003E8, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0C4C)

    @scena.Lambda('lambda_0C62')
    def lambda_0C62():
        OP_94(0x00, 0x00FE, 0x0000, 0x000001F4, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0C62)

    Sleep(300)

    @scena.Lambda('lambda_0C7D')
    def lambda_0C7D():
        OP_94(0x00, 0x00FE, 0x0000, 0x00000258, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0C7D)

    Sleep(400)

    NpcTalk(
        0x0107,
        '小女孩',
        (
            '#0070070416V#069F#2P呀……！',
            TxtCtl.Enter,
        ),
    )

    OP_9E(0x0107, 20, 0, 400, 4000)
    CloseMessageWindow()

    @scena.Lambda('lambda_0CD4')
    def lambda_0CD4():
        OP_94(0x00, 0x000A, 0x0000, 0x000007D0, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0CD4)

    ChrSetFlags(0x0101, 0x1000)
    ChrSetFlags(0x0102, 0x1000)
    ChrSetChipByIndex(0x0101, 4)
    ChrSetChipByIndex(0x0102, 6)

    @scena.Lambda('lambda_0CFE')
    def lambda_0CFE():
        CameraSetDistance(3160, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0CFE)

    @scena.Lambda('lambda_0D0E')
    def lambda_0D0E():
        CameraMove(203200, 0, -24900, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0D0E)

    @scena.Lambda('lambda_0D26')
    def lambda_0D26():
        OP_6C(78000, 1200)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0D26)

    ChrTalk(
        0x0101,
        (
            '#0010070417V#10A#1P喔喔喔喔喔！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    ChrWalkTo(0x0101, 206580, 0, -26490, 10000, 0x00)

    @scena.Lambda('lambda_0D6F')
    def lambda_0D6F():
        ChrWalkTo(0x00FE, 202680, 0, -27350, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0D6F)

    @scena.Lambda('lambda_0D8A')
    def lambda_0D8A():
        ChrSetDirection(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0002, lambda_0D8A)

    ChrSetFlags(0x0107, 0x1000)
    ChrSetChipByIndex(0x0107, 8)

    @scena.Lambda('lambda_0DA2')
    def lambda_0DA2():
        ChrMoveTo(0x00FE, 205130, 0, -27290, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_0DA2)

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0101, 7)

    @scena.Lambda('lambda_0DCD')
    def lambda_0DCD():
        OP_99(0x00FE, 0x00, 0x0C, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0DCD)

    PlaySE(164, 0x00, 0x64)
    PlaySE(500, 0x00, 0x64)
    ChrJumpTo(0x0101, 202800, 0, -25600, 1500, 6000)
    OP_7C(0, 100, 3000, 100)
    PlayEffect(0x08, 0xFF, 0x00FF, 202800, 0, -25600, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_0E44')
    def lambda_0E44():
        OP_94(0x01, 0x000A, 0x00B4, 0x000007D0, 0x00003A98, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0E44)

    ChrJumpTo(0x0101, 203410, 0, -26030, 500, 5000)

    @scena.Lambda('lambda_0E71')
    def lambda_0E71():
        OP_94(0x01, 0x00FE, 0x00B4, 0x00000384, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0E71)

    @scena.Lambda('lambda_0E87')
    def lambda_0E87():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0E87)

    @scena.Lambda('lambda_0E9D')
    def lambda_0E9D():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000001F4, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0E9D)

    WaitForThreadExit(0x0102, 0x0001)
    ChrSetChipByIndex(0x0102, 5)
    ChrClearFlags(0x0102, 0x0004)
    Sleep(1000)

    NpcTalk(
        0x0107,
        '小女孩',
        (
            '#0070070418V#065F咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0107, 1)
    ChrClearFlags(0x0107, 0x1000)
    ChrTurnDirection(0x0107, 0x0101, 400)

    NpcTalk(
        0x0107,
        '小女孩',
        (
            '#0070070419V#560F啊，刚才的……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070420V#006F待会再慢慢聊吧！\n',
            '你先退到我们后面去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070421V#012F总之\n',
            '先把这些家伙赶走吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Battle(0x000003A7, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_FA9'),
        (-1, 'loc_FAC'),
    )

    def _loc_FA9(): pass

    label('loc_FA9')

    OP_B4(0x00)

    Return()

    def _loc_FAC(): pass

    label('loc_FAC')

    EventBegin(0x00)

    ExecExpressionWithVar(
        0x23,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetPos(0x0101, 202800, 0, -25600, 315)
    ChrSetPos(0x0102, 202500, 0, -27300, 315)
    ChrSetPos(0x0107, 204200, 0, -26900, 315)
    CameraMove(203400, 0, -26050, 0)
    ChrSetChipByIndex(0x0107, 65535)
    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    FadeIn(1000, 0)
    OP_0D()

    NpcTalk(
        0x0107,
        '小女孩',
        (
            '#0070070422V#065F真、真是吓死人了～……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070423V#067F那个那个……\n',
            '真是非常感谢呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070424V救了我一命呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0101, 0xFF)

    @scena.Lambda('lambda_10B6')
    def lambda_10B6():
        CameraSetDistance(2790, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_10B6)

    ChrSetChipByIndex(0x0102, 65535)
    ChrTurnDirection(0x0102, 0x0107, 400)
    ChrSetChipByIndex(0x0101, 65535)
    ChrTurnDirection(0x0101, 0x0107, 400)
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0101,
        (
            '#0010070425V#001F啊哈哈。\n',
            '你没事就好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070426V#006F不过……\n',
            '以后可要吸取教训哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070427V一个人和魔兽战斗\n',
            '这种危险的事可不能做哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0107,
        '小女孩',
        (
            '#0070070428V#065F啊，但是但是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070429V如果放着不管的话，\n',
            '隧道的照明灯会坏掉呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070430V#505F这么说来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070431V为什么魔兽会聚集在\n',
            '熄灭了的照明灯周围呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0006, 0x01, 0x0008)"),
            Expr.Return,
        ),
        'loc_132A',
    )

    ChrTalk(
        0x0102,
        (
            '#0020070432V#010F以前在更换路灯的时候\n',
            '不是也发生过同样的事吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020070433V因为导力器里的七耀石\n',
            '是魔兽喜欢的东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020070434V因此路灯里\n',
            '都带有驱赶魔兽的机能……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020070435V如果这种机能坏了的话，\n',
            '自然就会容易吸引魔兽过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13D8')

    def _loc_132A(): pass

    label('loc_132A')

    ChrTalk(
        0x0102,
        (
            '#0020070436V#010F因为导力器里的七耀石\n',
            '是魔兽喜欢的东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020070437V因此路灯里\n',
            '都带有驱赶魔兽的机能……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020070438V如果这种机能坏了的话，\n',
            '自然就会容易吸引魔兽过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13D8(): pass

    label('loc_13D8')

    ChrTalk(
        0x0101,
        (
            '#0010070439V#501F啊，原来是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070440V#007F不过就算这样，\n',
            '也不能这么胡来啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070441V万一受伤的话可就不好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0107,
        '小女孩',
        (
            '#0070070442V#063F啊……\n',
            '对、对不起……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070443V#019F好了好了，到此为止吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020070444V更何况，『不能胡来』从你嘴里说出来，\n',
            '可是完全没有说服力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070445V#509F讨厌，少泼冷水啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070446V#006F算了……\n',
            '我叫艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070447V#010F我是约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020070448V我们俩都是\n',
            '游击士协会的见习游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0107,
        '小女孩',
        (
            '#0070070449V#061F哇～～\n',
            '难怪那么厉害呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070450V#060F我叫提妲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070451V现在正在\n',
            '蔡斯的中央工房实习。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070452V#501F嘿嘿～\n',
            '所以才会打扮成这样吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070453V那么，提妲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070454V你要回蔡斯的话，\n',
            '就和我们一起走吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070455V#010F是啊。\n',
            '如果再遇到魔兽就糟糕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070070456V#061F真、真的吗？\n',
            '真是非常感谢呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070457V#560F啊，不过请稍等一下。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070458V我得先修理好那个照明灯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070459V#004F啊，那也是。\n',
            '这样放着不管的确非常危险。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070460V不过……\n',
            '你是怎么知道这里的照明灯坏了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070070461V#060F啊，我在调查电脑的\n',
            '数据库的时候偶然发现的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070462V好像当初安装时候用的是次品，\n',
            '而且设置元件也不齐全。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070463V#010F原来如此，\n',
            '那你还是快看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070464V#505F（电脑？数据库？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(198940, 30, -23590, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    ChrSetPos(0x0101, 199360, 10, -24480, 0)
    ChrSetPos(0x0102, 198190, 20, -24530, 0)
    ChrSetPos(0x0107, 199160, 20, -22710, 0)
    ChrSetFlags(0x0107, 0x0004)
    Sleep(500)

    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0107,
        (
            '#0070070465V#062F#4P……嘿咻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_72(0x0001, 0x0004)
    Sleep(100)

    OP_71(0x0001, 0x0004)
    Sleep(100)

    OP_72(0x0001, 0x0004)
    Sleep(100)

    OP_71(0x0001, 0x0004)
    Sleep(90)

    OP_72(0x0001, 0x0004)
    Sleep(80)

    OP_71(0x0001, 0x0004)
    Sleep(70)

    OP_72(0x0001, 0x0004)
    Sleep(60)

    OP_71(0x0001, 0x0004)
    Sleep(50)

    OP_72(0x0001, 0x0004)
    Sleep(1000)

    ChrTalk(
        0x0107,
        (
            '#0070070466V#560F#4P好～这样就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveTo(0x0107, 199100, 30, -23330, 2000, 0x00)
    ChrSetDirection(0x0107, 180, 400)
    ChrClearFlags(0x0107, 0x0004)

    ChrTalk(
        0x0107,
        (
            '#0070070467V#061F#1P让你们久等了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070468V#501F哎～好厉害。\n',
            '原来你这么熟练的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070469V#019F真不愧是\n',
            '在中央工房的见习生啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070070470V#067F#1P嘿嘿……\n',
            '这不算什么啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070471V只不过是修正接触不良的结晶回路\n',
            '和调整错乱的导力压而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070472V#505F？？？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070473V唔……\n',
            '听起来好像相当复杂的样子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070070474V#560F其实一点也不复杂。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070475V这个呢，\n',
            '简单解释起来的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070070476V#1K#1P在导力器的内部镶嵌着\n',
            '可以发挥各种功能的结晶回路。\n',
            '结晶回路与元件必须准确地\n',
            '进行连接才能使导力器正常运作，\n',
            '而当两者出现连接错误时，\n',
            '导力器生成的导力就会无处可去，\n',
            '其结果自然就导致\n',
            '设计时预想的机能无法正常发挥。\n',
            '以照明灯的情况来说就是发光和驱除魔兽的……',
            TxtCtl.Enter,
        ),
    )

    Sleep(2000)

    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0101,
        (
            '#0010070477V#1K#004F停、停一下！',
            TxtCtl.Enter,
        ),
    )

    OP_56(0x01)
    OP_59()

    ChrTalk(
        0x0101,
        (
            '#0010070478V#506F还、还是以后再慢慢解释吧。\n',
            '我们差不多该出发了呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070479V嗯嗯～\n',
            '站在这里说话也不方便嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070070480V#067F#1P啊，说得也是。\n',
            '虽然没解释完有点可惜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070481V#007F（呼……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070482V#019F哈哈，\n',
            '那我们继续前往蔡斯吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070483V#006FＯＫ！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070070484V#061F#1P好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0101, 0x1000)
    ChrClearFlags(0x0102, 0x1000)
    OP_64(0x00, 0x0001)
    EventEnd(0x00)

    def _loc_1E4F(): pass

    label('loc_1E4F')

    Return()

# id: 0x0005 offset: 0x1E50
@scena.Code('func_05_1E50')
def func_05_1E50():
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '这是一台可供旅行者回复体力的导力器装置。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

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
        32,
        1,
        (
            TXT(0x00, '在此休息\n'),
            TXT(0x01, '离开\n'),
        ),
    )

    MenuEnd(0x0001)

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

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2069',
    )

    FadeIn(100, 0)
    Sleep(500)

    OP_26(13)
    StopEffect(0x00, 0x02)
    PlayEffect(0x00, 0x02, 0x00FF, 285640, 1000, -26290, 0, 0, 0, 700, 700, 700, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0011, 0)
    OP_70(0x0011, 50)
    OP_73(0x0011)
    OP_20(0x00000BB8)
    PlaySE(12, 0x00, 0x64)
    StopEffect(0x02, 0x02)
    LoadEffect(0x01, 'map\\\\mp027_01.eff')
    PlayEffect(0x01, 0x01, 0x00FF, 285640, 1000, -26290, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    FadeOut(1000, 0, -1)
    Sleep(700)

    PlaySE(13, 0x00, 0x64)
    OP_0D()
    ChrSetStatus(0x0000, 0xFE, 0)
    ChrSetStatus(0x0001, 0xFE, 0)
    ChrSetStatus(0x0002, 0xFE, 0)
    ChrSetStatus(0x0003, 0xFE, 0)
    ChrSetStatus(0x0004, 0xFE, 0)
    ChrSetStatus(0x0005, 0xFE, 0)
    ChrSetStatus(0x0006, 0xFE, 0)
    ChrSetStatus(0x0007, 0xFE, 0)
    ChrSetPos(0x0000, 285600, 30, -28390, 13)
    ChrSetPos(0x0001, 285600, 30, -28390, 13)
    ChrSetPos(0x0002, 285600, 30, -28390, 13)
    ChrSetPos(0x0003, 285600, 30, -28390, 13)
    OP_69(0x0000, 0)
    OP_30(0x00)
    Sleep(3500)

    StopEffect(0x01, 0x02)
    LoadEffect(0x00, 'map\\\\mp027_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, 285640, 1000, -26290, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0011, 0)
    OP_1E()
    FadeIn(1000, 0)
    OP_56(0x00)
    TalkEnd(0x00FF)

    Return()

    def _loc_2069(): pass

    label('loc_2069')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2083',
    )

    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

    def _loc_2083(): pass

    label('loc_2083')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
