import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C6000_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C6000   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C6000.x'
    header.mapIndex       = 1
    header.bgm            = 62
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
    ]

# id: 0x10001 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '目标',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0080,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0xC8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xC8
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 2000,
            y           = 4500,
            z           = 19500,
            range       = 4000,
            dword_10    = 0x00001964,
            dword_14    = 0x00004E20,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000012,
        ),
        ScenaEventData(
            x           = -12900,
            y           = 0,
            z           = 2140,
            range       = 2000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x0000001A,
        ),
    )

# id: 0x10004 offset: 0x108
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 2000,
            triggerZ            = 2000,
            triggerY            = 1560,
            triggerRange        = 1000,
            actorX              = 2000,
            actorZ              = 2000,
            actorY              = 1560,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 5200,
            triggerZ            = 0,
            triggerY            = 12110,
            triggerRange        = 1000,
            actorX              = 5200,
            actorZ              = 1200,
            actorY              = 13110,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001E,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x150
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_166',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    Event(0, func_11_34E7)

    Jump('loc_194')

    def _loc_166(): pass

    label('loc_166')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_177',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    Event(0, func_15_3EF7)

    Jump('loc_194')

    def _loc_177(): pass

    label('loc_177')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Return,
        ),
        'loc_194',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 3, 0x2203)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_190',
    )

    Event(0, func_02_1FA)

    Jump('loc_194')

    def _loc_190(): pass

    label('loc_190')

    Event(0, func_1B_4CB0)

    def _loc_194(): pass

    label('loc_194')

    Return()

# id: 0x0001 offset: 0x195
@scena.Code('func_01_195')
def func_01_195():
    PlaySE(451, 0x01, 0x64)
    OP_12(0x000124F8, 0x000493E0, 0x00000000)
    OP_72(0x0001, 0x0020)
    OP_72(0x0001, 0x0008)
    OP_6F(0x0001, 500)
    OP_72(0x0003, 0x0020)
    OP_72(0x0003, 0x0008)
    OP_6F(0x0003, 0)
    OP_71(0x0001, 0x0004)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 6, 0x2206)),
            Expr.Return,
        ),
        'loc_1E8',
    )

    OP_72(0x0001, 0x0004)
    OP_6F(0x0001, 950)
    OP_6F(0x0003, 240)

    def _loc_1E8(): pass

    label('loc_1E8')

    OP_72(0x0000, 0x0020)
    OP_72(0x0000, 0x0008)
    OP_6F(0x0000, 0)

    Return()

