import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C3300_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C3300   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'C3300.x'
    header.mapIndex       = 1
    header.bgm            = 32
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x6C8
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x000186A0,
            dword_04        = 0x00000000,
            dword_08        = 0xFFFE7960,
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
        ('ED6_DT09/CH10630._CH', 'ED6_DT09/CH10630P._CP'),
        ('ED6_DT09/CH10631._CH', 'ED6_DT09/CH10631P._CP'),
        ('ED6_DT09/CH10640._CH', 'ED6_DT09/CH10640P._CP'),
        ('ED6_DT09/CH10641._CH', 'ED6_DT09/CH10641P._CP'),
        ('ED6_DT09/CH10650._CH', 'ED6_DT09/CH10650P._CP'),
        ('ED6_DT09/CH10651._CH', 'ED6_DT09/CH10651P._CP'),
        ('ED6_DT09/CH10660._CH', 'ED6_DT09/CH10660P._CP'),
        ('ED6_DT09/CH10661._CH', 'ED6_DT09/CH10661P._CP'),
        ('ED6_DT09/CH10670._CH', 'ED6_DT09/CH10670P._CP'),
        ('ED6_DT09/CH10671._CH', 'ED6_DT09/CH10671P._CP'),
        ('ED6_DT09/CH10680._CH', 'ED6_DT09/CH10680P._CP'),
        ('ED6_DT09/CH10681._CH', 'ED6_DT09/CH10681P._CP'),
        ('ED6_DT09/CH10690._CH', 'ED6_DT09/CH10690P._CP'),
        ('ED6_DT09/CH10691._CH', 'ED6_DT09/CH10691P._CP'),
    ]

# id: 0x10002 offset: 0x11A
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0x11A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = 93670,
            z           = -30,
            y           = -101140,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01E2,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 105420,
            z           = 140,
            y           = -100870,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01E4,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 75750,
            z           = -50,
            y           = -78300,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01E3,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 106940,
            z           = 20,
            y           = -79600,
            word_0C     = 0x00B4,
            word_0E     = 0x000C,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01E7,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x18A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x18A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 39780,
            triggerZ            = -60,
            triggerY            = -82680,
            triggerRange        = 1000,
            actorX              = 39410,
            actorZ              = 1440,
            actorY              = -82290,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1AE
@scena.Code('PreInit')
def PreInit():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_1BA'),
        (-1, 'loc_1D0'),
    )

    def _loc_1BA(): pass

    label('loc_1BA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 3, 0x553)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 2, 0x552)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1CD',
    )

    SetScenaFlags(ScenaFlag(0x00AA, 3, 0x553))
    Event(0, 0x0002)

    def _loc_1CD(): pass

    label('loc_1CD')

    Jump('loc_1D0')

    def _loc_1D0(): pass

    label('loc_1D0')

    Return()

# id: 0x0001 offset: 0x1D1
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B8, 0, 0x5C0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1E3',
    )

    OP_6F(0x0000, 0)

    Jump('loc_1EA')

    def _loc_1E3(): pass

    label('loc_1E3')

    OP_6F(0x0000, 60)

    def _loc_1EA(): pass

    label('loc_1EA')

    PlaySE(461, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x1F0
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x00)
    SetChrPos(0x0101, 93760, 40, -147630, 0)
    SetChrPos(0x0108, 93830, 20, -149190, 0)
    SetChrPos(0x0102, 94540, 40, -148410, 0)
    SetChrPos(0x0107, 92640, -20, -148560, 0)
    CameraMove(92040, -100, -111390, 0)
    OP_67(0, 3470, -10000, 0)
    CameraSetDistance(5000, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_0282')
    def lambda_0282():
        OP_67(0, 8000, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0282)

    @scena.Lambda('lambda_029A')
    def lambda_029A():
        CameraMove(93740, 30, -148330, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_029A)

    Sleep(1000)

    @scena.Lambda('lambda_02B7')
    def lambda_02B7():
        OP_6C(135000, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_02B7)

    CameraSetDistance(3200, 7000)

    ChrTalk(
        0x0101,
        (
            '#0010081513V#501F这里就是钟乳洞啊……\n',
            '感觉是个很神秘的地方呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080081514V#070F不过……\n',
            '从里面传来很重的魔兽气息。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080081515V看来要花一番工夫来找了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070081516V#065F哎，唔唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0107, 400)

    ChrTalk(
        0x0101,
        (
            '#0010081517V#002F提妲，要是害怕的话，\n',
            '现在离开这里也可以哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010081518V不能太勉强自己哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_03E2')
    def lambda_03E2():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_03E2)

    @scena.Lambda('lambda_03F0')
    def lambda_03F0():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_03F0)

    ChrTurnDirection(0x0107, 0x0101, 400)

    ChrTalk(
        0x0107,
        (
            '#0070081519V#067F没、没关系呢……\n',
            '虽然有点害怕，但我没勉强自己。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070081520V#560F总之，我们快点去找找哪儿有\n',
            '『塞姆里亚苔藓』吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081521V#006F是啊……快点走吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010081522V嗯，雾香姐说过，\n',
            '苔藓是生长在洞窟湖的岸边对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020081523V#012F嗯，应该是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020081524V顺带一提，\n',
            '洞窟湖好像是在钟乳洞的西北方向。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080081525V#070F嗯，把握了方向和位置，\n',
            '接下来我们就谨慎地前进吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x0003 offset: 0x57A
@scena.Code('func_03_57A')
def func_03_57A():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B8, 0, 0x5C0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_67C',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01FF, 1)"),
            Expr.Return,
        ),
        'loc_5F6',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            'ＥＰ改良填充剂',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00B8, 0, 0x5C0))

    Jump('loc_679')

    def _loc_5F6(): pass

    label('loc_5F6')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            'ＥＰ改良填充剂',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            'ＥＰ改良填充剂',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0)

    def _loc_679(): pass

    label('loc_679')

    Jump('loc_6B2')

    def _loc_67C(): pass

    label('loc_67C')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱里什么东西都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    WaitEffect(0x0F, 0x25)
    def _loc_6B2(): pass

    label('loc_6B2')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
