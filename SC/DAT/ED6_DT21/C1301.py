import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C1301_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1301   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'C1301.x'
    header.mapIndex       = 52
    header.bgm            = 89
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
        ('ED6_DT07/CH01600._CH', 'ED6_DT07/CH01600P._CP'),
        ('ED6_DT27/CH03570._CH', 'ED6_DT27/CH03570P._CP'),
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT07/CH02070._CH', 'ED6_DT07/CH02070P._CP'),
        ('ED6_DT06/CH20063._CH', 'ED6_DT06/CH20063P._CP'),
        ('ED6_DT06/CH20064._CH', 'ED6_DT06/CH20064P._CP'),
    ]

# id: 0x10001 offset: 0xDA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '守备队长',
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
            name                = '穆拉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '朵洛希',
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
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
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
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0180,
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
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0180,
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
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0180,
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
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0180,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x1FA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x1FA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x1FA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -11400,
            triggerZ            = 4000,
            triggerY            = -2400,
            triggerRange        = 1500,
            actorX              = -8930,
            actorZ              = 6520,
            actorY              = -880,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0013,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -9150,
            triggerZ            = 5540,
            triggerY            = -590,
            triggerRange        = 1000,
            actorX              = -10940,
            actorZ              = 5000,
            actorY              = -1870,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0018,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x242
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_25C',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    Event(0, func_02_26F)

    Jump('loc_268')

    def _loc_25C(): pass

    label('loc_25C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0300, 4, 0x1804)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_268',
    )

    Event(0, func_0A_16C9)

    def _loc_268(): pass

    label('loc_268')

    Return()

# id: 0x0001 offset: 0x269
@scena.Code('func_01_269')
def func_01_269():
    MapSetFlags(0x02000000)

    Return()