# id: 0x0002 offset: 0x1FA
@scena.Code('func_02_1FA')
def func_02_1FA():
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
        'loc_211',
    )

    Call(0, 0x001C)
    Call(0, 0x001D)

    def _loc_211(): pass

    label('loc_211')

    CameraMove(-13000, -12750, 490, 0)
    OP_67(0, 3890, -10000, 0)
    CameraSetDistance(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    OP_6F(0x0000, 300)
    Yield()
    OP_89(0x0101, -12000, -23000, 2000, 90)
    OP_89(0x0102, -13000, -23000, 3000, 90)
    OP_89(0x00F8, -13000, -23000, 1000, 90)
    OP_89(0x00F9, -14000, -23000, 2000, 90)
    OP_70(0x0000, 0)
    PlaySE(235, 0x00, 0x64)

    @scena.Lambda('lambda_02AC')
    def lambda_02AC():
        CameraMove(-13000, 0, 2000, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_02AC)

    @scena.Lambda('lambda_02C4')
    def lambda_02C4():
        OP_67(0, 3880, -10000, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_02C4)

    FadeIn(1000, 0)
    Sleep(4000)

    OP_24(0x00EB, 0x5A)
    Sleep(50)

    OP_24(0x00EB, 0x50)
    Sleep(50)

    OP_24(0x00EB, 0x46)
    Sleep(50)

    OP_24(0x00EB, 0x3C)
    Sleep(50)

    OP_24(0x00EB, 0x32)
    Sleep(50)

    OP_24(0x00EB, 0x28)
    Sleep(50)

    OP_24(0x00EB, 0x1E)
    Sleep(50)

    OP_24(0x00EB, 0x14)
    Sleep(50)

    OP_24(0x00EB, 0x0A)
    Sleep(50)

    OP_23(0x00EB)
    OP_73(0x0000)
    Sleep(200)

    CreateThread(0x0101, 0x01, 0x00, func_03_1011)
    Sleep(100)

    CreateThread(0x0102, 0x01, 0x00, func_05_10BF)
    Sleep(800)

    CreateThread(0x00F8, 0x01, 0x00, func_07_110B)
    Sleep(500)

    CreateThread(0x00F9, 0x01, 0x00, func_09_116B)
    WaitForThreadExit(0x00F9, 0x0001)

    @scena.Lambda('lambda_0376')
    def lambda_0376():
        CameraMove(-3930, 0, 11550, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0376)

    @scena.Lambda('lambda_038E')
    def lambda_038E():
        OP_67(0, 7500, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_038E)

    @scena.Lambda('lambda_03A6')
    def lambda_03A6():
        CameraSetDistance(3650, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_03A6)

    @scena.Lambda('lambda_03B6')
    def lambda_03B6():
        OP_6E(262, 6000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_03B6)

    Sleep(3000)

    CreateThread(0x0101, 0x01, 0x00, func_04_10A3)
    Sleep(500)

    CreateThread(0x0102, 0x01, 0x00, func_06_10EF)
    Sleep(300)

    CreateThread(0x00F8, 0x01, 0x00, func_08_113B)
    Sleep(300)

    CreateThread(0x00F9, 0x01, 0x00, func_0A_119B)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x00F8, 0x0001)
    WaitForThreadExit(0x00F9, 0x0001)
    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_434',
    )

    ChrTalk(
        0x0107,
        (
            '#0070390893V#064F哇……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_52B')

    def _loc_434(): pass

    label('loc_434')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_469',
    )

    ChrTalk(
        0x0105,
        (
            '#0060390894V#1164F好厉害……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_52B')

    def _loc_469(): pass

    label('loc_469')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_49B',
    )

    ChrTalk(
        0x0103,
        (
            '#0030390895V#023F这真是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_52B')

    def _loc_49B(): pass

    label('loc_49B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4CE',
    )

    ChrTalk(
        0x0109,
        (
            '#0180390896V#1064F这真是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_52B')

    def _loc_4CE(): pass

    label('loc_4CE')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4FC',
    )

    ChrTalk(
        0x0104,
        (
            '#0040390897V#033F这……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_52B')

    def _loc_4FC(): pass

    label('loc_4FC')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_52B',
    )

    ChrTalk(
        0x0106,
        (
            '#0050390898V#052F这家伙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_52B(): pass

    label('loc_52B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_563',
    )

    ChrTalk(
        0x0108,
        (
            '#0080390899V#072F这还真是精彩……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_681')

    def _loc_563(): pass

    label('loc_563')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_59B',
    )

    ChrTalk(
        0x0106,
        (
            '#0050390900V#555F果然令人吃惊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_681')

    def _loc_59B(): pass

    label('loc_59B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5DC',
    )

    ChrTalk(
        0x0104,
        (
            '#0040390901V#035F呼……\n',
            '真是压倒性的景象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_681')

    def _loc_5DC(): pass

    label('loc_5DC')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_61B',
    )

    ChrTalk(
        0x0109,
        (
            '#0180390902V#1060F一句话，真是太棒了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_681')

    def _loc_61B(): pass

    label('loc_61B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_651',
    )

    ChrTalk(
        0x0103,
        (
            '#0030390903V#020F……了不起啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_681')

    def _loc_651(): pass

    label('loc_651')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_681',
    )

    ChrTalk(
        0x0105,
        (
            '#0060390904V#1382F了不起……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_681(): pass

    label('loc_681')

    ChrTalk(
        0x0101,
        (
            '#0010390905V#1004F#6P想、想不到\n',
            '是这么大的都市……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010390906V#1015F果然真的……\n',
            '没人住在这里吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020390907V#1035F#6P嗯……大概。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020390908V#1040F看来在被封入异次元时\n',
            '大多数的居民好像都离开了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020390909V利贝尔国民的始祖\n',
            '大概就是那些人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0102, 500)

    @scena.Lambda('lambda_07AE')
    def lambda_07AE():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_07AE)

    ChrTalk(
        0x0101,
        (
            '#0010390910V#1020F#2P那、那就是说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010390911V我们的祖先曾经\n',
            '住在这座都市里！？',
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
        'loc_8A8',
    )

    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060390912V#1167F……我觉得很有可能。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390913V#1162F不光是在利贝尔，\n',
            '大崩坏之前文明的痕迹据说\n',
            '在各地都惊人地稀少……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B78')

    def _loc_8A8(): pass

    label('loc_8A8')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_936',
    )

    ChrTurnDirection(0x0108, 0x0101, 400)

    ChrTalk(
        0x0108,
        (
            '#0080390914V#074F很有可能吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080390915V#072F在卡尔瓦德也一样，\n',
            '大崩坏之前文明的痕迹据说\n',
            '在各地都惊人地稀少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B78')

    def _loc_936(): pass

    label('loc_936')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9CA',
    )

    ChrTurnDirection(0x0104, 0x0101, 400)

    ChrTalk(
        0x0104,
        (
            '#0040390916V#035F我觉得很有可能。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040390917V#030F在埃雷波尼亚也一样，\n',
            '大崩坏之前文明的痕迹据说\n',
            '在各地都惊人地稀少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B78')

    def _loc_9CA(): pass

    label('loc_9CA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A62',
    )

    ChrTurnDirection(0x0109, 0x0101, 400)

    ChrTalk(
        0x0109,
        (
            '#0180390918V#1065F……可能性应该很高。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180390919V#1063F大陆全境都是一样，\n',
            '大崩坏之前文明的痕迹据说\n',
            '在各地都惊人地稀少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B78')

    def _loc_A62(): pass

    label('loc_A62')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AF6',
    )

    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030390920V#026F应该很有可能呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030390921V#022F不光是在利贝尔，\n',
            '大崩坏之前文明的痕迹据说\n',
            '在各地都惊人地稀少哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B78')

    def _loc_AF6(): pass

    label('loc_AF6')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B78',
    )

    ChrTurnDirection(0x0107, 0x0101, 400)

    ChrTalk(
        0x0107,
        (
            '#0070390922V#063F说、说起来以前\n',
            '爷爷说过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070390923V大崩坏之前文明的痕迹据说\n',
            '在各地都惊人地稀少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B78(): pass

    label('loc_B78')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BEE',
    )

    ChrTalk(
        0x0106,
        (
            '#0050211830V#053F原来如此啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050390925V#050F在地面上没留下痕迹\n',
            '原来是因为以前住在天上啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E3C')

    def _loc_BEE(): pass

    label('loc_BEE')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C63',
    )

    ChrTalk(
        0x0107,
        (
            '#0070390926V#065F这、这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070390927V在地面上没留下痕迹\n',
            '原来是因为以前都住在天上啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E3C')

    def _loc_C63(): pass

    label('loc_C63')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CD7',
    )

    ChrTalk(
        0x0103,
        (
            '#0030390928V#026F原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030390929V#022F在地面上没留下痕迹\n',
            '原来是因为以前住在天上啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E3C')

    def _loc_CD7(): pass

    label('loc_CD7')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D51',
    )

    ChrTalk(
        0x0109,
        (
            '#0180390930V#1068F哈，原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180390931V#1060F在地面上没留下痕迹\n',
            '原来是因为以前住在天上啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E3C')

    def _loc_D51(): pass

    label('loc_D51')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DC9',
    )

    ChrTalk(
        0x0104,
        (
            '#0040390932V#035F呵，原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040390933V#030F在地面上没留下痕迹\n',
            '原来是因为以前住在天上啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E3C')

    def _loc_DC9(): pass

    label('loc_DC9')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E3C',
    )

    ChrTalk(
        0x0108,
        (
            '#0080390934V#074F呼，原来如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080390935V#070F在地面上没留下痕迹\n',
            '原来是因为以前住在天上啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E3C(): pass

    label('loc_E3C')

    ChrTalk(
        0x0101,
        (
            '#0010390936V#1007F#2P好、好像越说越\n',
            '觉得离奇了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010390937V#1017F话说回来……\n',
            '景色看上去这么棒，\n',
            '这里到底是什么地方？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020390938V#1043F#6P可能只是普通的了望台……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0EF5')
    def lambda_0EF5():
        CameraMove(-2200, 0, 8670, 1500)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0EF5)

    @scena.Lambda('lambda_0F0D')
    def lambda_0F0D():
        OP_67(0, 6140, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0F0D)

    ChrSetDirection(0x0102, 135, 400)
    WaitForThreadExit(0x0102, 0x0001)

    ChrTalk(
        0x0102,
        (
            '#0020390939V#1040F#5P前面有像终端一样的东西，\n',
            '我们去调查一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(-3950, 0, 6730, 0)
    OP_67(0, 5700, -10000, 0)
    CameraSetDistance(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    ChrSetPos(0x0000, -3950, 0, 6730, 225)
    ChrSetPos(0x0001, -3950, 0, 6730, 225)
    ChrSetPos(0x0002, -3950, 0, 6730, 225)
    ChrSetPos(0x0003, -3950, 0, 6730, 225)
    Sleep(500)

    SetScenaFlags(ScenaFlag(0x0440, 3, 0x2203))
    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0003 offset: 0x1011
@scena.Code('func_03_1011')
def func_03_1011():
    @scena.Lambda('lambda_1017')
    def lambda_1017():
        CameraMove(-7380, 0, 2100, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1017)

    ChrWalkTo(0x00FE, -5800, 0, 2180, 3000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)
    OP_62(0x0101, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    Fade(500)
    CameraMove(18150, 5000, 23940, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(4990, 0)
    OP_6C(0, 0)
    OP_6E(267, 0)

    Return()

# id: 0x0004 offset: 0x10A3
@scena.Code('func_04_10A3')
def func_04_10A3():
    ChrWalkTo(0x00FE, -3670, 0, 9350, 5000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0005 offset: 0x10BF
@scena.Code('func_05_10BF')
def func_05_10BF():
    ChrWalkTo(0x00FE, -10760, 10, 1800, 2000, 0x00)
    ChrWalkTo(0x00FE, -7090, 0, 2050, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0006 offset: 0x10EF
@scena.Code('func_06_10EF')
def func_06_10EF():
    ChrWalkTo(0x00FE, -4720, 0, 8460, 5000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0007 offset: 0x110B
@scena.Code('func_07_110B')
def func_07_110B():
    ChrWalkTo(0x00FE, -10760, 10, 1800, 2000, 0x00)
    ChrWalkTo(0x00FE, -8000, 170, 1920, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0008 offset: 0x113B
@scena.Code('func_08_113B')
def func_08_113B():
    ChrWalkTo(0x00FE, -6880, 0, 2070, 5000, 0x00)
    ChrWalkTo(0x00FE, -2920, 0, 7840, 5000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0009 offset: 0x116B
@scena.Code('func_09_116B')
def func_09_116B():
    ChrWalkTo(0x00FE, -10760, 10, 1800, 2000, 0x00)
    ChrWalkTo(0x00FE, -9310, 200, 1890, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x000A offset: 0x119B
@scena.Code('func_0A_119B')
def func_0A_119B():
    ChrWalkTo(0x00FE, -6880, 0, 2070, 5000, 0x00)
    ChrWalkTo(0x00FE, -4100, 0, 6880, 5000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x000B offset: 0x11CB
@scena.Code('func_0B_11CB')
def func_0B_11CB():
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
        'loc_11F0',
    )

    Call(0, 0x001C)
    Call(0, 0x001D)
    FadeIn(0, 0)
    Sleep(100)

    def _loc_11F0(): pass

    label('loc_11F0')

    Fade(500)
    CameraMove(1950, 2000, 2470, 0)
    OP_67(0, 4850, -10000, 0)
    CameraSetDistance(3920, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 2480, 2000, 500, 0)
    ChrSetPos(0x0102, 1480, 2000, 500, 0)
    ChrSetPos(0x00F8, 2450, 1600, -1400, 0)
    ChrSetPos(0x00F9, 1560, 1600, -1220, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 4, 0x2204)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_187B',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(300, 78, 34, 12)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S『光环轨道』西卡尔玛丽站\n',
            '\n',
            '\n',
            '※现在『光环轨道』的运行受到了\n',
            '  大幅度的限制。麻烦请您在本终端\n',
            '  手动输入我们可以为您提供的服务。\n',
            '\n',
            '※因现在是紧急时期，无需用『福音』\n',
            '  进行市民ID的认证。\n',
            '\n',
            '\n',
            '『利贝尔·方舟』市·交通管理中心',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010390940V#1020F这、这是什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010390941V出现了好几个令人\n',
            '在意的词汇呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020390942V#1035F#6P『光环轨道』……\n',
            '好像是某种交通工具呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020390943V#1040F而且，这座浮游都市的\n',
            '名字看来叫做『利贝尔·方舟』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 270, 400)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010390944V#1004F『利贝尔·方舟』……',
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
        'loc_14F4',
    )

    ChrTalk(
        0x0105,
        (
            '#0060390945V#1382F从发音来判断的话……\n',
            '应该是『利贝尔』的语源吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_169B')

    def _loc_14F4(): pass

    label('loc_14F4')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_154B',
    )

    ChrTalk(
        0x0104,
        (
            '#0040390946V#035F嗯，从发音来判断的话\n',
            '好像是『利贝尔』的语源吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_169B')

    def _loc_154B(): pass

    label('loc_154B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_15A0',
    )

    ChrTalk(
        0x0103,
        (
            '#0030390947V#027F从发音来判断的话……\n',
            '就是『利贝尔』的语源吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_169B')

    def _loc_15A0(): pass

    label('loc_15A0')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_15F3',
    )

    ChrTalk(
        0x0108,
        (
            '#0080390948V#070F从发音来判断的话\n',
            '好像是『利贝尔』的语源吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_169B')

    def _loc_15F3(): pass

    label('loc_15F3')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1647',
    )

    ChrTalk(
        0x0109,
        (
            '#0180390949V#1060F从发音来判断的话\n',
            '好像是『利贝尔』的语源吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_169B')

    def _loc_1647(): pass

    label('loc_1647')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_169B',
    )

    ChrTalk(
        0x0106,
        (
            '#0050390950V#051F从发音来判断的话……\n',
            '好像是『利贝尔』的语源吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_169B(): pass

    label('loc_169B')

    ChrTalk(
        0x0101,
        (
            '#0010390951V#1015F#5P原，原来如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0102, 90, 400)
    Sleep(300)

    ChrTalk(
        0x0102,
        (
            '#0020390952V#1042F#6P还有『福音』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020390953V看来对这里的市民来说\n',
            '是个很普通的东西呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020390954V#1043F大概是享受公共服务时\n',
            '所需要的个人身份证明兼认证终端……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010390955V#1007F啊，我感到头脑混乱了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010390956V#1006F总之没有『福音』也可以\n',
            '做一些事吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010390957V快点进行各项调查吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020390958V#1040F#6P明白──\n',
            '呼叫出可以提供的服务一览吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 0, 400)
    ChrSetDirection(0x0102, 0, 400)
    Sleep(500)

    FadeOut(300, 0, 100)
    SetScenaFlags(ScenaFlag(0x0440, 4, 0x2204))
    SetMessageWindowPos(300, 78, 34, 12)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            TxtCtl.Enter,
        ),
    )

    Jump('loc_1970')

    def _loc_187B(): pass

    label('loc_187B')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(330, 78, 34, 12)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S『光环轨道』西卡尔玛丽站\n',
            '\n',
            '\n',
            '※现在『光环轨道』的运行受到了\n',
            '  大幅度的限制，麻烦请您在本终端\n',
            '  手动输入我们可以为您提供的服务。\n',
            '\n',
            '※因现在是紧急时期，无需用『福音』\n',
            '  进行市民ID的认证。\n',
            '\n',
            '\n',
            '『利贝尔·方舟』市·交通管理中心',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1970(): pass

    label('loc_1970')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_197A(): pass

    label('loc_197A')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1F46',
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
        20,
        100,
        1,
        (
            TXT(0x00, '【卡尔玛丽向导】\n'),
            TXT(0x01, '【使用光环轨道】\n'),
            TXT(0x02, '【网络商城】\n'),
            TXT(0x03, '【解除门锁】\n'),
            TXT(0x04, '【停止服务】\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1A02'),
        (0x00000001, 'loc_1B80'),
        (0x00000002, 'loc_1C9D'),
        (0x00000003, 'loc_1DEC'),
        (0x00000004, 'loc_1F29'),
        (-1, 'loc_1F36'),
    )

    def _loc_1A02(): pass

    label('loc_1A02')

    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S『卡尔玛丽』是\n',
            '建造在利贝尔·方舟市西区的大型公园区域，\n',
            '是供市民们休闲的场所。\n',
            '\n',
            '由数十个单边３００亚矩的\n',
            '正六边形组成，\n',
            '是一次主题为『自然与文明的和谐』的\n',
            '大规模造园行动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S四个入口分别为『光环轨道』的\n',
            '『北卡尔玛丽站』、『东卡尔玛丽站』、\n',
            '『西卡尔玛丽站』、『南卡尔玛丽站』。\n',
            '\n',
            '从各站开始的巡回路线，\n',
            '各自通向风格迥异的地区，\n',
            '可以享受到不同的四季景观和植被风貌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F43')

    def _loc_1B80(): pass

    label('loc_1B80')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 6, 0x2206)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C39',
    )

    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S现在『光环轨道』的运行受到了\n',
            '大幅度的限制。\n',
            '\n',
            '要启动『西卡尔玛丽站』的\n',
            '紧急运行模式吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Menu(
        1,
        130,
        240,
        0,
        (
            TXT(0x00, '【启动】\n'),
            TXT(0x01, '【不启动】\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1C1A'),
        (0x00000001, 'loc_1C30'),
        (-1, 'loc_1C36'),
    )

    def _loc_1C1A(): pass

    label('loc_1C1A')

    OP_5F(0x0000)
    OP_5F(0x0001)
    OP_56(0x00)
    FadeIn(300, 0)
    Call(0, 0x000C)

    Return()

    def _loc_1C30(): pass

    label('loc_1C30')

    OP_5F(0x0001)

    Jump('loc_1C36')

    def _loc_1C36(): pass

    label('loc_1C36')

    Jump('loc_1C9A')

    def _loc_1C39(): pass

    label('loc_1C39')

    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S现在『光环轨道』的运行受到了\n',
            '大幅度的限制。\n',
            '\n',
            '『西卡尔玛丽站』的紧急运行\n',
            '模式已经启动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1C9A(): pass

    label('loc_1C9A')

    Jump('loc_1F43')

    def _loc_1C9D(): pass

    label('loc_1C9D')

    FadeIn(300, 0)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            TxtCtl.Enter,
        ),
    )

    OP_A9(0xF0)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S<FIXME>《レールハイロゥ》西カルマーレ駅　　　　　　\n',
            '\n',
            '※現在《レールハイロゥ》の運行に\n',
            '  大幅な制限が加えられています。  お手数ですが、当端末から\n',
            '  可能なサービスを手動で入力してください。\n',
            '\n',
            '※非常時につき、《ゴスペル》による\n',
            '  市民ＩＤの認証は必要ありません。\n',
            '\n',
            '《リベル＝アーク》市·交通管理センター',
            TxtCtl.Enter,
        ),
    )

    FadeOut(300, 0, 100)

    Jump('loc_1F43')

    def _loc_1DEC(): pass

    label('loc_1DEC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0441, 5, 0x220D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1EF4',
    )

    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S当『光环轨道』\n',
            '由于各种原因而无法使用时，\n',
            '可以解除车站周边大门的锁定\n',
            '并进入地下通道之中。\n',
            '\n',
            '因现在处于紧急时期，\n',
            '可以解除大门的锁定。\n',
            '\n',
            '要解除吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Menu(
        1,
        130,
        240,
        0,
        (
            TXT(0x00, '【解除】\n'),
            TXT(0x01, '【不解除】\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1EC0'),
        (0x00000001, 'loc_1EEB'),
        (-1, 'loc_1EF1'),
    )

    def _loc_1EC0(): pass

    label('loc_1EC0')

    OP_5F(0x0000)
    OP_5F(0x0001)
    OP_56(0x00)
    FadeIn(300, 0)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/C5901._SN', 103, 0, 0)
    IdleLoop()

    Jump('loc_1EF1')

    def _loc_1EEB(): pass

    label('loc_1EEB')

    OP_5F(0x0001)

    Jump('loc_1EF1')

    def _loc_1EF1(): pass

    label('loc_1EF1')

    Jump('loc_1F26')

    def _loc_1EF4(): pass

    label('loc_1EF4')

    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S现在，西卡尔玛丽站的\n',
            '大门锁定已经解除。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1F26(): pass

    label('loc_1F26')

    Jump('loc_1F43')

    def _loc_1F29(): pass

    label('loc_1F29')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1F43')

    def _loc_1F36(): pass

    label('loc_1F36')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1F43')

    def _loc_1F43(): pass

    label('loc_1F43')

    Jump('loc_197A')

    def _loc_1F46(): pass

    label('loc_1F46')

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
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(100, 0)
    Sleep(100)

    Fade(500)
    CameraMove(2020, 2000, 40, 0)
    OP_67(0, 5700, -10000, 0)
    CameraSetDistance(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    ChrSetPos(0x0000, 2020, 2000, 40, 180)
    ChrSetPos(0x0001, 2020, 2000, 40, 180)
    ChrSetPos(0x0002, 2020, 2000, 40, 180)
    ChrSetPos(0x0003, 2020, 2000, 40, 180)
    EventEnd(0x00)

    Return()

# id: 0x000C offset: 0x1FF4
@scena.Code('func_0C_1FF4')
def func_0C_1FF4():
    EventBegin(0x00)
    OP_72(0x0001, 0x0004)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 5, 0x2205)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2C99',
    )

    Fade(500)
    CameraMove(-7060, 5000, 19260, 0)
    OP_67(0, 8670, -10000, 0)
    CameraSetDistance(4960, 0)
    OP_6C(347000, 0)
    OP_6E(268, 0)
    ChrSetPos(0x0008, -25730, 5110, 21310, 90)
    OP_0D()
    OP_6F(0x0003, 0)
    OP_70(0x0003, 240)
    Sleep(500)

    @scena.Lambda('lambda_2070')
    def lambda_2070():
        CameraMove(17390, 5000, 16010, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2070)

    PlaySE(317, 0x00, 0x64)
    OP_73(0x0003)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(500)

    Fade(500)
    CameraMove(1980, 2000, 1300, 0)
    OP_67(0, 5050, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(0, 0)
    OP_6E(205, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010390959V#1004F#6P那、那是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020390960V#1044F#6P……有东西过来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    CameraMove(-7920, 5000, 21760, 0)
    OP_67(0, 9120, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_0D()

    @scena.Lambda('lambda_2180')
    def lambda_2180():
        CameraMove(3080, 5110, 21340, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2180)

    @scena.Lambda('lambda_2198')
    def lambda_2198():
        OP_67(0, 6030, -10000, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2198)

    OP_6F(0x0001, 500)
    OP_70(0x0001, 800)
    PlaySE(318, 0x00, 0x64)

    @scena.Lambda('lambda_21C3')
    def lambda_21C3():
        ChrWalkTo(0x00FE, 3140, 5110, 21050, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_21C3)

    Sleep(2000)

    CreateThread(0x0101, 0x01, 0x00, func_0D_340B)
    Sleep(500)

    CreateThread(0x0102, 0x01, 0x00, func_0E_3442)
    Sleep(500)

    CreateThread(0x00F8, 0x01, 0x00, func_0F_3479)
    Sleep(500)

    CreateThread(0x00F9, 0x01, 0x00, func_10_34B0)
    OP_73(0x0001)
    OP_23(0x013E)
    WaitForThreadExit(0x0101, 0x0000)
    OP_6F(0x0001, 800)
    OP_70(0x0001, 950)
    Sleep(500)

    PlaySE(107, 0x00, 0x64)
    OP_73(0x0001)
    TerminateThread(0x0101, 0x02)
    TerminateThread(0x0102, 0x02)
    TerminateThread(0x00F8, 0x02)
    TerminateThread(0x00F9, 0x02)

    ChrTalk(
        0x0101,
        (
            '#0010390961V#1004F#6P那、那是什么……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_22DA',
    )

    ChrTalk(
        0x0102,
        (
            '#0020390962V#1040F#6P看来这就是\n',
            '『光环轨道』了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020390963V是通过什么样的原理呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26D4')

    def _loc_22DA(): pass

    label('loc_22DA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2372',
    )

    ChrTalk(
        0x010F,
        (
            '#0100390964V#173F<FIXME>どうやらこれが\n',
            '《レールハイロゥ》のようだな。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390965V#178Fしかし一体\n',
            'どういう仕組みなのだろうか……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26D4')

    def _loc_2372(): pass

    label('loc_2372')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_23E5',
    )

    ChrTalk(
        0x0105,
        (
            '#0060390966V#1165F#6P看来这就是\n',
            '『光环轨道』了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390967V#1382F是通过什么样的原理呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26D4')

    def _loc_23E5(): pass

    label('loc_23E5')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_245C',
    )

    ChrTalk(
        0x0103,
        (
            '#0030390968V#026F#6P嗯……\n',
            '看来这就是『光环轨道』了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030390969V#020F是通过什么样的原理呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26D4')

    def _loc_245C(): pass

    label('loc_245C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_24DA',
    )

    ChrTalk(
        0x0106,
        (
            '#0050390970V#053F#6P呼，\n',
            '看来这就是『光环轨道』了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050390971V#555F虽然不知道是\n',
            '通过什么样的原理……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26D4')

    def _loc_24DA(): pass

    label('loc_24DA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2553',
    )

    ChrTalk(
        0x0108,
        (
            '#0080390972V#074F#6P呼呼。\n',
            '看来这就是『光环轨道』了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080390973V#070F虽然完全不懂是什么原理……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26D4')

    def _loc_2553(): pass

    label('loc_2553')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_25DB',
    )

    ChrTalk(
        0x0109,
        (
            '#0180390974V#1064F#6P哈……\n',
            '看来这就是『光环轨道』了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180390975V#1068F虽然完全搞不清楚\n',
            '是通过什么样的原理……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26D4')

    def _loc_25DB(): pass

    label('loc_25DB')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_264C',
    )

    ChrTalk(
        0x0104,
        (
            '#0040390976V#035F#6P呼，看来这就是\n',
            '『光环轨道』了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040390977V#030F虽然不了解其原理……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26D4')

    def _loc_264C(): pass

    label('loc_264C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_26D4',
    )

    ChrTalk(
        0x010B,
        (
            '#0090390978V#216F#5P<FIXME>ど、どうやらこれが\n',
            '《レールハイロゥ》みたいだけど……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090390979V一体どうなってんの？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_26D4(): pass

    label('loc_26D4')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_276A',
    )

    ChrTalk(
        0x0110,
        (
            '#0110390980V#278F<FIXME>……帝国を走る鉄道と\n',
            '雰囲気は似ているな。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110390981V#277F透明なレールというのが\n',
            'やや落ち着かんが……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B85')

    def _loc_276A(): pass

    label('loc_276A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_27F2',
    )

    ChrTalk(
        0x010B,
        (
            '#0090390982V#213F#6P……但感觉和帝国的\n',
            '铁路有点相似。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090390983V#413F不过，透明的轨道\n',
            '还真令人有点胆战心惊啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B85')

    def _loc_27F2(): pass

    label('loc_27F2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2874',
    )

    ChrTalk(
        0x0104,
        (
            '#0040390984V#030F#6P呼，好像是帝国\n',
            '铁路的进化版一样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040390985V#031F不过，透明的轨道\n',
            '还是相当惊险的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B85')

    def _loc_2874(): pass

    label('loc_2874')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_28F6',
    )

    ChrTalk(
        0x0109,
        (
            '#0180390986V#1064F#6P好像是一些国家使用的\n',
            '铁路的进化版。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180390987V#1068F透明的轨道\n',
            '很让人感到不安啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B85')

    def _loc_28F6(): pass

    label('loc_28F6')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2976',
    )

    ChrTalk(
        0x0108,
        (
            '#0080390988V#073F#6P像矿车一样\n',
            '在轨道上跑的交通工具啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080390989V#075F透明的轨道还真\n',
            '让人不放心啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B85')

    def _loc_2976(): pass

    label('loc_2976')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_29F4',
    )

    ChrTalk(
        0x0106,
        (
            '#0050390990V#555F#6P像矿车一样\n',
            '在轨道上跑的交通工具啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050390991V#551F透明的轨道真是\n',
            '感觉怪怪的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B85')

    def _loc_29F4(): pass

    label('loc_29F4')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2A70',
    )

    ChrTalk(
        0x0103,
        (
            '#0030390992V#020F#6P像矿车一样\n',
            '在轨道上跑的交通工具。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030390993V#524F透明的轨道\n',
            '总让人有点不安……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B85')

    def _loc_2A70(): pass

    label('loc_2A70')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2AE8',
    )

    ChrTalk(
        0x0105,
        (
            '#0060390994V#1164F#6P好像是帝国铁路的\n',
            '进化版一样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390995V这透明的轨道\n',
            '是用什么做出来呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B85')

    def _loc_2AE8(): pass

    label('loc_2AE8')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2B85',
    )

    ChrTalk(
        0x010F,
        (
            '#0100390996V#176F<FIXME>帝国で運用されている\n',
            '鉄道に似ているようだな。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390997V#178F透明なレールというのは\n',
            'さすがに落ち着かないが……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B85(): pass

    label('loc_2B85')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2C08',
    )

    ChrTalk(
        0x0107,
        (
            '#0070390998V#064F#6P说、说不定是\n',
            '在空中展开了某种力场\n',
            '所形成的轨道……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070390999V#067F了、了不起的技术啊～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C08(): pass

    label('loc_2C08')

    ChrTalk(
        0x0101,
        (
            '#0010391000V#1006F#6P嗯，虽然没什么头绪，\n',
            '不过既然是一种移动的手段，\n',
            '就没有不尝试的道理。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010391001V#1018F快点坐上去看看吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0440, 5, 0x2205))
    OP_28(0x009D, 0x01, 0x0020)

    Jump('loc_3365')

    def _loc_2C99(): pass

    label('loc_2C99')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0441, 2, 0x220A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2F1A',
    )

    CameraMove(-7060, 5000, 19260, 0)
    OP_67(0, 8670, -10000, 0)
    CameraSetDistance(4960, 0)
    OP_6C(347000, 0)
    OP_6E(268, 0)
    ChrSetPos(0x0008, -25730, 5110, 21310, 90)
    OP_0D()
    OP_6F(0x0003, 0)
    OP_70(0x0003, 240)
    Sleep(500)

    @scena.Lambda('lambda_2D09')
    def lambda_2D09():
        CameraMove(17390, 5000, 16010, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2D09)

    PlaySE(317, 0x00, 0x64)
    OP_73(0x0003)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(1000)

    Fade(500)
    CameraMove(1980, 2000, 1300, 0)
    OP_67(0, 5050, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(0, 0)
    OP_6E(205, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010391002V#1006F#6P来了……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Fade(500)
    CameraMove(-7920, 5000, 21760, 0)
    OP_67(0, 9120, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_0D()

    @scena.Lambda('lambda_2DE3')
    def lambda_2DE3():
        CameraMove(3080, 5110, 21340, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2DE3)

    @scena.Lambda('lambda_2DFB')
    def lambda_2DFB():
        OP_67(0, 6030, -10000, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2DFB)

    OP_6F(0x0001, 500)
    OP_70(0x0001, 800)
    PlaySE(318, 0x00, 0x64)

    @scena.Lambda('lambda_2E26')
    def lambda_2E26():
        ChrWalkTo(0x00FE, 3140, 5110, 21050, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2E26)

    CreateThread(0x0101, 0x01, 0x00, func_0D_340B)
    Sleep(500)

    CreateThread(0x0102, 0x01, 0x00, func_0E_3442)
    Sleep(500)

    CreateThread(0x00F8, 0x01, 0x00, func_0F_3479)
    Sleep(500)

    CreateThread(0x00F9, 0x01, 0x00, func_10_34B0)
    OP_73(0x0001)
    OP_23(0x013E)
    WaitForThreadExit(0x0101, 0x0000)
    OP_6F(0x0001, 800)
    OP_70(0x0001, 950)
    Sleep(300)

    PlaySE(107, 0x00, 0x64)
    OP_73(0x0001)
    TerminateThread(0x0101, 0x02)
    TerminateThread(0x0102, 0x02)
    TerminateThread(0x00F8, 0x02)
    TerminateThread(0x00F9, 0x02)

    ChrTalk(
        0x0101,
        (
            '#0010391003V#1006F#6P好了，这样一来总算\n',
            '可以使用这个东西了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020391004V#1040F#6P说得也是……\n',
            '马上试试吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0441, 2, 0x220A))

    Jump('loc_3365')

    def _loc_2F1A(): pass

    label('loc_2F1A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0441, 3, 0x220B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_312B',
    )

    Fade(500)
    CameraMove(-7060, 5000, 19260, 0)
    OP_67(0, 8670, -10000, 0)
    CameraSetDistance(4960, 0)
    OP_6C(347000, 0)
    OP_6E(268, 0)
    ChrSetPos(0x0008, -25730, 5110, 21310, 90)
    OP_0D()
    OP_6F(0x0003, 0)
    OP_70(0x0003, 240)
    Sleep(500)

    @scena.Lambda('lambda_2F8F')
    def lambda_2F8F():
        CameraMove(17390, 5000, 16010, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2F8F)

    PlaySE(317, 0x00, 0x64)
    OP_73(0x0003)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(1000)

    Fade(500)
    CameraMove(-7920, 5000, 21760, 0)
    OP_67(0, 9120, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_0D()

    @scena.Lambda('lambda_2FFC')
    def lambda_2FFC():
        CameraMove(3080, 5110, 21340, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2FFC)

    @scena.Lambda('lambda_3014')
    def lambda_3014():
        OP_67(0, 6030, -10000, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3014)

    OP_6F(0x0001, 500)
    OP_70(0x0001, 800)
    PlaySE(318, 0x00, 0x64)

    @scena.Lambda('lambda_303F')
    def lambda_303F():
        ChrWalkTo(0x00FE, 3140, 5110, 21050, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_303F)

    CreateThread(0x0101, 0x01, 0x00, func_0D_340B)
    Sleep(500)

    CreateThread(0x0102, 0x01, 0x00, func_0E_3442)
    Sleep(500)

    CreateThread(0x00F8, 0x01, 0x00, func_0F_3479)
    Sleep(500)

    CreateThread(0x00F9, 0x01, 0x00, func_10_34B0)
    OP_73(0x0001)
    OP_23(0x013E)
    WaitForThreadExit(0x0101, 0x0000)
    OP_6F(0x0001, 800)
    OP_70(0x0001, 950)
    Sleep(300)

    PlaySE(107, 0x00, 0x64)
    OP_73(0x0001)
    TerminateThread(0x0101, 0x02)
    TerminateThread(0x0102, 0x02)
    TerminateThread(0x00F8, 0x02)
    TerminateThread(0x00F9, 0x02)

    ChrTalk(
        0x0101,
        (
            '#0010391005V#1015F#6P嗯，现在可以来往于\n',
            '３个车站了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020391006V#1040F#6P嗯……\n',
            '变得相当方便了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0441, 3, 0x220B))

    Jump('loc_3365')

    def _loc_312B(): pass

    label('loc_312B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0441, 4, 0x220C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3365',
    )

    Fade(500)
    CameraMove(-7060, 5000, 19260, 0)
    OP_67(0, 8670, -10000, 0)
    CameraSetDistance(4960, 0)
    OP_6C(347000, 0)
    OP_6E(268, 0)
    ChrSetPos(0x0008, -25730, 5110, 21310, 90)
    OP_0D()
    OP_6F(0x0003, 0)
    OP_70(0x0003, 240)
    Sleep(500)

    @scena.Lambda('lambda_31A0')
    def lambda_31A0():
        CameraMove(17390, 5000, 16010, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_31A0)

    PlaySE(317, 0x00, 0x64)
    OP_73(0x0003)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(1000)

    Fade(500)
    CameraMove(-7920, 5000, 21760, 0)
    OP_67(0, 9120, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_0D()

    @scena.Lambda('lambda_320D')
    def lambda_320D():
        CameraMove(3080, 5110, 21340, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_320D)

    @scena.Lambda('lambda_3225')
    def lambda_3225():
        OP_67(0, 6030, -10000, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3225)

    OP_6F(0x0001, 500)
    OP_70(0x0001, 800)
    PlaySE(318, 0x00, 0x64)

    @scena.Lambda('lambda_3250')
    def lambda_3250():
        ChrWalkTo(0x00FE, 3140, 5110, 21050, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_3250)

    CreateThread(0x0101, 0x01, 0x00, func_0D_340B)
    Sleep(500)

    CreateThread(0x0102, 0x01, 0x00, func_0E_3442)
    Sleep(500)

    CreateThread(0x00F8, 0x01, 0x00, func_0F_3479)
    Sleep(500)

    CreateThread(0x00F9, 0x01, 0x00, func_10_34B0)
    OP_73(0x0001)
    OP_23(0x013E)
    WaitForThreadExit(0x0101, 0x0000)
    OP_6F(0x0001, 800)
    OP_70(0x0001, 950)
    Sleep(300)

    PlaySE(107, 0x00, 0x64)
    OP_73(0x0001)
    TerminateThread(0x0101, 0x02)
    TerminateThread(0x0102, 0x02)
    TerminateThread(0x00F8, 0x02)
    TerminateThread(0x00F9, 0x02)

    ChrTalk(
        0x0102,
        (
            '#0020391007V#1035F#6P好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020391008V#1040F现在从『卡尔玛丽』\n',
            '到『中枢塔』都能\n',
            '方便地来回了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010391009V#1007F#6P呼……好长的距离啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0441, 4, 0x220C))
    OP_28(0x009F, 0x01, 0x0002)

    def _loc_3365(): pass

    label('loc_3365')

    SetScenaFlags(ScenaFlag(0x0440, 6, 0x2206))
    OP_28(0x009D, 0x01, 0x0010)
    FadeOut(1000, 0, -1)
    OP_0D()
    ChrSetPos(0x0000, 3060, 5000, 18520, 0)
    ChrSetPos(0x0001, 3060, 5000, 18520, 0)
    ChrSetPos(0x0002, 3060, 5000, 18520, 0)
    ChrSetPos(0x0003, 3060, 5000, 18520, 0)
    CameraMove(3060, 5000, 18520, 0)
    OP_67(0, 5700, -10000, 0)
    CameraSetDistance(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x000D offset: 0x340B
@scena.Code('func_0D_340B')
def func_0D_340B():
    ChrSetPos(0x00FE, 13930, 4000, 17320, 270)
    ChrWalkTo(0x00FE, 2620, 5000, 18360, 5000, 0x00)

    @scena.Lambda('lambda_3436')
    def lambda_3436():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_3436')

    DispatchAsync2(0x00FE, 0x0002, lambda_3436)

    Return()

# id: 0x000E offset: 0x3442
@scena.Code('func_0E_3442')
def func_0E_3442():
    ChrSetPos(0x00FE, 13930, 4000, 17320, 270)
    ChrWalkTo(0x00FE, 3630, 5000, 18380, 5000, 0x00)

    @scena.Lambda('lambda_346D')
    def lambda_346D():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_346D')

    DispatchAsync2(0x00FE, 0x0002, lambda_346D)

    Return()

# id: 0x000F offset: 0x3479
@scena.Code('func_0F_3479')
def func_0F_3479():
    ChrSetPos(0x00FE, 13930, 4000, 17320, 270)
    ChrWalkTo(0x00FE, 2240, 5000, 17190, 5000, 0x00)

    @scena.Lambda('lambda_34A4')
    def lambda_34A4():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_34A4')

    DispatchAsync2(0x00FE, 0x0002, lambda_34A4)

    Return()

# id: 0x0010 offset: 0x34B0
@scena.Code('func_10_34B0')
def func_10_34B0():
    ChrSetPos(0x00FE, 13930, 4000, 17320, 270)
    ChrWalkTo(0x00FE, 4070, 5000, 17190, 5000, 0x00)

    @scena.Lambda('lambda_34DB')
    def lambda_34DB():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_34DB')

    DispatchAsync2(0x00FE, 0x0002, lambda_34DB)

    Return()

# id: 0x0011 offset: 0x34E7
@scena.Code('func_11_34E7')
def func_11_34E7():
    EventBegin(0x00)
    CameraMove(1950, 2000, 2470, 0)
    OP_67(0, 4850, -10000, 0)
    CameraSetDistance(3920, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 2480, 2000, 500, 0)
    ChrSetPos(0x0102, 1480, 2000, 500, 0)
    ChrSetPos(0x00F8, 2450, 1600, -1400, 0)
    ChrSetPos(0x00F9, 1560, 1600, -1220, 0)
    FadeIn(1000, 0)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('合成音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '本站附近的大门锁定\n',
            '已经解除。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '地下通道７８号已经可以使用了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    Fade(500)
    CameraMove(2020, 2000, 40, 0)
    OP_67(0, 5700, -10000, 0)
    CameraSetDistance(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    ChrSetPos(0x0000, 2020, 2000, 40, 180)
    ChrSetPos(0x0001, 2020, 2000, 40, 180)
    ChrSetPos(0x0002, 2020, 2000, 40, 180)
    ChrSetPos(0x0003, 2020, 2000, 40, 180)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x0441, 5, 0x220D))
    OP_28(0x009D, 0x01, 0x0080)
    EventEnd(0x00)

    Return()

# id: 0x0012 offset: 0x3671
@scena.Code('func_12_3671')
def func_12_3671():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 6, 0x2206)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_367A',
    )

    Return()

    def _loc_367A(): pass

    label('loc_367A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 7, 0x2207)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0441, 0, 0x2208)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0441, 1, 0x2209)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3ACF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0441, 6, 0x220E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3A42',
    )

    EventBegin(0x00)
    Fade(500)
    CameraMove(3080, 5110, 21340, 0)
    OP_67(0, 6030, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 2620, 5000, 18360, 0)
    ChrSetPos(0x0102, 3630, 5000, 18380, 0)
    ChrSetPos(0x00F8, 2240, 5000, 17190, 0)
    ChrSetPos(0x00F9, 4070, 5000, 17190, 0)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('合成音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '现在其它车站的紧急运行\n',
            '模式尚未启动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    TalkSetChrName('合成音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '『光环轨道』无法使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_37DA',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x18, 0x1B, 0x000000FA, 0x00)

    Jump('loc_380E')

    def _loc_37DA(): pass

    label('loc_37DA')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_37FC',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)

    Jump('loc_380E')

    def _loc_37FC(): pass

    label('loc_37FC')

    OP_62(0x00F8, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)

    def _loc_380E(): pass

    label('loc_380E')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3835',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x18, 0x1B, 0x000000FA, 0x00)

    Jump('loc_3869')

    def _loc_3835(): pass

    label('loc_3835')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3857',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)

    Jump('loc_3869')

    def _loc_3857(): pass

    label('loc_3857')

    OP_62(0x00F9, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)

    def _loc_3869(): pass

    label('loc_3869')

    Sleep(1500)

    OP_63(0x0101)
    OP_63(0x0102)
    OP_63(0x00F8)
    OP_63(0x00F9)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010391010V#1019F#6P……怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020391011V#1035F#6P……看来不启动其他\n',
            '车站的『紧急运行模式』的话，\n',
            '就不能使用这个来移动了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020391012V#1040F很遗憾，\n',
            '现在只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010391013V#1007F#6P唔～……\n',
            '害我空欢喜了一场。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010391014V#1015F没办法，先找其他路线吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0441, 6, 0x220E))
    OP_28(0x009D, 0x01, 0x0040)
    FadeOut(1000, 0, -1)
    OP_0D()
    ChrSetPos(0x0000, 3060, 5000, 18520, 0)
    ChrSetPos(0x0001, 3060, 5000, 18520, 0)
    ChrSetPos(0x0002, 3060, 5000, 18520, 0)
    ChrSetPos(0x0003, 3060, 5000, 18520, 0)
    CameraMove(3060, 5000, 18520, 0)
    OP_67(0, 5700, -10000, 0)
    CameraSetDistance(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Jump('loc_3ACC')

    def _loc_3A42(): pass

    label('loc_3A42')

    EventBegin(0x02)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('合成音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '现在其它车站的紧急运行\n',
            '模式尚未启动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    TalkSetChrName('合成音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '『光环轨道』无法使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    def _loc_3ACC(): pass

    label('loc_3ACC')

    Jump('loc_3DAA')

    def _loc_3ACF(): pass

    label('loc_3ACF')

    EventBegin(0x00)
    Fade(500)
    CameraMove(3080, 5110, 21340, 0)
    OP_67(0, 6030, -10000, 0)
    CameraSetDistance(5000, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 2620, 5000, 18360, 0)
    ChrSetPos(0x0102, 3630, 5000, 18380, 0)
    ChrSetPos(0x00F8, 2240, 5000, 17190, 0)
    ChrSetPos(0x00F9, 4070, 5000, 17190, 0)
    OP_0D()
    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
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

    OP_CC(0x00, 0x00, 0x000A, 0x000A, 0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 7, 0x2207)),
            Expr.Return,
        ),
        'loc_3BB0',
    )

    OP_CC(0x01, 0x00, '【第３５克雷德尔站】')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_3BB0(): pass

    label('loc_3BB0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0441, 0, 0x2208)),
            Expr.Return,
        ),
        'loc_3BD9',
    )

    OP_CC(0x01, 0x00, '【第７法克特里亚站】')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x2),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_3BD9(): pass

    label('loc_3BD9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0441, 1, 0x2209)),
            Expr.Return,
        ),
        'loc_3BFC',
    )

    OP_CC(0x01, 0x00, '【中枢塔前站】')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x4),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_3BFC(): pass

    label('loc_3BFC')

    OP_CC(0x01, 0x00, '【放弃使用】')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x8),
            Expr.Or2,
            Expr.Return,
        ),
    )

    OP_CC(0x02, 0x00)
    MenuEnd(0x0000)
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_3C3F',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3CC1')

    def _loc_3C3F(): pass

    label('loc_3C3F')

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_3C49(): pass

    label('loc_3C49')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3CC1',
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3C63',
    )

    Jump('loc_3CC1')

    def _loc_3C63(): pass

    label('loc_3C63')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3CB4',
    )

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_3C9D',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x2),
            Expr.Div2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3C9A',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_3C9A(): pass

    label('loc_3C9A')

    Jump('loc_3CB4')

    def _loc_3C9D(): pass

    label('loc_3C9D')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x2),
            Expr.Div2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Jump('loc_3C63')

    def _loc_3CB4(): pass

    label('loc_3CB4')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_3C49')

    def _loc_3CC1(): pass

    label('loc_3CC1')

    MapSetFlags(0x00100000)

    Switch(
        (
            (Expr.PushReg, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_3CDF'),
        (0x00000001, 'loc_3D1D'),
        (0x00000002, 'loc_3D5B'),
        (0x00000003, 'loc_3D99'),
        (-1, 'loc_3D9C'),
    )

    def _loc_3CDF(): pass

    label('loc_3CDF')

    SetScenaFlags(ScenaFlag(0x0442, 0, 0x2210))
    SetScenaFlags(ScenaFlag(0x0442, 5, 0x2215))
    CreateThread(0x0101, 0x01, 0x00, func_13_3DAB)

    @scena.Lambda('lambda_3CF2')
    def lambda_3CF2():
        OP_67(0, 5450, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3CF2)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0000)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C6010._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_3D9C')

    def _loc_3D1D(): pass

    label('loc_3D1D')

    SetScenaFlags(ScenaFlag(0x0442, 0, 0x2210))
    SetScenaFlags(ScenaFlag(0x0442, 6, 0x2216))
    CreateThread(0x0101, 0x01, 0x00, func_13_3DAB)

    @scena.Lambda('lambda_3D30')
    def lambda_3D30():
        OP_67(0, 5450, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3D30)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0000)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C6010._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_3D9C')

    def _loc_3D5B(): pass

    label('loc_3D5B')

    SetScenaFlags(ScenaFlag(0x0442, 0, 0x2210))
    SetScenaFlags(ScenaFlag(0x0442, 7, 0x2217))
    CreateThread(0x0101, 0x01, 0x00, func_13_3DAB)

    @scena.Lambda('lambda_3D6E')
    def lambda_3D6E():
        OP_67(0, 5450, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3D6E)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0000)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C6010._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_3D9C')

    def _loc_3D99(): pass

    label('loc_3D99')

    Jump('loc_3D9C')

    def _loc_3D9C(): pass

    label('loc_3D9C')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    EventEnd(0x00)
    def _loc_3DAA(): pass

    label('loc_3DAA')

    Return()

# id: 0x0013 offset: 0x3DAB
@scena.Code('func_13_3DAB')
def func_13_3DAB():
    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    CreateThread(0x0101, 0x02, 0x00, func_14_3EA3)
    Sleep(800)

    CreateThread(0x0102, 0x01, 0x00, func_14_3EA3)
    Sleep(800)

    CreateThread(0x00F8, 0x01, 0x00, func_14_3EA3)
    Sleep(800)

    CreateThread(0x00F9, 0x01, 0x00, func_14_3EA3)
    Sleep(1500)

    OP_6F(0x0001, 950)
    OP_70(0x0001, 1100)
    Sleep(300)

    PlaySE(107, 0x00, 0x64)
    OP_73(0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0442, 7, 0x2217)),
            Expr.Return,
        ),
        'loc_3E57',
    )

    OP_6F(0x0001, 1100)
    OP_70(0x0001, 1300)
    PlaySE(318, 0x00, 0x64)

    @scena.Lambda('lambda_3E22')
    def lambda_3E22():
        CameraMove(8300, 5000, 21350, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3E22)

    @scena.Lambda('lambda_3E3A')
    def lambda_3E3A():
        OP_6C(12000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3E3A)

    @scena.Lambda('lambda_3E4A')
    def lambda_3E4A():
        CameraSetDistance(5000, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_3E4A)

    Jump('loc_3E92')

    def _loc_3E57(): pass

    label('loc_3E57')

    OP_6F(0x0001, 300)
    OP_70(0x0001, 500)
    PlaySE(318, 0x00, 0x64)

    @scena.Lambda('lambda_3E70')
    def lambda_3E70():
        CameraMove(-2860, 5000, 21710, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3E70)

    @scena.Lambda('lambda_3E88')
    def lambda_3E88():
        CameraSetDistance(5000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3E88)

    def _loc_3E92(): pass

    label('loc_3E92')

    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()

    Return()

# id: 0x0014 offset: 0x3EA3
@scena.Code('func_14_3EA3')
def func_14_3EA3():
    ChrWalkTo(0x00FE, 3080, 5000, 19030, 2000, 0x00)
    ChrWalkTo(0x00FE, 3010, 5110, 20330, 2000, 0x00)

    @scena.Lambda('lambda_3ED1')
    def lambda_3ED1():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 800)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_3ED1)

    ChrWalkTo(0x00FE, 3100, 5110, 24220, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0015 offset: 0x3EF7
@scena.Code('func_15_3EF7')
def func_15_3EF7():
    EventBegin(0x00)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    CameraMove(3100, 5110, 23900, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 3050, 5110, 21510, 180)
    ChrSetPos(0x0102, 3050, 5110, 21510, 180)
    ChrSetPos(0x00F8, 3050, 5110, 21510, 180)
    ChrSetPos(0x00F9, 3050, 5110, 21510, 180)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0442, 1, 0x2211)),
            Expr.Return,
        ),
        'loc_4000',
    )

    CameraMove(-9950, 5000, 20680, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_6F(0x0001, 500)
    OP_70(0x0001, 800)
    PlaySE(318, 0x00, 0x64)

    @scena.Lambda('lambda_3FEB')
    def lambda_3FEB():
        CameraMove(2890, 5000, 22450, 5500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3FEB)

    Jump('loc_4078')

    def _loc_4000(): pass

    label('loc_4000')

    CameraMove(12690, 5000, 20450, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(348000, 0)
    OP_6E(262, 0)
    OP_6F(0x0001, 1300)
    OP_70(0x0001, 1600)
    PlaySE(318, 0x00, 0x64)

    @scena.Lambda('lambda_4056')
    def lambda_4056():
        CameraMove(2890, 5000, 22450, 5500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_4056)

    @scena.Lambda('lambda_406E')
    def lambda_406E():
        OP_6C(0, 5500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_406E)

    def _loc_4078(): pass

    label('loc_4078')

    ClearScenaFlags(ScenaFlag(0x0442, 0, 0x2210))
    ClearScenaFlags(ScenaFlag(0x0442, 1, 0x2211))
    ClearScenaFlags(ScenaFlag(0x0442, 2, 0x2212))
    ClearScenaFlags(ScenaFlag(0x0442, 3, 0x2213))
    FadeIn(1000, 0)
    OP_73(0x0001)
    OP_23(0x013E)
    OP_6F(0x0001, 800)
    OP_70(0x0001, 950)
    Sleep(300)

    PlaySE(107, 0x00, 0x64)
    OP_73(0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0441, 7, 0x220F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_494E',
    )

    CreateThread(0x0101, 0x01, 0x00, func_16_4A58)
    Sleep(800)

    CreateThread(0x0102, 0x01, 0x00, func_17_4AAF)
    Sleep(800)

    @scena.Lambda('lambda_40D4')
    def lambda_40D4():
        CameraMove(3100, 5000, 18850, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_40D4)

    @scena.Lambda('lambda_40EC')
    def lambda_40EC():
        CameraSetDistance(4000, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_40EC)

    CreateThread(0x00F8, 0x01, 0x00, func_18_4B01)
    Sleep(800)

    CreateThread(0x00F9, 0x01, 0x00, func_19_4B53)
    WaitForThreadExit(0x00F9, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010391015V#1004F#4P好、好像一转眼\n',
            '就到了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020391016V#1035F#6P速度很快，\n',
            '却几乎没有摇晃……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020391017V#1040F真是了不起的技术。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010391018V#1015F#4P确实如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010391019V#1016F不过难得有那么棒的景色，\n',
            '真想它能跑得慢一点，\n',
            '让我好好欣赏一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4299',
    )

    ChrTalk(
        0x010B,
        (
            '#0090391020V#413F#5P真是的……\n',
            '你还真是悠哉啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090391021V#210F……不过确实也\n',
            '有点可惜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4494')

    def _loc_4299(): pass

    label('loc_4299')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_42DF',
    )

    ChrTalk(
        0x0107,
        (
            '#0070391022V#067F#5P嘿嘿……\n',
            '的确可以这么说呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4494')

    def _loc_42DF(): pass

    label('loc_42DF')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4320',
    )

    ChrTalk(
        0x0105,
        (
            '#0060391023V#1168F#5P呵呵……\n',
            '确实是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4494')

    def _loc_4320(): pass

    label('loc_4320')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_435B',
    )

    ChrTalk(
        0x0103,
        (
            '#0030391024V#021F#5P呵呵……有道理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4494')

    def _loc_435B(): pass

    label('loc_435B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4393',
    )

    ChrTalk(
        0x0109,
        (
            '#0180391025V#1061F#5P哈哈，没错～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4494')

    def _loc_4393(): pass

    label('loc_4393')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_43D0',
    )

    ChrTalk(
        0x0104,
        (
            '#0040391026V#031F#5P呵呵……我有同感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4494')

    def _loc_43D0(): pass

    label('loc_43D0')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4418',
    )

    ChrTalk(
        0x010F,
        (
            '#0100391027V#171F<FIXME>ふふ……\n',
            'それもそうだな。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4494')

    def _loc_4418(): pass

    label('loc_4418')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4451',
    )

    ChrTalk(
        0x0108,
        (
            '#0080391028V#071F#5P哈哈……没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4494')

    def _loc_4451(): pass

    label('loc_4451')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4494',
    )

    ChrTalk(
        0x0106,
        (
            '#0050391029V#051F<FIXME>へっ……\n',
            'まあ確かにな。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4494(): pass

    label('loc_4494')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4536',
    )

    ChrTalk(
        0x0110,
        (
            '#0110391030V#278F<FIXME>だが、これのおかげで\n',
            '探索が楽になりそうだ。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110391031V#277F新しい駅を見つけたら\n',
            'すぐに使えるようにすべきだろう。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4948')

    def _loc_4536(): pass

    label('loc_4536')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_45B5',
    )

    ChrTalk(
        0x0106,
        (
            '#0050391032V#051F#5P不过，多亏有这东西，\n',
            '探索变得轻松许多了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050391033V发现了新的车站\n',
            '就赶紧启用吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4948')

    def _loc_45B5(): pass

    label('loc_45B5')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_462E',
    )

    ChrTalk(
        0x0108,
        (
            '#0080391034V#070F#5P不过，有了这个，\n',
            '探索就方便得多了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080391035V发现了新的车站\n',
            '就赶紧启用吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4948')

    def _loc_462E(): pass

    label('loc_462E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_46D8',
    )

    ChrTalk(
        0x010F,
        (
            '#0100391036V#179F<FIXME>だが、これのおかげで\n',
            'ずいぶん探索が楽になりそうだ。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100391037V#170F新しい駅を発見したら\n',
            'すぐに使えるようにしてしまおう。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4948')

    def _loc_46D8(): pass

    label('loc_46D8')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4758',
    )

    ChrTalk(
        0x0104,
        (
            '#0040391038V#035F#5P呵呵，有了这个\n',
            '探索就方便得多了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040391039V#030F发现了新的车站\n',
            '还真想赶紧启用啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4948')

    def _loc_4758(): pass

    label('loc_4758')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_47D0',
    )

    ChrTalk(
        0x0109,
        (
            '#0180391040V#1060F#5P不过，有了这个\n',
            '探索就方便得多了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180391041V发现了新的车站\n',
            '就赶紧启用吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4948')

    def _loc_47D0(): pass

    label('loc_47D0')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4847',
    )

    ChrTalk(
        0x0103,
        (
            '#0030391042V#027F#5P不过，有了这个\n',
            '探索就方便得多了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030391043V发现了新的车站\n',
            '就赶紧启用吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4948')

    def _loc_4847(): pass

    label('loc_4847')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_48C9',
    )

    ChrTalk(
        0x0105,
        (
            '#0060391044V#1167F#5P不过，有了这个\n',
            '探索就方便得多了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060391045V#1168F发现了新的车站\n',
            '还真想赶紧启用呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4948')

    def _loc_48C9(): pass

    label('loc_48C9')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4948',
    )

    ChrTalk(
        0x0107,
        (
            '#0070391046V#061F#5P嘿嘿，不过有了这个\n',
            '探索就轻松许多了阿⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070391047V#560F发现了新的车站\n',
            '就赶快启用吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4948(): pass

    label('loc_4948')

    SetScenaFlags(ScenaFlag(0x0441, 7, 0x220F))

    Jump('loc_49A6')

    def _loc_494E(): pass

    label('loc_494E')

    CreateThread(0x0101, 0x01, 0x00, func_16_4A58)
    Sleep(800)

    CreateThread(0x0102, 0x01, 0x00, func_17_4AAF)
    Sleep(800)

    @scena.Lambda('lambda_496C')
    def lambda_496C():
        CameraMove(3100, 5000, 18850, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_496C)

    @scena.Lambda('lambda_4984')
    def lambda_4984():
        CameraSetDistance(4000, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_4984)

    CreateThread(0x00F8, 0x01, 0x00, func_18_4B01)
    Sleep(800)

    CreateThread(0x00F9, 0x01, 0x00, func_19_4B53)
    Sleep(500)

    def _loc_49A6(): pass

    label('loc_49A6')

    FadeOut(1000, 0, -1)
    OP_0D()
    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x0001, 0xFF)
    TerminateThread(0x0002, 0xFF)
    TerminateThread(0x0003, 0xFF)
    ChrSetPos(0x0000, 3060, 5000, 18520, 180)
    ChrSetPos(0x0001, 3060, 5000, 18520, 180)
    ChrSetPos(0x0002, 3060, 5000, 18520, 180)
    ChrSetPos(0x0003, 3060, 5000, 18520, 180)
    CameraMove(3060, 5000, 18520, 0)
    OP_67(0, 5700, -10000, 0)
    CameraSetDistance(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)
    MapClearFlags(0x00100000)

    Return()

# id: 0x0016 offset: 0x4A58
@scena.Code('func_16_4A58')
def func_16_4A58():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_4A6E')
    def lambda_4A6E():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_4A6E)

    ChrWalkTo(0x00FE, 3100, 5000, 18910, 2000, 0x00)
    ChrWalkTo(0x00FE, 3790, 5000, 17270, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)
    ChrClearFlags(0x00FE, 0x0080)

    Return()

# id: 0x0017 offset: 0x4AAF
@scena.Code('func_17_4AAF')
def func_17_4AAF():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_4AC5')
    def lambda_4AC5():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_4AC5)

    ChrWalkTo(0x00FE, 3100, 5000, 18910, 2000, 0x00)
    ChrWalkTo(0x00FE, 2550, 5000, 17250, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0018 offset: 0x4B01
@scena.Code('func_18_4B01')
def func_18_4B01():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_4B17')
    def lambda_4B17():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_4B17)

    ChrWalkTo(0x00FE, 3160, 5000, 19120, 2000, 0x00)
    ChrWalkTo(0x00FE, 4230, 5000, 18440, 2000, 0x00)
    ChrSetDirection(0x00FE, 225, 400)

    Return()

# id: 0x0019 offset: 0x4B53
@scena.Code('func_19_4B53')
def func_19_4B53():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_4B69')
    def lambda_4B69():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_4B69)

    ChrWalkTo(0x00FE, 3160, 5000, 19120, 2000, 0x00)
    ChrWalkTo(0x00FE, 1970, 5000, 18340, 2000, 0x00)
    ChrSetDirection(0x00FE, 135, 400)

    Return()

# id: 0x001A offset: 0x4BA5
@scena.Code('func_1A_4BA5')
def func_1A_4BA5():
    EventBegin(0x00)
    Fade(1000)
    CameraMove(-13000, 0, 2000, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_89(0x0101, -12000, 0, 2000, 90)
    OP_89(0x0102, -13000, 0, 3000, 90)
    OP_89(0x00F8, -13000, 0, 1000, 90)
    OP_89(0x00F9, -14000, 0, 2000, 90)
    OP_0D()
    Sleep(100)

    MapSetFlags(0x00100000)
    PlaySE(235, 0x00, 0x64)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 1200)

    @scena.Lambda('lambda_4C51')
    def lambda_4C51():
        CameraMove(-13000, -25000, 490, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4C51)

    @scena.Lambda('lambda_4C69')
    def lambda_4C69():
        OP_67(0, 3890, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4C69)

    @scena.Lambda('lambda_4C81')
    def lambda_4C81():
        CameraSetDistance(5200, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_4C81)

    Sleep(4000)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_23(0x01C3)
    Sleep(500)

    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    NewScene('ED6_DT21/C5901._SN', 101, 0, 0)
    IdleLoop()

    Return()

# id: 0x001B offset: 0x4CB0
@scena.Code('func_1B_4CB0')
def func_1B_4CB0():
    EventBegin(0x00)
    CameraMove(-13000, -12750, 490, 0)
    OP_67(0, 3890, -10000, 0)
    CameraSetDistance(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    OP_6F(0x0000, 300)
    Yield()
    OP_89(0x0101, -12000, -23000, 2000, 90)
    OP_89(0x0102, -13000, -23000, 3000, 90)
    OP_89(0x00F8, -13000, -23000, 1000, 90)
    OP_89(0x00F9, -14000, -23000, 2000, 90)
    PlaySE(235, 0x00, 0x64)
    FadeIn(1000, 0)
    OP_70(0x0000, 0)

    @scena.Lambda('lambda_4D56')
    def lambda_4D56():
        CameraMove(-13000, 0, 2000, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_4D56)

    @scena.Lambda('lambda_4D6E')
    def lambda_4D6E():
        OP_67(0, 3880, -10000, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4D6E)

    Sleep(4000)

    OP_24(0x00EB, 0x5A)
    Sleep(50)

    OP_24(0x00EB, 0x50)
    Sleep(50)

    OP_24(0x00EB, 0x46)
    Sleep(50)

    OP_24(0x00EB, 0x3C)
    Sleep(50)

    OP_24(0x00EB, 0x32)
    Sleep(50)

    OP_24(0x00EB, 0x28)
    Sleep(50)

    OP_24(0x00EB, 0x1E)
    Sleep(50)

    OP_24(0x00EB, 0x14)
    Sleep(50)

    OP_24(0x00EB, 0x0A)
    Sleep(50)

    OP_23(0x00EB)
    OP_73(0x0000)
    Sleep(200)

    Fade(500)
    CameraMove(-7000, 0, 2000, 0)
    OP_67(0, 5700, -10000, 0)
    CameraSetDistance(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    ChrSetPos(0x0000, -7000, 0, 2000, 90)
    ChrSetPos(0x0001, -7000, 0, 2000, 90)
    ChrSetPos(0x0002, -7000, 0, 2000, 90)
    ChrSetPos(0x0003, -7000, 0, 2000, 90)
    OP_0D()
    EventEnd(0x00)

    Return()

# id: 0x001C offset: 0x4E6B
@scena.Code('func_1C_4E6B')
def func_1C_4E6B():
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
        (0x00000000, 'loc_4EE5'),
        (0x00000001, 'loc_4EEB'),
        (-1, 'loc_4EF1'),
    )

    def _loc_4EE5(): pass

    label('loc_4EE5')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_4EF1')

    def _loc_4EEB(): pass

    label('loc_4EEB')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_4EF1')

    def _loc_4EF1(): pass

    label('loc_4EF1')

    Return()

# id: 0x001D offset: 0x4EF2
@scena.Code('func_1D_4EF2')
def func_1D_4EF2():
    FadeOut(0, 0, -1)
    CameraMove(-545830, 30000, 755590, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(315000, 0)
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
            ChrTable['科洛丝'],
            ChrTable['奥利维尔'],
            ChrTable['提妲'],
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

# id: 0x001E offset: 0x4F83
@scena.Code('func_1E_4F83')
def func_1E_4F83():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '≡ 前面的月台\n',
            '　　　西卡尔玛丽站',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
