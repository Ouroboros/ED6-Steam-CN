import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4112_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4112   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4112.x'
    header.mapIndex       = 1
    header.bgm            = 81
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
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT07/CH02190._CH', 'ED6_DT07/CH02190P._CP'),
        ('ED6_DT07/CH00133._CH', 'ED6_DT07/CH00133P._CP'),
        ('ED6_DT07/CH00035._CH', 'ED6_DT07/CH00035P._CP'),
    ]

# id: 0x10001 offset: 0xCA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '奥利维尔',
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
    )

# id: 0x10002 offset: 0x10A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x10A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x10A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x10A
@scena.Code('Init')
def Init():
    OP_26(137)
    MapSetFlags(0x10000000)
    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_02_12B)

    Return()

# id: 0x0001 offset: 0x11A
@scena.Code('func_01_11A')
def func_01_11A():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 2, 0x66A)),
            Expr.Return,
        ),
        'loc_12A',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x4B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_12A(): pass

    label('loc_12A')

    Return()

# id: 0x0002 offset: 0x12B
@scena.Code('func_02_12B')
def func_02_12B():
    MapClearFlags(0x10000000)
    MapClearFlags(0x02000000)
    EventBegin(0x00)
    OP_24(0x01C9, 0x4B)
    OP_77(0xC9, 0xC9, 0xFF, 0x00, 0x00000000)
    ChrSetPos(0x0008, -940, 0, 4500, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    ChrSetFlags(0x0004, 0x0080)
    CameraMove(370, 0, 5650, 0)
    OP_67(0, 5170, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(273, 0)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetFlags(0x0009, 0x0004)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0040100052V#035F美丽的王都笼罩着乌云，\n',
            '昏暗的热情序曲正在奏响……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040100053V#030F嘻嘻……\n',
            '这不是很有趣吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_72(0x0000, 0x0010)
    OP_6F(0x0000, 30)
    PlaySE(6, 0x00, 0x64)
    Sleep(500)

    ChrSetPos(0x0009, 6430, 0, -20, 270)
    ChrClearFlags(0x0009, 0x0080)

    NpcTalk(
        0x0009,
        '男人的声音',
        (
            '#0110100054V……还是老样子，真是悠闲啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_02BF')
    def lambda_02BF():
        ChrTurnDirection(0x0008, 0x0009, 400)
        Yield()

        Jump('lambda_02BF')

    DispatchAsync2(0x0008, 0x0003, lambda_02BF)

    @scena.Lambda('lambda_02D0')
    def lambda_02D0():
        CameraMove(2800, 0, 3250, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_02D0)

    @scena.Lambda('lambda_02E8')
    def lambda_02E8():
        OP_6E(318, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_02E8)

    ChrWalkTo(0x0009, 4070, 0, 90, 2000, 0x00)
    ChrSetDirection(0x0009, 270, 400)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0040100055V#033F#5P哦哦……\n',
            '你能领略到我的梦中情景吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040100056V#031F穆拉，我亲爱的朋友！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040100057V一向那么繁忙的你，\n',
            '竟然特地从帝都来到这里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040100058V今天到底是吹的什么风啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_72(0x0000, 0x0800)
    PlaySE(7, 0x00, 0x64)
    OP_71(0x0000, 0x0010)
    OP_70(0x0000, 0)

    @scena.Lambda('lambda_03F1')
    def lambda_03F1():
        CameraMove(490, 0, 4019, 1500)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_03F1)

    ChrWalkTo(0x0009, -620, 0, 2620, 3000, 0x00)
    ChrSetDirection(0x0009, 0, 400)
    TerminateThread(0x0008, 0x03)

    ChrTalk(
        0x0009,
        (
            '#0110100059V#270F你在装什么傻……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110100060V还不是因为你一直不和我联络，\n',
            '到处闲逛吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110100061V这不是给我添麻烦嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0040100062V#035F#5P哼哼，不用害羞了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040100063V虽然嘴上说得如此无情，\n',
            '其实还不是因为担心我，\n',
            '才像飞艇那般迅速地赶过来吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040100064V人们不是常说，恋爱是盲目的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0110100065V#273F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0040100066V#031F#5P好了，不要再考虑了，\n',
            '赶快飞奔过来扑到我的怀里吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0110100067V#272F我特地带过来的，\n',
            '是你拜托我调查的情报……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110100068V看样子，你是不想知道了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0040100069V#036F#5P讨厌～\n',
            '不要说这么过分的话嘛～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040100070V#035F我明白了。\n',
            '你是要我拿出诚意对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0110100071V#270F这应该是理所当然的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0040100072V#030F#5P这种小事就请看好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040100073V#035F咳咳……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrSetChipByIndex(0x0008, 2)
    ChrSetSubChip(0x0008, 1)
    OP_99(0x0008, 0x01, 0x02, 1000)
    OP_62(0x0008, 0x0000012C, 1600, 0x36, 0x39, 0x000000FA, 0x00)
    PlaySE(137, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0040100074V#031F#5P拜托您了，我的主人☆',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040100075V#031F#5P请务必告诉人家㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1600)

    OP_63(0x0009)
    Sleep(500)

    OP_63(0x0008)

    ChrTalk(
        0x0008,
        (
            '#0040100076V#033F#5P啊，不对是吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040100077V#035F那么，下一个是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    ChrSetChipByIndex(0x0008, 3)
    ChrSetSubChip(0x0008, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0040100078V#039F#3S#5P大哥！\n',
            '这是我一生的心愿啊啊啊啊！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0040100079V#039F#3S#5P请一定告诉我啊啊啊啊！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1200)

    ChrTalk(
        0x0009,
        (
            '#0110100080V#274F够了……\n',
            '我头都要晕了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110100081V你快给我闭嘴，我这就告诉你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 0)
    OP_0D()
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0040100082V#031F#5P哇～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0110100083V#270F『那个人』的……\n',
            '行踪终于被我们发现了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110100084V大概一个月之前，\n',
            '在帝国的游击士协会里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0040100085V#033F#5P哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0110100086V#270F在这几个月里，\n',
            '帝国各地的协会支部陆续受到了袭击。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110100087V他好像在调查这件事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0040100088V#030F#5P袭击啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040100089V虽然觉得有点不大可能，\n',
            '但会不会是哪里的部队干的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0110100090V#272F这确实不大可能……\n',
            '现在毕竟已经和十年前不一样了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110100091V据我所知，\n',
            '所有的部队都没有接到出动的命令。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110100092V很有可能是某人雇佣了猎兵团\n',
            '犯下这些案件的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110100093V#270F而且到了最后，事件得到解决的同时，\n',
            '又失去了那个人的行踪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0040100094V#034F#5P呼……被耍了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040100095V虽然来到了利贝尔王国，\n',
            '但是这个结果并不是我想要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0110100096V#270F没错，就是这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110100097V目标人物已经不在了，\n',
            '你还有留在这里的必要吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110100098V好像有一场比想象中\n',
            '更加激烈的暴风雨就要临近了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110100099V被卷进去之前，还是赶快回帝都吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0040100100V#031F#5P哈·哈·哈，别开玩笑了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040100101V好戏正要上演，\n',
            '本人没理由中途退席的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0110100102V#273F……什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110100103V#271F喂，难道你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0DDC')
    def lambda_0DDC():
        ChrSetDirection(0x0008, 0, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0DDC)

    @scena.Lambda('lambda_0DEA')
    def lambda_0DEA():
        OP_6E(290, 1500)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0DEA)

    CameraMove(-250, 0, 5610, 1500)

    ChrTalk(
        0x0008,
        (
            '#0040100104V#035F#6P演员已经到齐了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040100105V虽然主演不在，不过替补演员嘛……\n',
            '本人心中已经有数了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040100106V#030F那两个人，肯定会凭借自己的力量，\n',
            '在这广大的舞台上有所作为的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    MapClearFlags(0x00100000)
    Sleep(1000)

    OP_AD('ED6_DT04/C_VIS044._CH', 0x0000, 0x0000, 0x00000064)
    Sleep(4000)

    OP_56(0x02)
    OP_AE(0x000000C8)
    Sleep(2000)

    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T3120._SN', 100, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