# id: 0x0002 offset: 0x26F
@scena.Code('func_02_26F')
def func_02_26F():
    EventBegin(0x00)
    LoadEffect(0x00, 'map\\\\mp032_00.eff')
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    CameraMove(-17010, 4000, -16370, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3150, 0)
    OP_6C(145000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    CreateThread(0x0008, 0x01, 0x00, func_03_14E8)
    Sleep(1000)

    CreateThread(0x0009, 0x01, 0x00, func_04_152E)
    WaitForThreadExit(0x0009, 0x0001)
    WaitForThreadExit(0x0008, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#3290280001V这边请。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0009, 0, 400)

    ChrTalk(
        0x0009,
        (
            '#0110280002V#273F#2P……哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 0, 400)

    @scena.Lambda('lambda_034C')
    def lambda_034C():
        CameraMove(-6100, 4000, -2470, 7000)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_034C)

    @scena.Lambda('lambda_0364')
    def lambda_0364():
        OP_67(0, 5960, -10000, 7000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0364)

    @scena.Lambda('lambda_037C')
    def lambda_037C():
        OP_6E(255, 7000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_037C)

    @scena.Lambda('lambda_038C')
    def lambda_038C():
        CameraSetDistance(4500, 7000)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_038C)

    CreateThread(0x0008, 0x01, 0x00, func_05_1559)
    Sleep(300)

    CreateThread(0x0009, 0x01, 0x00, func_06_1575)
    WaitForThreadExit(0x0009, 0x0001)
    WaitForThreadExit(0x0008, 0x0000)

    ChrTalk(
        0x0009,
        (
            '#0110280003V#277F#2P呼……\n',
            '保养得十分彻底嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110280004V王国军方面似乎\n',
            '整备得非常完善。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3290280005V#6P哈哈，因为用过几次\n',
            '作为飞行训练嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3290280006V#6P我也亲自操纵过两，三次。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0110280007V#277F#2P实际操纵的\n',
            '感觉怎么样呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3290280008V#6P啊，速度和机动性\n',
            '都在我们军方警备飞艇以上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3290280009V#6P记得是三年前发表的\n',
            '由莱恩福尔特社制造的\n',
            '高速飞艇吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3290280010V#6P失礼了，凡提到飞艇\n',
            '就以为是利贝尔制造的，\n',
            '老实说真令人大吃一惊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0110280011V#277F#2P和贵国的警备艇相比，\n',
            '装甲比较薄弱，\n',
            '也无法搭载太多的武器。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110280012V尽管如此，作为侦察机的话，\n',
            '这制造成本也太高了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110280013V说实话，并不是一艘\n',
            '适合军用的飞船啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3290280014V#6P哦，是这样吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3290280015V#6P唔……明明是艘好飞船，\n',
            '真觉得有点可惜啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0110280016V#272F#2P在我国似乎基本都是\n',
            '作为贵族和资产家的业余爱好\n',
            '来使用的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110280017V那个空贼团，原本\n',
            '也是相同状况吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 180, 400)

    ChrTalk(
        0x0008,
        (
            '#3290280018V#6P记得……\n',
            '是『卡普亚男爵家』的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0009, 0, 400)

    ChrTalk(
        0x0009,
        (
            '#0110280019V#270F#2P是原男爵家。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110280020V由于积欠债务而失去领地，\n',
            '连爵位也被剥夺了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110280021V其实这艘飞船也是抵押品之一，\n',
            '债权人正要求交还呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3290280022V#6P原，原来如此……\n',
            '似乎有不少内情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0110280023V#272F#2P无论如何，原帝国贵族\n',
            '在贵国犯下罪行是事实。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110280024V实在非常抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3290280025V#6P哈哈，不必在意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3290280026V#6P那么何时可以\n',
            '进行交接呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0110280027V#277F#2P快的话就这几天吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110280028V毕竟你们这边似乎\n',
            '也有很多事情要忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3290280029V#6P哈哈……\n',
            '是政变事件的余党吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3290280030V#6P不过是逃亡者在做\n',
            '最后的挣扎而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3290280031V#6P请不必担心，\n',
            '很快就能逮捕归案的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x000A, -17490, 4000, -5790, 180)
    ChrSetChipByIndex(0x000A, 4)

    NpcTalk(
        0x000A,
        '女孩的声音',
        (
            '#0280280032V#1P呜哇～和之前来的时候相比\n',
            '气氛有点不同呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(100)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetPos(0x000A, -17100, 2000, -11000, 180)

    @scena.Lambda('lambda_0AA6')
    def lambda_0AA6():
        CameraMove(-12350, 4000, -10330, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0AA6)

    @scena.Lambda('lambda_0ABE')
    def lambda_0ABE():
        CameraSetDistance(3830, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_0ABE)

    CreateThread(0x000B, 0x01, 0x00, func_07_15A5)
    Sleep(400)

    CreateThread(0x000A, 0x01, 0x00, func_08_15F8)

    @scena.Lambda('lambda_0AE1')
    def lambda_0AE1():
        ChrTurnDirection(0x00FE, 0x000A, 400)
        Yield()

        Jump('lambda_0AE1')

    DispatchAsync2(0x0009, 0x0003, lambda_0AE1)

    Sleep(100)

    @scena.Lambda('lambda_0AF7')
    def lambda_0AF7():
        ChrTurnDirection(0x00FE, 0x000A, 400)
        Yield()

        Jump('lambda_0AF7')

    DispatchAsync2(0x0008, 0x0003, lambda_0AF7)

    Sleep(5000)

    @scena.Lambda('lambda_0B0D')
    def lambda_0B0D():
        CameraMove(-10820, 4000, -7210, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_0B0D)

    WaitForThreadExit(0x000A, 0x0001)
    TerminateThread(0x0009, 0x03)
    TerminateThread(0x0008, 0x03)
    ChrSetDirection(0x000A, 45, 400)
    Sleep(100)

    ChrSetDirection(0x000B, 45, 400)
    WaitForThreadExit(0x000A, 0x0000)

    ChrTalk(
        0x000A,
        (
            '#0280280033V#153F啊啊，空贼艇！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280280034V#150F哦～还放在\n',
            '这个地方啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    ChrSetChipByIndex(0x000A, 5)
    ChrSetSubChip(0x000A, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0280280035V#151F嗯～不错呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280280036V在夜间照明之下的身影\n',
            '也好可爱呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(124, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x000A, 0, 1400, 500, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    PlaySE(124, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x000A, 0, 1400, 500, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    PlaySE(124, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x000A, 0, 1400, 500, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    ChrSetDirection(0x000B, 180, 400)

    ChrTalk(
        0x000B,
        (
            '#2450280037V#6P喂喂，这位小姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2450280038V#6P方便的话请摄影之前\n',
            '先取得批准吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    Fade(250)
    ChrSetChipByIndex(0x000A, 4)
    ChrSetSubChip(0x000A, 0)
    OP_0D()
    ChrSetDirection(0x000A, 180, 600)
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0280280039V#153F#6P#3S啊啊～！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    @scena.Lambda('lambda_0D8F')
    def lambda_0D8F():
        CameraMove(-8500, 4000, -21880, 3000)

        ExitThread()

    DispatchAsync(0x000B, 0x0000, lambda_0D8F)

    @scena.Lambda('lambda_0DA7')
    def lambda_0DA7():
        OP_67(0, 3170, -10000, 3000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0DA7)

    @scena.Lambda('lambda_0DBF')
    def lambda_0DBF():
        OP_6C(169000, 3000)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_0DBF)

    @scena.Lambda('lambda_0DCF')
    def lambda_0DCF():
        CameraSetDistance(4090, 3000)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_0DCF)

    @scena.Lambda('lambda_0DDF')
    def lambda_0DDF():
        OP_6E(262, 3000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0DDF)

    ChrWalkTo(0x000A, -10770, 4000, -13390, 5000, 0x00)
    ChrSetDirection(0x000A, 180, 400)
    WaitForThreadExit(0x0009, 0x0001)

    ChrTalk(
        0x000A,
        (
            '#0280280040V#150F#5P在月光照耀下\n',
            '深夜的迷雾峡谷……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280280041V#151F嗯～多么梦幻\n',
            '又可爱啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    ChrSetChipByIndex(0x000A, 5)
    ChrSetSubChip(0x000A, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0280280042V#151F#5P来，茄～子㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    ChrSetChipByIndex(0x000A, 5)
    ChrSetSubChip(0x000A, 0)
    OP_0D()
    PlaySE(124, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x000A, -300, 1300, 1000, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    PlaySE(124, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x000A, -300, 1300, 1000, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    PlaySE(124, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x000A, -300, 1300, 1000, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    ChrTalk(
        0x000B,
        (
            '#2450280043V#5P我，我说啊～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    Fade(1000)
    CameraMove(-9870, 4000, -5820, 0)
    OP_67(0, 5730, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(145000, 0)
    OP_6E(342, 0)
    ChrSetDirection(0x0009, 180, 0)
    OP_0D()

    ChrTalk(
        0x0009,
        (
            '#0110280044V#273F#5P……她是？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3290280045V#5P哈哈，媒体的人啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3290280046V#5P刚才硬要跑到这个训练场\n',
            '来采访。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3290280047V#5P之前的确是有预约，\n',
            '不过这个时间过来也实在是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0110280048V#272F#5P原来如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    Fade(250)
    ChrSetChipByIndex(0x000A, 4)
    ChrSetSubChip(0x000A, 0)
    OP_0D()
    ChrSetDirection(0x000A, 0, 600)
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0280280049V#153F#3S#6P啊啊啊啊！？',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    @scena.Lambda('lambda_1149')
    def lambda_1149():
        ChrTurnDirection(0x00FE, 0x000A, 400)
        Yield()

        Jump('lambda_1149')

    DispatchAsync2(0x000B, 0x0000, lambda_1149)

    @scena.Lambda('lambda_115A')
    def lambda_115A():
        CameraMove(-10080, 4000, -2580, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_115A)

    ChrWalkTo(0x000A, -10670, 4000, -3900, 5000, 0x00)
    WaitForThreadExit(0x000A, 0x0001)
    TerminateThread(0x000B, 0x00)

    ChrTalk(
        0x000A,
        (
            '#0280280050V#150F哦～穿着没见过的\n',
            '军服呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280280051V个子也好高～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280280052V请问是隶属于\n',
            '哪个部队的呢～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0110280053V#273F#6P……不，我是………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0280280054V#151F啊，还没自我介绍呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280280055V我是『利贝尔通讯』\n',
            '杂志的摄影师\n',
            '朵洛希·海娅特～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280280056V为了杂志的特辑而来这个训练场\n',
            '进行拍照的～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0110280057V#272F#6P……我是隶属于埃雷波尼亚帝国军，\n',
            '驻利贝尔的武官——穆拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0280280058V#153F埃雷波尼亚的军人！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280280059V#151F呜哇～我还是\n',
            '第一次见到呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280280060V因为１０年前的战争时\n',
            '我还住在王都嘛～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0110280061V#270F#6P是，是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_13D5')
    def lambda_13D5():
        CameraMove(-12340, 4000, -8660, 2000)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_13D5)

    Sleep(200)

    CreateThread(0x000C, 0x01, 0x00, func_09_1652)
    WaitForThreadExit(0x000C, 0x0002)
    Sleep(2000)

    @scena.Lambda('lambda_1403')
    def lambda_1403():
        CameraMove(-11560, 4000, -3660, 2000)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_1403)

    WaitForThreadExit(0x000C, 0x0002)
    WaitForThreadExit(0x000C, 0x0001)

    ChrTalk(
        0x000C,
        (
            '#2460280062V队长，打扰一下可以吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3290280063V怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2460280064V从司令部发来的联络。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2460280065V关于那些余党的动向\n',
            '似乎有很大进展。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    ChrClearFlags(0x0000, 0x0080)
    ChrClearFlags(0x0001, 0x0080)
    ChrClearFlags(0x0002, 0x0080)
    ChrClearFlags(0x0003, 0x0080)
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/C1402._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x14E8
@scena.Code('func_03_14E8')
def func_03_14E8():
    ChrSetPos(0x00FE, -16500, 0, -8750, 180)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -16500, 4000, -16500, 3000, 0x00)
    ChrWalkTo(0x00FE, -15140, 4000, -16420, 3000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)

    Return()

# id: 0x0004 offset: 0x152E
@scena.Code('func_04_152E')
def func_04_152E():
    ChrSetPos(0x00FE, -17490, 0, -8830, 180)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -17200, 4000, -16500, 3000, 0x00)

    Return()

# id: 0x0005 offset: 0x1559
@scena.Code('func_05_1559')
def func_05_1559():
    ChrWalkTo(0x00FE, -10510, 4000, 500, 3000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x0006 offset: 0x1575
@scena.Code('func_06_1575')
def func_06_1575():
    ChrWalkTo(0x00FE, -14820, 4000, -16270, 3000, 0x00)
    ChrWalkTo(0x00FE, -10500, 4000, -1230, 3000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x0007 offset: 0x15A5
@scena.Code('func_07_15A5')
def func_07_15A5():
    ChrSetPos(0x00FE, -16500, 0, -8750, 180)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -16500, 4000, -16500, 3000, 0x00)
    ChrMoveToRelative(0x00FE, 2500, 0, 0, 2000, 0x00)
    ChrWalkTo(0x00FE, -12250, 4000, -7160, 3000, 0x00)

    Return()

# id: 0x0008 offset: 0x15F8
@scena.Code('func_08_15F8')
def func_08_15F8():
    ChrSetPos(0x00FE, -17490, 0, -8830, 180)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -17490, 4000, -16500, 3000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)
    ChrMoveToRelative(0x00FE, 2500, 0, 0, 2000, 0x00)
    ChrWalkTo(0x00FE, -12450, 4000, -8460, 3000, 0x00)

    Return()

# id: 0x0009 offset: 0x1652
@scena.Code('func_09_1652')
def func_09_1652():
    ChrSetPos(0x00FE, -16500, 0, -8750, 180)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_1679')
    def lambda_1679():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1679)

    ChrWalkTo(0x00FE, -17490, 4000, -16500, 4000, 0x00)
    ChrMoveToRelative(0x00FE, 2500, 0, 0, 4000, 0x00)
    ChrWalkTo(0x00FE, -13700, 4000, -6390, 4000, 0x00)
    ChrSetDirection(0x00FE, 0, 0)

    Return()

# id: 0x000A offset: 0x16C9
@scena.Code('func_0A_16C9')
def func_0A_16C9():
    EventBegin(0x00)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    CameraMove(-17010, 4000, -16370, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(145000, 0)
    OP_6E(262, 0)
    CreateThread(0x0129, 0x01, 0x00, func_0B_19D6)
    Sleep(500)

    CreateThread(0x012A, 0x01, 0x00, func_0C_1A01)
    Sleep(500)

    CreateThread(0x0146, 0x01, 0x00, func_0D_1A2C)
    Sleep(500)

    CreateThread(0x0102, 0x01, 0x00, func_0E_1A57)
    WaitForThreadExit(0x0129, 0x0001)
    ChrSetDirection(0x0129, 45, 400)

    ChrTalk(
        0x0129,
        (
            '#0300280241V#192F#2P喔喔……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_177D')
    def lambda_177D():
        CameraMove(-7610, 4000, -1690, 7000)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_177D)

    @scena.Lambda('lambda_1795')
    def lambda_1795():
        OP_67(0, 5790, -10000, 7000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_1795)

    @scena.Lambda('lambda_17AD')
    def lambda_17AD():
        OP_6E(255, 7000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_17AD)

    @scena.Lambda('lambda_17BD')
    def lambda_17BD():
        CameraSetDistance(4660, 7000)

        ExitThread()

    DispatchAsync(0x0129, 0x0003, lambda_17BD)

    CreateThread(0x0129, 0x01, 0x00, func_0F_1A82)
    Sleep(300)

    CreateThread(0x012A, 0x01, 0x00, func_10_1AB2)
    Sleep(300)

    CreateThread(0x0146, 0x01, 0x00, func_11_1AF6)
    Sleep(400)

    CreateThread(0x0102, 0x01, 0x00, func_12_1B3A)
    WaitForThreadExit(0x0146, 0x0001)

    ChrTalk(
        0x0129,
        (
            '#0300280242V#191F#6P可爱的『山猫号』……\n',
            '真想死你了～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0146,
        (
            '#0090280243V#211F看起来\n',
            '保养得很好呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012A,
        (
            '#0290280244V#202F#5P嘿嘿，不愧是利贝尔军。\n',
            '知道该怎么样好好对待飞船。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020280245V#1035F#2P我知道你们很高兴，\n',
            '不过时间所剩不多了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020280246V#1030F而且启动钥匙\n',
            '现在还没找到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x012A, 180, 400)

    ChrTalk(
        0x012A,
        (
            '#0290280247V#200F#6P是是，知道啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0129, 180, 400)
    ChrSetDirection(0x0146, 180, 400)

    ChrTalk(
        0x0129,
        (
            '#0300280248V#198F#6P真是的……\n',
            '再让我们沉浸一下嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0146,
        (
            '#0090280249V#210F#6P启动钥匙要是\n',
            '留在船里就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0300, 4, 0x1804))
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

# id: 0x000B offset: 0x19D6
@scena.Code('func_0B_19D6')
def func_0B_19D6():
    ChrSetPos(0x00FE, -17220, 0, -8680, 180)
    ChrClearFlags(0x00FE, 0x0080)
    ChrMoveToRelative(0x00FE, 0, 0, -8000, 3000, 0x00)

    Return()

# id: 0x000C offset: 0x1A01
@scena.Code('func_0C_1A01')
def func_0C_1A01():
    ChrSetPos(0x00FE, -17220, 0, -8680, 180)
    ChrClearFlags(0x00FE, 0x0080)
    ChrMoveToRelative(0x00FE, 0, 0, -6820, 3000, 0x00)

    Return()

# id: 0x000D offset: 0x1A2C
@scena.Code('func_0D_1A2C')
def func_0D_1A2C():
    ChrSetPos(0x00FE, -17220, 0, -8680, 180)
    ChrClearFlags(0x00FE, 0x0080)
    ChrMoveToRelative(0x00FE, 0, 0, -5820, 3000, 0x00)

    Return()

# id: 0x000E offset: 0x1A57
@scena.Code('func_0E_1A57')
def func_0E_1A57():
    ChrSetPos(0x00FE, -17220, 0, -8680, 180)
    ChrClearFlags(0x00FE, 0x0080)
    ChrMoveToRelative(0x00FE, 0, 0, -4820, 3000, 0x00)

    Return()

# id: 0x000F offset: 0x1A82
@scena.Code('func_0F_1A82')
def func_0F_1A82():
    ChrMoveToRelative(0x00FE, 2500, 0, 0, 3000, 0x00)
    ChrWalkTo(0x00FE, -10500, 4000, 730, 3000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x0010 offset: 0x1AB2
@scena.Code('func_10_1AB2')
def func_10_1AB2():
    ChrMoveToRelative(0x00FE, 0, 0, -1000, 3000, 0x00)
    ChrMoveToRelative(0x00FE, 2500, 0, 0, 3000, 0x00)
    ChrWalkTo(0x00FE, -10770, 4000, -480, 3000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x0011 offset: 0x1AF6
@scena.Code('func_11_1AF6')
def func_11_1AF6():
    ChrMoveToRelative(0x00FE, 0, 0, -2000, 3000, 0x00)
    ChrMoveToRelative(0x00FE, 2500, 0, 0, 3000, 0x00)
    ChrWalkTo(0x00FE, -12060, 4000, 720, 3000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x0012 offset: 0x1B3A
@scena.Code('func_12_1B3A')
def func_12_1B3A():
    ChrMoveToRelative(0x00FE, 0, 0, -3000, 3000, 0x00)
    ChrMoveToRelative(0x00FE, 2500, 0, 0, 3000, 0x00)
    ChrWalkTo(0x00FE, -11760, 4000, -1610, 3000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x0013 offset: 0x1B7E
@scena.Code('func_13_1B7E')
def func_13_1B7E():
    ExecExpressionWithValue(
        0x000D,
        0x01,
        (
            (Expr.GetChrWork, 0x0, 0x1),
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x02,
        (
            (Expr.GetChrWork, 0x0, 0x2),
            (Expr.GetChrWork, 0x0, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x03,
        (
            (Expr.GetChrWork, 0x0, 0x3),
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x01,
        (
            (Expr.GetChrWork, 0x1, 0x1),
            (Expr.GetChrWork, 0x1, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x02,
        (
            (Expr.GetChrWork, 0x1, 0x2),
            (Expr.GetChrWork, 0x1, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x03,
        (
            (Expr.GetChrWork, 0x1, 0x3),
            (Expr.GetChrWork, 0x1, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x01,
        (
            (Expr.GetChrWork, 0x2, 0x1),
            (Expr.GetChrWork, 0x2, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x02,
        (
            (Expr.GetChrWork, 0x2, 0x2),
            (Expr.GetChrWork, 0x2, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x03,
        (
            (Expr.GetChrWork, 0x2, 0x3),
            (Expr.GetChrWork, 0x2, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    CreateThread(0x0000, 0x01, 0x00, func_17_1D40)
    CreateThread(0x0001, 0x01, 0x00, func_16_1D04)
    CreateThread(0x0002, 0x01, 0x00, func_15_1CBA)
    CreateThread(0x0003, 0x01, 0x00, func_14_1C62)
    WaitForThreadExit(0x0003, 0x0001)
    OP_30(0x00)
    TalkEnd(0x00FF)

    Return()

# id: 0x0014 offset: 0x1C62
@scena.Code('func_14_1C62')
def func_14_1C62():
    ChrSetFlags(0x00FE, 0x0004)
    OP_92(0x00FE, 0x000F, 0, 6000, 0x00)
    OP_92(0x00FE, 0x000E, 0, 6000, 0x00)
    OP_92(0x00FE, 0x000D, 0, 6000, 0x00)
    ChrSetDirection(0x00FE, 90, 0)
    ChrSetSubChip(0x00FE, 0)
    ChrJumpTo(0x00FE, -8900, 5510, -640, 2000, 5000)
    ChrClearFlags(0x00FE, 0x0004)

    Return()

# id: 0x0015 offset: 0x1CBA
@scena.Code('func_15_1CBA')
def func_15_1CBA():
    ChrSetFlags(0x00FE, 0x0004)
    OP_92(0x00FE, 0x000E, 0, 6000, 0x00)
    OP_92(0x00FE, 0x000D, 0, 6000, 0x00)
    ChrSetDirection(0x00FE, 90, 0)
    ChrSetSubChip(0x00FE, 0)
    ChrJumpTo(0x00FE, -8900, 5510, -640, 2000, 5000)
    ChrClearFlags(0x00FE, 0x0004)

    Return()

# id: 0x0016 offset: 0x1D04
@scena.Code('func_16_1D04')
def func_16_1D04():
    ChrSetFlags(0x00FE, 0x0004)
    OP_92(0x00FE, 0x000D, 0, 6000, 0x00)
    ChrSetDirection(0x00FE, 90, 0)
    ChrSetSubChip(0x00FE, 0)
    ChrJumpTo(0x00FE, -8900, 5510, -640, 2000, 5000)
    ChrClearFlags(0x00FE, 0x0004)

    Return()

# id: 0x0017 offset: 0x1D40
@scena.Code('func_17_1D40')
def func_17_1D40():
    ChrSetFlags(0x00FE, 0x0004)
    ChrSetDirection(0x00FE, 90, 0)
    ChrSetSubChip(0x00FE, 0)
    ChrJumpTo(0x00FE, -8900, 5510, -640, 2000, 5000)
    ChrClearFlags(0x00FE, 0x0004)

    Return()

# id: 0x0018 offset: 0x1D6E
@scena.Code('func_18_1D6E')
def func_18_1D6E():
    ExecExpressionWithValue(
        0x000D,
        0x01,
        (
            (Expr.GetChrWork, 0x0, 0x1),
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x02,
        (
            (Expr.GetChrWork, 0x0, 0x2),
            (Expr.GetChrWork, 0x0, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x03,
        (
            (Expr.GetChrWork, 0x0, 0x3),
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x01,
        (
            (Expr.GetChrWork, 0x1, 0x1),
            (Expr.GetChrWork, 0x1, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x02,
        (
            (Expr.GetChrWork, 0x1, 0x2),
            (Expr.GetChrWork, 0x1, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x03,
        (
            (Expr.GetChrWork, 0x1, 0x3),
            (Expr.GetChrWork, 0x1, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x01,
        (
            (Expr.GetChrWork, 0x2, 0x1),
            (Expr.GetChrWork, 0x2, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x02,
        (
            (Expr.GetChrWork, 0x2, 0x2),
            (Expr.GetChrWork, 0x2, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x03,
        (
            (Expr.GetChrWork, 0x2, 0x3),
            (Expr.GetChrWork, 0x2, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    CreateThread(0x0000, 0x01, 0x00, func_1C_1F30)
    CreateThread(0x0001, 0x01, 0x00, func_1B_1EF4)
    CreateThread(0x0002, 0x01, 0x00, func_1A_1EAA)
    CreateThread(0x0003, 0x01, 0x00, func_19_1E52)
    WaitForThreadExit(0x0003, 0x0001)
    OP_30(0x00)
    TalkEnd(0x00FF)

    Return()

# id: 0x0019 offset: 0x1E52
@scena.Code('func_19_1E52')
def func_19_1E52():
    ChrSetFlags(0x00FE, 0x0004)
    OP_92(0x00FE, 0x000F, 0, 6000, 0x00)
    OP_92(0x00FE, 0x000E, 0, 6000, 0x00)
    OP_92(0x00FE, 0x000D, 0, 6000, 0x00)
    ChrSetDirection(0x00FE, 270, 0)
    ChrSetSubChip(0x00FE, 0)
    ChrJumpTo(0x00FE, -11000, 4000, -1990, 500, 5000)
    ChrClearFlags(0x00FE, 0x0004)

    Return()

# id: 0x001A offset: 0x1EAA
@scena.Code('func_1A_1EAA')
def func_1A_1EAA():
    ChrSetFlags(0x00FE, 0x0004)
    OP_92(0x00FE, 0x000E, 0, 6000, 0x00)
    OP_92(0x00FE, 0x000D, 0, 6000, 0x00)
    ChrSetDirection(0x00FE, 270, 0)
    ChrSetSubChip(0x00FE, 0)
    ChrJumpTo(0x00FE, -11000, 4000, -1990, 500, 5000)
    ChrClearFlags(0x00FE, 0x0004)

    Return()

# id: 0x001B offset: 0x1EF4
@scena.Code('func_1B_1EF4')
def func_1B_1EF4():
    ChrSetFlags(0x00FE, 0x0004)
    OP_92(0x00FE, 0x000D, 0, 6000, 0x00)
    ChrSetDirection(0x00FE, 270, 0)
    ChrSetSubChip(0x00FE, 0)
    ChrJumpTo(0x00FE, -11000, 4000, -1990, 500, 5000)
    ChrClearFlags(0x00FE, 0x0004)

    Return()

# id: 0x001C offset: 0x1F30
@scena.Code('func_1C_1F30')
def func_1C_1F30():
    ChrSetFlags(0x00FE, 0x0004)
    ChrSetDirection(0x00FE, 270, 0)
    ChrSetSubChip(0x00FE, 0)
    ChrJumpTo(0x00FE, -11000, 4000, -1990, 500, 5000)
    ChrClearFlags(0x00FE, 0x0004)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
